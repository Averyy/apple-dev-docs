# ssCompanionDescriptor

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The descriptor for a SuperSpeed USB endpoint companion.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var ssCompanionDescriptor: IOUSBSuperSpeedEndpointCompanionDescriptor
```

```c
IOUSBSuperSpeedEndpointCompanionDescriptor ssCompanionDescriptor;
```

#### Discussion

This descriptor may be necessary for `bcdUSB` versions 0x0300 and greater, depending on device operating speed and values set in the descriptors. See USB 3.2, 9.5 for more information.

## See Also

### Descriptors
- [var bcdUSB: UInt16](./bcdusb.md)
  The USB version that the device supports.
- [var descriptor: IOUSBEndpointDescriptor](./descriptor.md)
  The descriptor for a USB endpoint.
- [var sspCompanionDescriptor: IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](./sspcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosourcedescriptors/sscompaniondescriptor)*