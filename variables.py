import numpy as np
import math
import scipy.constants as const


g = const.g  # gravitational constant
rod_length = 67 # total length of rod
x_length = 0.75  # Length of x
length_ratio = 3.75  # y/x
y_length = x_length * length_ratio  # Length of y
counterweight = 1000  # Mass of the counterweight
fruit_weight = 1  # Mass of the fruit (kg)
initial_angle = -45  # Horizontal level arm Initial angle (degree)
launch_angle = 45  # Launch Angle (degree)
rod_weight = 0.168  # mass of the rod
pi = math.pi


# When the coefficient is very large, it could cause stack overflow

dt = 1e-5  # integration time step (delta t)
'''
v0 = 35  # Average speed at t=0
v0min = 30  # Minimum Speed
v0max = 40  # Maximum Speed
'''
time = np.arange(0, 2000, dt)  # create time axis
c = 0.47  # Drag Coefficient
p = 1.225  # Density of the air (kg/m^3)
A = 0.01  # Surface Area (m^2)
inity = 0  # Initial height (m)
windx = 0  # Wind velocity in the x direction（vector) (m/s)
wind_y = 0  # Wind velocity in the y direction（vector) (m/s)

launch_angle = launch_angle / 180 * math.pi  # Convert to radian