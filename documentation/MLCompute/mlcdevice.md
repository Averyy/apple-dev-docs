# MLCDevice

**Framework**: ML Compute  
**Kind**: class

An object that represents the CPU or one or more GPUs the framework uses to execute a neural network.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCDevice
```

## Topics

### Creating Devices
- [convenience init?(type: MLCDeviceType)](mlcdevice/init(type:).md)
  Creates a device of the type you specify.
- [convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)](mlcdevice/init(type:selectsmultiplecomputedevices:).md)
  Creates a device that you can configure to use multiple compute devices.
- [enum MLCDeviceType](mlcdevicetype.md)
  A device type for execution of a neural network.
- [convenience init?(gpuDevices: [any MTLDevice])](mlcdevice/init(gpudevices:)-4mj85.md)
  Creates a device using the GPUs you specify.
- [class func cpu() -> Self](mlcdevice/cpu.md)
  Creates a device that uses the CPU.
- [class func gpu() -> Self?](mlcdevice/gpu.md)
  Creates a device that uses a GPU, if one exists.
- [class func ane() -> Self?](mlcdevice/ane.md)
  Creates a device that uses the Apple Neural Engine, if one exists.
### Inspecting Devices
- [var type: MLCDeviceType](mlcdevice/type.md)
  The type you specify when creating the device.
- [var actualDeviceType: MLCDeviceType](mlcdevice/actualdevicetype.md)
  The active device.
- [var gpuDevices: [any MTLDevice]](mlcdevice/gpudevices.md)
  An array that contains the specific Metal devices you use to execute neural networks.
### Initializers
- [convenience init?(GPUDevices: [any MTLDevice])](mlcdevice/init(gpudevices:)-9w16l.md)

## Relationships

### Inherits From
- [NSObject](../objectivec/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../swift/cvararg.md)
- [CustomDebugStringConvertible](../swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../swift/customstringconvertible.md)
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [NSCopying](../foundation/nscopying.md)
- [NSObjectProtocol](../objectivec/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice)*