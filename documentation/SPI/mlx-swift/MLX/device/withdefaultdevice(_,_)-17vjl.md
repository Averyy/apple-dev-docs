---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device/withdefaultdevice(_:_:)-17vjl"
framework: "mlx-swift/MLX"
---

# withDefaultDevice(_:_:)

**Framework**: mlx-swift/MLX  
**Kind**: method  
**Role**: Type Method

Use a device scoped to a Task.

## Declaration

```swift
static func withDefaultDevice<R>(_ device: Device, _ body: () async throws -> R) async rethrows -> R
```

## Mentions

- [Using Streams](../using-streams.md)

## Discussion

This can be used to set the default device to e.g. the CPU:

```swift
Device.withDefaultDevice(.cpu) {
    // default device is cpu inside this scope/task
}
```

If a GPU device is given and it does not match the current GPU it will override the default device and provide a new stream:

```swift
Device.withDefaultDevice(.init(.gpu, index: 3)) {
    // if the enclosing GPU was index 0, this will have
    // both a new default device and a new stream
}
```

See also [`withNewDefaultStream(device:_:)`](../stream/withnewdefaultstream%28device,_%29-5bwc3.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlx/device/withdefaultdevice(_:_:)-17vjl)*