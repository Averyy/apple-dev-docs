# IOUSBHostIOSourceDescriptors

**Framework**: IOUSBHost  
**Kind**: struct

The descriptors for a single endpoint.

**Availability**:
- Mac Catalyst 14.0+
- macOS 10.15+

## Declaration

```swift
struct IOUSBHostIOSourceDescriptors
```

#### Overview

The [`IOUSBHostIOSourceDescriptors`](iousbhostiosourcedescriptors.md) structure initializes and adjusts pipes in the system.

## Topics

### Descriptors
- [var bcdUSB: UInt16](iousbhostiosourcedescriptors/bcdusb.md)
  The USB version that the device supports.
- [var descriptor: IOUSBEndpointDescriptor](iousbhostiosourcedescriptors/descriptor.md)
  The descriptor for a USB endpoint.
- [var ssCompanionDescriptor: IOUSBSuperSpeedEndpointCompanionDescriptor](iousbhostiosourcedescriptors/sscompaniondescriptor.md)
  The descriptor for a SuperSpeed USB endpoint companion.
- [var sspCompanionDescriptor: IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor](iousbhostiosourcedescriptors/sspcompaniondescriptor.md)
  The descriptor for a SuperSpeedPlus isochronous USB endpoint companion.
### Initializing the Structure
- [init()](iousbhostiosourcedescriptors/init.md)
  Creates a new source descriptor structure.
- [init(bcdUSB: UInt16, descriptor: IOUSBEndpointDescriptor, ssCompanionDescriptor: IOUSBSuperSpeedEndpointCompanionDescriptor, sspCompanionDescriptor: IOUSBSuperSpeedPlusIsochronousEndpointCompanionDescriptor)](iousbhostiosourcedescriptors/init(bcdusb:descriptor:sscompaniondescriptor:sspcompaniondescriptor:).md)
  Creates a new source descriptor structure.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func adjust(with: UnsafePointer<IOUSBHostIOSourceDescriptors>) throws](iousbhostpipe/adjust(with:).md)
  Adjusts the behavior of periodic endpoints to consume a different amount of bus bandwidth.
- [var descriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](iousbhostpipe/descriptors.md)
  A property that retrieves the current endpoint descriptors controlling the endpoint.
- [var originalDescriptors: UnsafePointer<IOUSBHostIOSourceDescriptors>](iousbhostpipe/originaldescriptors.md)
  A property that retrieves the original endpoint descriptors from the pipe at the point of creation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/iousbhost/iousbhostiosourcedescriptors)*