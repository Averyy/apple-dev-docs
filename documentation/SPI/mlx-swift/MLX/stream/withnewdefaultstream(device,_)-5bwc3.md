---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/stream/withnewdefaultstream(device:_:)-5bwc3"
framework: "mlx-swift/MLX"
---

# withNewDefaultStream(device:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Obtain a new CPU and GPU stream scoped to the block and inherited through `Tasks`.

## Declaration

```swift
static func withNewDefaultStream<R>(device: Device? = nil, _ body: () async throws -> R) async rethrows -> R
```

## Mentions

- [Using Streams](../using-streams.md)

## Discussion

For example you can get a new stream on the current device:

```swift
Stream.withNewDefaultStream {
    // A new Stream on the default Device scoped to the block and Task
}
```

Or a new stream on a different device (it will become the default device, scoped to the block and Task):

```swift
Stream.withNewDefaultStream(device: .cpu) {
    // A new Stream on the cpu Device scoped to the block and Task.
    // The cpu is now the default device.
}
```

These calls can be nested arbitrarily.

See also [`withDefaultDevice(_:_:)`](../device/withdefaultdevice%28_,_%29-17vjl.md) which can change the default device without creating new scoped Streams.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/stream/withnewdefaultstream(device:_:)-5bwc3)*