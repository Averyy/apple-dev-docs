# bcdUSB

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The USB version that the device supports.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var bcdUSB: UInt16
```

```c
uint16_t bcdUSB;
```

#### Discussion

Initialize this descriptor to the USB version that the device supports. Acceptable values are 0x0110, 0x0200, 0x0300, 0x0310.

## See Also

### Descriptors
- [var descriptor: IOUSBEndpointDescriptor](./descriptor.md)
  The descriptor for a USB endpoint.
- [var ssCompanionDescriptor: IOUSBSuperSpeedEndpointCompanionDescriptor](./sscompaniondescriptor.md)
  The descriptor for a SuperSpeed USB endpoint companion.
- [var sspCompanionDescriptor: IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](./sspcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosourcedescriptors/bcdusb)*