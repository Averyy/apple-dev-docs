# init(type:selectsMultipleComputeDevices:)

**Framework**: ML Compute  
**Kind**: init

Creates a device that you can configure to use multiple compute devices.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)
```

#### Discussion

For the `type` parameter, use [`MLCDeviceType.any`](mlcdevicetype/any.md) unless you need to control device selection. This ensures that the framework selects the best device to execute the neural network.

## Parameters

- `type`: The device type.
- `selectsMultipleComputeDevices`: A Boolean that indicates whether to select multiple compute devices if the system supports it.

## See Also

- [convenience init?(type: MLCDeviceType)](mlcdevice/init(type:).md)
  Creates a device of the type you specify.
- [enum MLCDeviceType](mlcdevicetype.md)
  A device type for execution of a neural network.
- [convenience init?(gpuDevices: [any MTLDevice])](mlcdevice/init(gpudevices:).md)
  Creates a device using the GPUs you specify.
- [class func cpu() -> Self](mlcdevice/cpu.md)
  Creates a device that uses the CPU.
- [class func gpu() -> Self?](mlcdevice/gpu.md)
  Creates a device that uses a GPU, if one exists.
- [class func ane() -> Self?](mlcdevice/ane.md)
  Creates a device that uses the Apple Neural Engine, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/init(type:selectsmultiplecomputedevices:))*