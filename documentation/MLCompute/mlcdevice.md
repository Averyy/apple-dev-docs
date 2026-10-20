# MLCDevice

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

An object that represents the CPU or one or more GPUs the framework uses to execute a neural network.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCDevice
```

```objc
@interface MLCDevice : NSObject
```

## Topics

### Creating Devices
- [convenience init?(type: MLCDeviceType)](./mlcdevice/init%28type%29.md)
  Creates a device of the type you specify.
- [convenience init?(type: MLCDeviceType, selectsMultipleComputeDevices: Bool)](./mlcdevice/init%28type,selectsmultiplecomputedevices%29.md)
  Creates a device that you can configure to use multiple compute devices.
- [enum MLCDeviceType](./mlcdevicetype.md)
  A device type for execution of a neural network.
- [convenience init?(gpuDevices: [any MTLDevice])](./mlcdevice/init%28gpudevices%29-4mj85.md)
  Creates a device using the GPUs you specify.
- [class func cpu() -> Self](./mlcdevice/cpu%28%29.md)
  Creates a device that uses the CPU.
- [class func gpu() -> Self?](./mlcdevice/gpu%28%29.md)
  Creates a device that uses a GPU, if one exists.
- [class func ane() -> Self?](./mlcdevice/ane%28%29.md)
  Creates a device that uses the Apple Neural Engine, if one exists.
### Inspecting Devices
- [var type: MLCDeviceType](./mlcdevice/type.md)
  The type you specify when creating the device.
- [var actualDeviceType: MLCDeviceType](./mlcdevice/actualdevicetype.md)
  The active device.
- [var gpuDevices: [any MTLDevice]](./mlcdevice/gpudevices.md)
  An array that contains the specific Metal devices you use to execute neural networks.
### Initializers
- [convenience init?(GPUDevices: [any MTLDevice])](./mlcdevice/init%28gpudevices%29-9w16l.md)

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcdevice)*