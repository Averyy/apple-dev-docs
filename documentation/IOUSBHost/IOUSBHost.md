# IOUSBHost

**Framework**: IOUSBHost  
**Kind**: module

Create host-mode user space drivers for USB devices.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

#### Overview

With the [`IOUSBHost`](IOUSBHost.md) framework, you can access custom and non–class-compliant USB devices from within your apps. Use this framework to connect to cameras, audio devices, scanners, printers, keyboards, mouse devices, MIDI keyboards, and USB hubs.

This framework refers to the USB Implementers Forum (USB-IF) , Revision 1.0, September 22, 2017. You can view this specification at [`http://www.usb.org/`](https://developer.apple.comhttp://www.usb.org/).

## Topics

### Function Drivers
- [class IOUSBHostInterface](iousbhostinterface.md)
  The class for accessing USB-related services.
- [class IOUSBHostPipe](iousbhostpipe.md)
  The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.
- [class IOUSBHostStream](iousbhoststream.md)
  The class responsible for sending stream data for function drivers.
### Device Drivers
- [class IOUSBHostDevice](iousbhostdevice.md)
  The class that claims and configures devices, retrieves descriptors, and sends device requests.
### Base Classes
- [class IOUSBHostObject](iousbhostobject.md)
  This class provides basic functionality for sending device requests and retrieving descriptors.
- [class IOUSBHostIOSource](iousbhostiosource.md)
  This class provides basic functionality for deriving pipe and stream classes.
### IOServicePlane Properties
- [struct IOUSBHostInterfacePropertyKey](iousbhostinterfacepropertykey.md)
  Properties of a USB interface that describe its state.
- [struct IOUSBHostDevicePropertyKey](iousbhostdevicepropertykey.md)
  Properties of a USB device that describe its state.
- [struct IOUSBHostMatchingPropertyKey](iousbhostmatchingpropertykey.md)
  Properties for implementing the matching service.
- [typealias IOUSBHostPropertyKey](iousbhostpropertykey.md)
  Properties that the USB host device and interface classes share.
### Error Domain
- [let IOUSBHostErrorDomain: String](iousbhosterrordomain.md)
  The error domain for the framework.
### Classes
- [class IOUSBHostCIControllerStateMachine](iousbhostcicontrollerstatemachine.md)
- [class IOUSBHostCIDeviceStateMachine](iousbhostcidevicestatemachine.md)
- [class IOUSBHostCIEndpointStateMachine](iousbhostciendpointstatemachine.md)
- [class IOUSBHostCIPortStateMachine](iousbhostciportstatemachine.md)
- [class IOUSBHostControllerInterface](iousbhostcontrollerinterface.md)
### Reference
- [IOUSBHost Structures](iousbhost-structures.md)
- [IOUSBHost Enumerations](iousbhost-enumerations.md)
- [IOUSBHost Constants](iousbhost-constants.md)
- [IOUSBHost Functions](iousbhost-functions.md)
- [IOUSBHost Data Types](iousbhost-data-types.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/IOUSBHost)*