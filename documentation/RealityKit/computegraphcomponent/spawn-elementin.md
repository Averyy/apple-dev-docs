# spawn(element:in:)

**Framework**: RealityKit  
**Kind**: method

Spawns a new element in the particle simulation.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- macOS 27.0+ (Beta)
- tvOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)

## Declaration

```swift
mutating func spawn(element: ElementSpawnParameters, in system: ComputeNodeGraph.NodeID? = nil)
```

#### Discussion

This method queues an element to be spawned during the next simulation update. The spawning is deferred and batched for performance reasons.

> **Note**: The actual spawning occurs during the simulation update cycle.

## Parameters

- `element`: The spawn parameters defining the properties of the element to create
- `system`: The ID of the specific system to spawn the element in. When `nil`, all systems will be asked to spawn the same element.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/computegraphcomponent/spawn(element:in:))*