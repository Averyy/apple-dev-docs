# addForce(_:at:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Applies a force to the physics body at the specified position.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func addForce(_ force: SIMD3<Float>, at position: SIMD3<Float>, relativeTo referenceEntity: Entity?)
```

#### Discussion

The physics simulator applies the added force until the end of the frame interval. To continue exerting the force after that time, add the force again with another call to the method. Handle the [`SceneEvents.Update`](sceneevents/update.md) event to receive an indication of when the frame interval ends. For an app that renders at 60 frames per second (fps), this event occurs about once per 16 milliseconds.

## Parameters

- `force`: A force in newtons.
- `position`: The position at which to apply the force.
- `referenceEntity`: The reference entity that defines the coordinate   space in which   and   are defined.

## See Also

- [func addForce(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/addforce(_:relativeto:).md)
  Applies a force to the physics body at its center of mass.
- [func addTorque(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/addtorque(_:relativeto:).md)
  Applies a torque to the physics body at its center of mass.
- [func clearForcesAndTorques()](hasphysicsbody/clearforcesandtorques.md)
  Clears all forces previously added to the physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsbody/addforce(_:at:relativeto:))*