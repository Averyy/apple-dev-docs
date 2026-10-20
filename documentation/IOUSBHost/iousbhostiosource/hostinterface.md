# hostInterface

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The interface for the input/output source.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var hostInterface: IOUSBHostInterface { get }
```

```objc
@property (readonly) IOUSBHostInterface * hostInterface;
```

## See Also

### Obtaining Device Information
- [var deviceAddress: Int](./deviceaddress.md)
  The device’s bus address.
- [var endpointAddress: Int](./endpointaddress.md)
  The pipe or stream’s endpoint address.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosource/hostinterface)*