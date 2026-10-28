# init(type:selectsMultipleComputeDevices:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a device that you can configure to use multiple compute devices.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)
```

```objc
+ (instancetype) deviceWithType:(MLCDeviceType) type selectsMultipleComputeDevices:(BOOL) selectsMultipleComputeDevices;
```

## Discussion

For the `type` parameter, use [`MLCDeviceType.any`](../mlcdevicetype/any.md) unless you need to control device selection. This ensures that the framework selects the best device to execute the neural network.

## Parameters

- `type`: The device type.
- `selectsMultipleComputeDevices`: A Boolean that indicates whether to select multiple compute devices if the system supports it.

## See Also

### Creating Devices
- [convenience init?(type: MLCDeviceType)](./init%28type%29.md)
  Creates a device of the type you specify.
- [enum MLCDeviceType](../mlcdevicetype.md)
  A device type for execution of a neural network.
- [convenience init?(gpuDevices: [any MTLDevice])](./init%28gpudevices%29-4mj85.md)
  Creates a device using the GPUs you specify.
- [class func cpu() -> Self](./cpu%28%29.md)
  Creates a device that uses the CPU.
- [class func gpu() -> Self?](./gpu%28%29.md)
  Creates a device that uses a GPU, if one exists.
- [class func ane() -> Self?](./ane%28%29.md)
  Creates a device that uses the Apple Neural Engine, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice/init(type:selectsmultiplecomputedevices:))*