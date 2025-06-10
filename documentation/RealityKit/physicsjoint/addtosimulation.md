# addToSimulation()

**Framework**: RealityKit  
**Kind**: method

Adds this joint to the simulation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 18.0+
- macOS 15.0+
- tvOS 26.0+ (Beta)
- visionOS 2.0+

## Declaration

```swift
@discardableResult
@MainActor func addToSimulation() throws -> Entity
```

#### Return Value

The entity that owns the [`PhysicsJointsComponent`](physicsjointscomponent.md), which this joint has been added to.

#### Discussion

This method looks for an ancestral [`Entity`](entity.md) that has [`PhysicsJointsComponent`](physicsjointscomponent.md) by traversing upwards from the entity referenced by [`pin0`](physicsjoint/pin0.md).

If found, it adds the joint to that ancestor’s [`PhysicsJointsComponent`](physicsjointscomponent.md).

The traversal stops when reaching an [`Entity`](entity.md) with [`PhysicsSimulationComponent`](physicssimulationcomponent.md), or when it cannot traverse up anymore. In the former case it adds the joint to [`joints`](physicsjointscomponent/joints.md). In the latter case it adds [`PhysicsJointsComponent`](physicsjointscomponent.md) to the first [`Entity`](entity.md) referenced by the joint, and adds the joint to the newly created [`PhysicsJointsComponent`](physicsjointscomponent.md).

> **Note**: When the joint contains invalid data.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/physicsjoint/addtosimulation())*