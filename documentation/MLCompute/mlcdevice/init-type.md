# init(type:)

**Framework**: ML Compute  
**Kind**: init

Creates a device of the type you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init?(type: MLCDeviceType)
```

#### Discussion

For the `type` parameter, use [`MLCDeviceType.any`](mlcdevicetype/any.md) unless you need to control device selection. This ensures that the framework selects the best device to execute the neural network.

## Parameters

- `type`: The device type.

## See Also

- [convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)](mlcdevice/init(type:selectsmultiplecomputedevices:).md)
  Creates a device that you can configure to use multiple compute devices.
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

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/init(type:))*