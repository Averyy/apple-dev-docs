# IOUSBHostInterface

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

The class for accessing USB-related services.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostInterface
```

```objc
@interface IOUSBHostInterface : IOUSBHostObject
```

## Overview

Use this class to create pipes, retrieve descriptors, send device requests, and enable power savings. Create an instance of the class with [`initWithIOService:options:queue:error:interestHandler:`](./iousbhostobject/initwithioservice_options_queue_error_interesthandler_.md).

## Topics

### Retrieving Function Descriptors
- [var configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>](./iousbhostinterface/configurationdescriptor.md)
  The configuration descriptor for the interface.
- [var interfaceDescriptor: UnsafePointer<IOUSBInterfaceDescriptor>](./iousbhostinterface/interfacedescriptor.md)
  The descriptor for the interface.
### Managing Pipes
- [func selectAlternateSetting(Int) throws](./iousbhostinterface/selectalternatesetting%28_%29.md)
  Selects an alternative setting for the interface.
- [func copyPipe(withAddress: Int) throws -> IOUSBHostPipe](./iousbhostinterface/copypipe%28withaddress%29.md)
  Copies a pipe for a specific endpoint address.
### Enabling Power Savings
- [var idleTimeout: TimeInterval](./iousbhostinterface/idletimeout.md)
  The current idle suspend timeout.
- [func setIdleTimeout(TimeInterval) throws](./iousbhostinterface/setidletimeout%28_%29.md)
  Sets the desired idle suspend timeout for the interface.
### Finding Interfaces
- [+ createMatchingDictionaryWithVendorID:productID:bcdDevice:interfaceNumber:configurationValue:interfaceClass:interfaceSubclass:interfaceProtocol:speed:productIDArray:](./iousbhostinterface/creatematchingdictionarywithvendorid_productid_bcddevice_interfacenumber_configurationvalue_interfaceclass_interfacesubclass_interfaceprotocol_speed_productidarray_.md)
  Creates a matching dictionary to find a USB interface.
### Instance Methods
- [- initWithIOService:options:queue:error:interestHandler:](./iousbhostinterface/initwithioservice_options_queue_error_interesthandler_.md)

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

## See Also

### Function Drivers
- [class IOUSBHostPipe](./iousbhostpipe.md)
  The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.
- [class IOUSBHostStream](./iousbhoststream.md)
  The class responsible for sending stream data for function drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface)*