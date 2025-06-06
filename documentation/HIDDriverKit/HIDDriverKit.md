# HIDDriverKit

**Framework**: Hiddriverkit  
**Kind**: module

Develop drivers for human-interface devices, such as keyboards, pointing devices, and digitizers like pens and touch pads.

**Availability**:
- DriverKit 19.0+
- macOS 10.15+

#### Overview

The HIDDriverKit framework provides C++ classes for developing drivers for human interface devices. HIDDriverKit uses the core types defined in [`DriverKit`](https://developer.apple.com/documentation/DriverKit), and adds features specific to human interface device development.

Develop your driver with DriverKit and HIDDriverKit, and package it in an app that uses the [`System Extensions`](https://developer.apple.com/documentation/SystemExtensions) framework to install and upgrade the driver on the user’s Mac.

> **Note**:  HIDDriverKit is available on macOS.

## Topics

### Essentials
- [com.apple.developer.driverkit.transport.hid](../BundleResources/Entitlements/com.apple.developer.driverkit.transport.hid.md)
  A Boolean value that indicates whether the driver communicates with human interface devices.
- [Handling Keyboard Events from a Human Interface Device](handling-keyboard-events-from-a-human-interface-device.md)
  Process keyboard-related data from a human interface device and dispatch events to the system.
- [Handling Stylus Input from a Human Interface Device](handling-stylus-input-from-a-human-interface-device.md)
  Process stylus-related input from a human interface device and dispatch events to the system.
### Samples
- [DriverKit sample code](../DriverKit/driverkit-sample-code.md)
  Explore projects that demonstrate how to write macOS device drivers with the DriverKit family of frameworks.
### Driver Interfaces
- [com.apple.developer.driverkit.family.hid.eventservice](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.eventservice.md)
  A Boolean value that indicates whether the driver provides a HID-related event service to the system.
- [IOUserHIDEventDriver](iouserhideventdriver.md)
  A complete driver object that dispatches keyboard, digitizer, scrolling, and pointer events originating from a HID device.
- [IOUserHIDEventService](iouserhideventservice.md)
  A service that parses HID report data into elements that you can use to dispatch events.
- [IOHIDEventService](iohideventservice.md)
  The base class for implementing a device or operating system service that dispatches events to the system.
### Providers
- [com.apple.developer.driverkit.family.hid.device](../BundleResources/Entitlements/com.apple.developer.driverkit.family.hid.device.md)
  A Boolean value that indicates whether the driver provides a HID-related service to the system.
- [IOHIDInterface](iohidinterface.md)
  A provider object for a HID device’s interface.
- [IOUserUSBHostHIDDevice](iouserusbhosthiddevice.md)
  A provider object for USB devices that support HID interactions.
- [IOUserHIDDevice](iouserhiddevice.md)
  A provider object for devices that support interactions with users.
- [IOHIDDevice](iohiddevice.md)
  An object containing the low-level behavior for all HID device providers.
### Events
- [IOHIDDigitizerStylusData](iohiddigitizerstylusdata.md)
  A structure containing digitizer stylus data.
- [IOHIDDigitizerTouchData](iohiddigitizertouchdata.md)
  A structure containing the current digitizer touch data.
### HID Usage Tables
- [HID Usage Tables](hid-usage-tables.md)
  Identify the types of data that HID devices can report to your driver.
- [Match Criteria](match-criteria.md)
  Specify the criteria that the system uses to match your driver to a device.
### HID Device Data
- [IOHIDElement](iohidelement.md)
  An object that contains parsed information from a HID input report.
- [IOHIDDigitizerCollection](iohiddigitizercollection.md)
  A collection of elements that contain digitizer-related data.
- [com.apple.developer.hid.virtual.device](../BundleResources/Entitlements/com.apple.developer.hid.virtual.device.md)
  A Boolean value that indicates whether the driver creates a virtual HID device.
- [Low-Level Information](low-level-information.md)
  Understand the underlying structures that support HID drivers.
### Reference
- [HIDDriverKit Macros](hiddriverkit-macros.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/HIDDriverKit)*