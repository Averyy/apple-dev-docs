# IOUSBHostIOSource

**Framework**: IOUSBHost  
**Kind**: class  
**Role**: Class

This class provides basic functionality for deriving pipe and stream classes.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
class IOUSBHostIOSource
```

```objc
@interface IOUSBHostIOSource : NSObject
```

#### Overview

Don’t create objects of this class or use this class as a subclass. Instead, use [`copyPipe(withAddress:)`](./iousbhostinterface/copypipe%28withaddress%29.md) and [`copyStream(withStreamID:)`](./iousbhostpipe/copystream%28withstreamid%29.md) when creating an [`IOUSBHostIOSource`](./iousbhostiosource.md).

## Topics

### Obtaining Device Information
- [var deviceAddress: Int](./iousbhostiosource/deviceaddress.md)
  The device’s bus address.
- [var endpointAddress: Int](./iousbhostiosource/endpointaddress.md)
  The pipe or stream’s endpoint address.
- [var hostInterface: IOUSBHostInterface](./iousbhostiosource/hostinterface.md)
  The interface for the input/output source.
### Related Documentation
- [class IOUSBHostPipe](./iousbhostpipe.md)
  The class that sends control, bulk, interrupt, and isochronous input/output requests for function drivers, and manages stream capabilities.
- [class IOUSBHostStream](./iousbhoststream.md)
  The class responsible for sending stream data for function drivers.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Inherited By
- [IOUSBHostPipe](./iousbhostpipe.md)
- [IOUSBHostStream](./iousbhoststream.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Base Classes
- [class IOUSBHostObject](./iousbhostobject.md)
  This class provides basic functionality for sending device requests and retrieving descriptors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosource)*