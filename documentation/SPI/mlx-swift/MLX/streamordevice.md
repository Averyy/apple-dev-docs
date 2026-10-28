---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/streamordevice"
framework: "mlx-swift/MLX"
---

# StreamOrDevice

**Framework**: mlx-swift/MLX  
**Kind**: struct  
**Role**: Structure

Parameter type for all MLX operations.

## Declaration

```swift
struct StreamOrDevice
```

## Mentions

- [Using Streams](./using-streams.md)

## Overview

Use this to control where operations are evaluated:

```swift
// produced on cpu
let a = MLXRandom.uniform([100, 100], stream: .cpu)

// produced on gpu
let b = MLXRandom.uniform([100, 100], stream: .gpu)
```

If omitted it will use the [`default`](./streamordevice/default.md), which will be [`gpu`](./device/gpu.md) unless set otherwise.

### See Also

- [Using Streams](./using-streams.md)
- [`Stream`](./stream.md)
- [`Device`](./device.md)

## Topics

### Instance Properties
- [var ctx: mlx_stream](./streamordevice/ctx.md)
  Internal context – used with Cmlx calls.
- [var description: String](./streamordevice/description.md)
- [let stream: Stream](./streamordevice/stream.md)
### Type Properties
- [static var cpu: StreamOrDevice](./streamordevice/cpu.md)
  Evaluate on the current CPU stream, [`cpu`](./stream/cpu.md).
- [static var `default`: StreamOrDevice](./streamordevice/default.md)
  The default stream on the default device.
- [static var gpu: StreamOrDevice](./streamordevice/gpu.md)
  Evaluate on the current GPU stream, [`gpu`](./stream/gpu.md).
### Type Methods
- [static func device(Device) -> StreamOrDevice](./streamordevice/device%28_%29.md)
  Evaluate on the given [`Device`](./device.md).
- [static func stream(Stream) -> StreamOrDevice](./streamordevice/stream%28_%29.md)
  Evaluate on the given stream.
### Default Implementations
- [Equatable Implementations](./streamordevice/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Streams and Devices
- [class Device](./device.md)
  Representation of a Device in MLX.
- [enum DeviceType](./devicetype.md)
  Type of device.
- [class Stream](./stream.md)
  A stream of evaluation attached to a particular device.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/streamordevice)*