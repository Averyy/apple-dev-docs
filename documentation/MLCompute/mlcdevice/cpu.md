# cpu()

**Framework**: ML Compute  
**Kind**: method

Creates a device that uses the CPU.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class func cpu() -> Self
```

#### Return Value

A device that uses the CPU.

## See Also

- [convenience init?(type: MLCDeviceType)](mlcdevice/init(type:).md)
  Creates a device of the type you specify.
- [convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)](mlcdevice/init(type:selectsmultiplecomputedevices:).md)
  Creates a device that you can configure to use multiple compute devices.
- [enum MLCDeviceType](mlcdevicetype.md)
  A device type for execution of a neural network.
- [convenience init?(gpuDevices: [any MTLDevice])](mlcdevice/init(gpudevices:).md)
  Creates a device using the GPUs you specify.
- [class func gpu() -> Self?](mlcdevice/gpu.md)
  Creates a device that uses a GPU, if one exists.
- [class func ane() -> Self?](mlcdevice/ane.md)
  Creates a device that uses the Apple Neural Engine, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/cpu())*