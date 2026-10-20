# MLCDeviceType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

A device type for execution of a neural network.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCDeviceType
```

```c
enum MLCDeviceType : int32_t;
```

## Topics

### Device Types
- [MLCDeviceType.any](./mlcdevicetype/any.md)
  A device type that represents either the CPU or GPU.
- [MLCDeviceType.cpu](./mlcdevicetype/cpu.md)
  A device type that represents the CPU.
- [MLCDeviceType.gpu](./mlcdevicetype/gpu.md)
  A device type that represents the GPU.
- [MLCDeviceType.ane](./mlcdevicetype/ane.md)
  A device type that represents the Apple Neural Engine.
### Initializers
- [init?(rawValue: Int32)](./mlcdevicetype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Devices
- [convenience init?(type: MLCDeviceType)](./mlcdevice/init%28type%29.md)
  Creates a device of the type you specify.
- [convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)](./mlcdevice/init%28type,selectsmultiplecomputedevices%29.md)
  Creates a device that you can configure to use multiple compute devices.
- [convenience init?(gpuDevices: [any MTLDevice])](./mlcdevice/init%28gpudevices%29-4mj85.md)
  Creates a device using the GPUs you specify.
- [class func cpu() -> Self](./mlcdevice/cpu%28%29.md)
  Creates a device that uses the CPU.
- [class func gpu() -> Self?](./mlcdevice/gpu%28%29.md)
  Creates a device that uses a GPU, if one exists.
- [class func ane() -> Self?](./mlcdevice/ane%28%29.md)
  Creates a device that uses the Apple Neural Engine, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevicetype)*