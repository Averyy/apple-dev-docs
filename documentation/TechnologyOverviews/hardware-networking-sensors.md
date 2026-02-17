# Hardware, networking, and sensors

**Framework**: Technology Overviews

Access device-related sensors, connect to a network, and build low-level drivers and software to support custom hardware.

Sensors and hardware help you create software that connects people to the real world. Sensors like accelerometers, gyroscopes, GPS, and others give contextual information about the physical state of the device such as its movement and location. Wi-Fi, Bluetooth, and Ethernet connect to other devices and to the Internet, giving you access to additional information and services.

Access the hardware for a device using system frameworks, which insulate you from device- or hardware-specific details. The system frameworks give you access to the features you want while minimizing your code’s impact on battery life, system performance, and other apps. The frameworks also help the device owner protect their personal data, keeping them informed of which apps use that data and giving them controls to manage that access.

#### Device Sensors

Sensor hardware provides information about the physical state of a device or its surrounding environment. Use sensor-related data as direct input to your app, or as additional context for your app to use when generating content. For example:

#### Networking and Communication

Devices access local networks and the Internet using hardware such as Wi-Fi, cellular, Bluetooth, or Ethernet. The system frameworks you use to connect to the Internet let you focus on the tasks you want to perform more than the network connection itself. Use these frameworks to browse the web or fetch resources, communicate with your company’s RESTful endpoints, or implement voice or video conversation tools. For example:

#### Hardware Level Interactions

Developers occasionally need to work more closely with Apple silicon or the underlying hardware. Discover connected hardware accessories and communicate with them using the built-in device drivers. Create custom drivers to support the features unique to your company’s accessories, and optimize your code for Apple silicon to take maximum advantage of the available hardware. For example:

## Topics

- [Device sensors](device-sensors.md)
  Adjust your app’s behavior using contextual data you receive from a device’s built-in sensors.
- [Networking and communication](networking-and-communication.md)
  Communicate with other devices over a network, extend the system’s core networking capabilities, and incorporate telephony into your apps.
- [Hardware-level interactions](hardware-level-interactions.md)
  Communicate with connected hardware and write code that runs well on Apple silicon.


---

*[View on Apple Developer](https://developer.apple.com/documentation/technologyoverviews/hardware-networking-sensors)*