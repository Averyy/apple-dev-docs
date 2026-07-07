# spawn(elements:in:using:)

**Framework**: Compute Graph  
**Kind**: method

Spawns new elements into the simulation with the given initial parameters.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- Reality Composer Pro ?+

## Declaration

```swift
final func spawn(elements: borrowing [ElementSpawnParameters], in systemID: Int?, using encoder: any MTLComputeCommandEncoder)
```

#### Discussion

Each entry in `elements` produces one new element. The initialization stage of the simulation graph runs on the newly spawned elements before they participate in subsequent simulation steps, and may read or overwrite the values supplied here.

## Parameters

- `elements`: The initial state for each element to spawn.
- `systemID`: The index of the particle simulation stage to spawn into, or `nil` to spawn into all simulations.
- `encoder`: The compute command encoder to encode the spawn operation with.


---

*[View on Apple Developer](https://developer.apple.com/documentation/computegraph/computegraphsimulation/spawn(elements:in:using:))*