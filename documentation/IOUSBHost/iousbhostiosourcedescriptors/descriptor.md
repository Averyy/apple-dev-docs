# descriptor

**Framework**: IOUSBHost  
**Kind**: property

The descriptor for a USB endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var descriptor: IOUSBEndpointDescriptor
```

#### Discussion

Initialize this descriptor with a valid [`IOUSBEndpointDescriptor`](https://developer.apple.com/documentation/iokit/iousbendpointdescriptor). See USB 3.2, 9.6.6.

## See Also

- [var bcdUSB: UInt16](iousbhostiosourcedescriptors/bcdusb.md)
  The USB version that the device supports.
- [var ssCompanionDescriptor: IOUSBSuperSpeedEndpointCompanionDescriptor](iousbhostiosourcedescriptors/sscompaniondescriptor.md)
  The descriptor for a SuperSpeed USB endpoint companion.
- [var sspCompanionDescriptor: IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](iousbhostiosourcedescriptors/sspcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosourcedescriptors/descriptor)*