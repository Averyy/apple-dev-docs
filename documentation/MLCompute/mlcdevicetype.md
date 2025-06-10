# MLCDeviceType

**Framework**: ML Compute  
**Kind**: enum

A device type for execution of a neural network.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
enum MLCDeviceType
```

## Topics

### Device Types
- [MLCDeviceType.any](mlcdevicetype/any.md)
  A device type that represents either the CPU or GPU.
- [MLCDeviceType.cpu](mlcdevicetype/cpu.md)
  A device type that represents the CPU.
- [MLCDeviceType.gpu](mlcdevicetype/gpu.md)
  A device type that represents the GPU.
- [MLCDeviceType.ane](mlcdevicetype/ane.md)
  A device type that represents the Apple Neural Engine.
### Initializers
- [init?(rawValue: Int32)](mlcdevicetype/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [convenience init?(type: MLCDeviceType)](mlcdevice/init(type:).md)
  Creates a device of the type you specify.
- [convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)](mlcdevice/init(type:selectsmultiplecomputedevices:).md)
  Creates a device that you can configure to use multiple compute devices.
- [convenience init?(gpuDevices: [any MTLDevice])](mlcdevice/init(gpudevices:).md)
  Creates a device using the GPUs you specify.
- [class func cpu() -> Self](mlcdevice/cpu.md)
  Creates a device that uses the CPU.
- [class func gpu() -> Self?](mlcdevice/gpu.md)
  Creates a device that uses a GPU, if one exists.
- [class func ane() -> Self?](mlcdevice/ane.md)
  Creates a device that uses the Apple Neural Engine, if one exists.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevicetype)*