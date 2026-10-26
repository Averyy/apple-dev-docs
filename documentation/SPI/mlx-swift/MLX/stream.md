---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/stream"
framework: "mlx-swift/MLX"
---

# Stream

**Framework**: mlx-swift/MLX  
**Kind**: class  
**Role**: Class

A stream of evaluation attached to a particular device.

## Declaration

```swift
final class Stream
```

## Mentions

- [Using Streams](./using-streams.md)

#### Overview

Typically this is used via the `stream:` parameter on a method with a [`StreamOrDevice`](./streamordevice.md):

```swift
let a: MLXArray ...
let result = sqrt(a, stream: .gpu)
```

Read more at [Using Streams](./using-streams.md).

#### Implementation Notes

There is a global pair of CPU/GPU streams.  On devices with a GPU (and associated GPU software) the default stream will be a GPU stream.

The default streams can be overridden and scoped to a `Task` using:

```swift
Stream.withNewDefaultStream {
    // the default stream is private to this Task
}
```

Callers can override the default device by passing a device to that method or using [`withDefaultDevice(_:_:)`](./device/withdefaultdevice%28_,_%29-17vjl.md) to override the default device without getting a new (private) default stream.

Also note that the current [`defaultDevice()`](./device/defaultdevice%28%29.md) is owned by [`defaultStream`](./stream/defaultstream.md).

##### See Also

- [Using Streams](./using-streams.md)
- [`StreamOrDevice`](./streamordevice.md)
- [`Device`](./device.md)

## Topics

### Operators
- [static func == (Stream, Stream) -> Bool](./stream/eqeq%28_,_%29.md)
### Initializers
- [init()](./stream/init%28%29.md)
  New stream on the default device.
- [init(Device)](./stream/init%28_%29.md)
  New stream on the given device.
- [init(index: Int32, Device)](./stream/init%28index,_%29.md)
  New stream on the given device.
### Instance Methods
- [func synchronize()](./stream/synchronize%28%29.md)
  Synchronize with the given stream
### Type Properties
- [static var cpu: Stream](./stream/cpu.md)
  the current CPU stream
- [static var defaultStream: Stream](./stream/defaultstream.md)
  the current default stream, see [`StreamOrDevice`](./streamordevice.md) – if no stream is specified, this will be the stream that all operations run on.
- [static var gpu: Stream](./stream/gpu.md)
  the current GPU stream
### Type Methods
- [static func defaultStream(Device) -> Stream](./stream/defaultstream%28_%29-1ktf0.md)
- [static func defaultStream(DeviceType) -> Stream](./stream/defaultstream%28_%29-4sz67.md)
- [static func withNewDefaultStream<R>(device: Device?, () async throws -> R) async rethrows -> R](./stream/withnewdefaultstream%28device,_%29-5bwc3.md)
  Obtain a new CPU and GPU stream scoped to the block and inherited through `Tasks`.
- [static func withNewDefaultStream<R>(device: Device?, () throws -> R) rethrows -> R](./stream/withnewdefaultstream%28device,_%29-7pvrv.md)
  Obtain a new CPU and GPU stream scoped to the block and inherited through `Tasks`.
### Default Implementations
- [CustomStringConvertible Implementations](./stream/customstringconvertible-implementations.md)
- [Equatable Implementations](./stream/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Copyable
- Swift.CustomStringConvertible
- Swift.Equatable
- Swift.Escapable
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Streams and Devices
- [struct StreamOrDevice](./streamordevice.md)
  Parameter type for all MLX operations.
- [class Device](./device.md)
  Representation of a Device in MLX.
- [enum DeviceType](./devicetype.md)
  Type of device.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/stream)*