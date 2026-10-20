# IOUSBHostDevice

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

The class that claims and configures devices, retrieves descriptors, and sends device requests.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostDevice
```

```objc
@interface IOUSBHostDevice : IOUSBHostObject
```

#### Overview

This class enables management of the device state, including sending control requests to the default endpoint 0, configuring the device, and resetting the device. The interest handler also allows monitoring of the device state. The client creates the class and initializes it with [`initWithIOService:options:queue:error:interestHandler:`](./iousbhostobject/initwithioservice_options_queue_error_interesthandler_.md).

> **Note**:  To prevent other drivers from changing the state of your device, maintain an [`IOUSBHostDevice`](../kernel/iousbhostdevice.md) object until you no longer need control over the device.

## Topics

### Retrieving Device Descriptors
- [var configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>?](./iousbhostdevice/configurationdescriptor.md)
  The currently selected configuration descriptor.
### Resetting the Device
- [func reset() throws](./iousbhostdevice/reset%28%29.md)
  Terminates the device and attempts to re-enumerate it.

## Relationships

### Inherits From
- [IOUSBHostObject](./iousbhostobject.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostdevice)*