# deviceAddress

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The device’s bus address.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var deviceAddress: Int { get }
```

```objc
@property (readonly) NSUInteger deviceAddress;
```

## See Also

### Obtaining Device Information
- [var endpointAddress: Int](./endpointaddress.md)
  The pipe or stream’s endpoint address.
- [var hostInterface: IOUSBHostInterface](./hostinterface.md)
  The interface for the input/output source.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosource/deviceaddress)*