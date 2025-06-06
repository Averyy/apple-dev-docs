# IOUSBHostIOSource

**Framework**: IOUSBHost  
**Kind**: class

This class provides basic functionality for deriving pipe and stream classes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostIOSource
```

#### Overview

Don’t create objects of this class or use this class as a subclass. Instead, use [`copyPipe(withAddress:)`](iousbhostinterface/copypipe(withaddress:).md) and [`copyStream(withStreamID:)`](iousbhostpipe/copystream(withstreamid:).md) when creating an [`IOUSBHostIOSource`](iousbhostiosource.md).

## Topics

### Obtaining Device Information
- [var deviceAddress: Int](iousbhostiosource/deviceaddress.md)
  The device’s bus address.
- [var endpointAddress: Int](iousbhostiosource/endpointaddress.md)
  The pipe or stream’s endpoint address.
- [var hostInterface: IOUSBHostInterface](iousbhostiosource/hostinterface.md)
  The interface for the input/output source.
### Related Documentation
- [class IOUSBHostPipe](iousbhostpipe.md)
  The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.
- [class IOUSBHostStream](iousbhoststream.md)
  The class responsible for sending stream data for function drivers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Inherited By
- [IOUSBHostPipe](iousbhostpipe.md)
- [IOUSBHostStream](iousbhoststream.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class IOUSBHostObject](iousbhostobject.md)
  This class provides basic functionality for sending device requests and retrieving descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosource)*