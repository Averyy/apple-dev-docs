# endpointAddress

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The pipe or stream’s endpoint address.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var endpointAddress: Int { get }
```

```objc
@property (readonly) NSUInteger endpointAddress;
```

## See Also

### Obtaining Device Information
- [var deviceAddress: Int](./deviceaddress.md)
  The device’s bus address.
- [var hostInterface: IOUSBHostInterface](./hostinterface.md)
  The interface for the input/output source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosource/endpointaddress)*