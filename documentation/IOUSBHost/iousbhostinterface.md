# IOUSBHostInterface

**Framework**: IOUSBHost  
**Kind**: class

The class for accessing USB-related services.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostInterface
```

#### Overview

Use this class to create pipes, retrieve descriptors, send device requests, and enable power savings. Create an instance of the class with [`initWithIOService:options:queue:error:interestHandler:`](iousbhostobject/initwithioservice:options:queue:error:interesthandler:.md).

## Topics

### Retrieving Function Descriptors
- [var configurationDescriptor: UnsafePointer<IOUSBConfigurationDescriptor>](iousbhostinterface/configurationdescriptor.md)
  The configuration descriptor for the interface.
- [var interfaceDescriptor: UnsafePointer<IOUSBInterfaceDescriptor>](iousbhostinterface/interfacedescriptor.md)
  The descriptor for the interface.
### Managing Pipes
- [func selectAlternateSetting(Int) throws](iousbhostinterface/selectalternatesetting(_:).md)
  Selects an alternative setting for the interface.
- [func copyPipe(withAddress: Int) throws -> IOUSBHostPipe](iousbhostinterface/copypipe(withaddress:).md)
  Copies a pipe for a specific endpoint address.
### Enabling Power Savings
- [var idleTimeout: TimeInterval](iousbhostinterface/idletimeout.md)
  The current idle suspend timeout.
- [func setIdleTimeout(TimeInterval) throws](iousbhostinterface/setidletimeout(_:).md)
  Sets the desired idle suspend timeout for the interface.

## Relationships

### Inherits From
- [IOUSBHostObject](iousbhostobject.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class IOUSBHostPipe](iousbhostpipe.md)
  The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.
- [class IOUSBHostStream](iousbhoststream.md)
  The class responsible for sending stream data for function drivers.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostinterface)*