# ane()

**Framework**: ML Compute  
**Kind**: method  
**Role**: Type Method

Creates a device that uses the Apple Neural Engine, if one exists.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
class func ane() -> Self?
```

```objc
+ (instancetype) aneDevice;
```

## Return Value

A device that uses the Apple Neural Engine, or `nil` if none exists.

## Discussion

When you select this device, the system uses the Apple Neural Engine to execute valid layers. Layers that can’t execute on the Apple Neural Engine run on the `CPU` or `GPU`. The system doesn’t select the Apple Neural Engine if you use [`MLCDeviceType.any`](../mlcdevicetype/any.md).

This device applies to inference graphs only. It doesn’t work with a training graph or inference graph that shares layers with a training graph.

## See Also

### Creating Devices
- [convenience init?(type: MLCDeviceType)](./init%28type%29.md)
  Creates a device of the type you specify.
- [convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)](./init%28type,selectsmultiplecomputedevices%29.md)
  Creates a device that you can configure to use multiple compute devices.
- [enum MLCDeviceType](../mlcdevicetype.md)
  A device type for execution of a neural network.
- [convenience init?(gpuDevices: [any MTLDevice])](./init%28gpudevices%29-4mj85.md)
  Creates a device using the GPUs you specify.
- [class func cpu() -> Self](./cpu%28%29.md)
  Creates a device that uses the CPU.
- [class func gpu() -> Self?](./gpu%28%29.md)
  Creates a device that uses a GPU, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/ane())*