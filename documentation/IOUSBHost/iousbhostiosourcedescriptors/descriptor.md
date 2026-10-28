# descriptor

**Framework**: IOUSBHost  
**Kind**: property  
**Role**: Instance Property

The descriptor for a USB endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
var descriptor: IOUSBEndpointDescriptor
```

```c
IOUSBEndpointDescriptor descriptor;
```

## Discussion

Initialize this descriptor with a valid [`IOUSBEndpointDescriptor`](../../iokit/iousbendpointdescriptor.md). See USB 3.2, 9.6.6.

## See Also

### Descriptors
- [var bcdUSB: UInt16](./bcdusb.md)
  The USB version that the device supports.
- [var ssCompanionDescriptor: IOUSBSuperSpeedEndpointCompanionDescriptor](./sscompaniondescriptor.md)
  The descriptor for a SuperSpeed USB endpoint companion.
- [var sspCompanionDescriptor: IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](./sspcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosourcedescriptors/descriptor)*