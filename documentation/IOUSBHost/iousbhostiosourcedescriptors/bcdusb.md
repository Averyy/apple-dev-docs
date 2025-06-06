# bcdUSB

**Framework**: IOUSBHost  
**Kind**: property

The USB version that the device supports.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var bcdUSB: UInt16
```

#### Discussion

Initialize this descriptor to the USB version that the device supports. Acceptable values are 0x0110, 0x0200, 0x0300, 0x0310.

## See Also

- [var descriptor: IOUSBEndpointDescriptor](iousbhostiosourcedescriptors/descriptor.md)
  The descriptor for a USB endpoint.
- [var ssCompanionDescriptor: IOUSBSuperSpeedEndpointCompanionDescriptor](iousbhostiosourcedescriptors/sscompaniondescriptor.md)
  The descriptor for a SuperSpeed USB endpoint companion.
- [var sspCompanionDescriptor: IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](iousbhostiosourcedescriptors/sspcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosourcedescriptors/bcdusb)*