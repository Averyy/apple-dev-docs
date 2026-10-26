---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device"
framework: "mlx-swift/MLX"
---

# Device

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

Representation of a Device in MLX.

## Declaration

```swift
final class Device
```

#### Overview

This is typically used with [`withDefaultDevice(_:_:)`](./device/withdefaultdevice%28_,_%29-17vjl.md) or [`withNewDefaultStream(device:_:)`](./stream/withnewdefaultstream%28device,_%29-5bwc3.md).

```swift
Device.withDefaultDevice(.cpu) {
    // default device is cpu inside this scope/task
}

Stream.withNewDefaultStream(device: .cpu) {
    // default device is cpu inside this scope/task AND there
    // is a new Stream scoped to the work
}
```

Implementation: [`Stream`](./stream.md) hold the current device as a Task local variable.

##### See Also

- [Using Streams](./using-streams.md)
- [`StreamOrDevice`](./streamordevice.md)
- [`Stream`](./stream.md)

## Topics

### Operators
- [static func == (Device, Device) -> Bool](./device/eqeq%28_,_%29.md)
  Compare two [`Device`](./device.md) for equality
### Initializers
- [convenience init()](./device/init%28%29.md)
- [init(DeviceType, index: Int32)](./device/init%28_,index%29.md)
  Initialize a new `Device` with a type and optional index.
### Instance Properties
- [var deviceType: DeviceType](./device/devicetype.md)
  The [`DeviceType`](./devicetype.md) for the device.
### Instance Methods
- [func hash(into: inout Hasher)](./device/hash%28into%29.md)
### Type Properties
- [static var cpu: Device](./device/cpu.md)
  Current CPU device.
- [static var gpu: Device](./device/gpu.md)
  Current GPU device.
### Type Methods
- [static func defaultDevice() -> Device](./device/defaultdevice%28%29.md)
  Return the current default device.
- [static func setDefault(device: Device?)](./device/setdefault%28device%29.md)
  Set the default device globally.  Use the scoped version, [`withDefaultDevice(_:_:)`](./device/withdefaultdevice%28_,_%29-17vjl.md) – this is only usable before any mlx resources are created.
- [static func withDefaultDevice<R>(Device, () async throws -> R) async rethrows -> R](./device/withdefaultdevice%28_,_%29-17vjl.md)
  Use a device scoped to a Task.
- [static func withDefaultDevice<R>(Device, () throws -> R) rethrows -> R](./device/withdefaultdevice%28_,_%29-8auhy.md)
  Use a device scoped to a Task.
### Default Implementations
- [CustomStringConvertible Implementations](./device/customstringconvertible-implementations.md)
- [Equatable Implementations](./device/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Escapable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Streams and Devices
- [struct StreamOrDevice](./streamordevice.md)
  Parameter type for all MLX operations.
- [enum DeviceType](./devicetype.md)
  Type of device.
- [class Stream](./stream.md)
  A stream of evaluation attached to a particular device.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device)*