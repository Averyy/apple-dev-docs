# resetPhysicsTransform(_:recursive:)

**Framework**: RealityKit  
**Kind**: method

Resets the position and velocities of the simulated physics body.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+
- Unknown ?+ - Deprecated

## Declaration

```swift
@MainActor
@preconcurrency func resetPhysicsTransform(_ transform: Transform, recursive: Bool = true)
```

#### Discussion

Call this method to change the transform applied to a body by physics simulation. This only matters for dynamic rigid bodies, with a [`mode`](physicsbodycomponent/mode.md) of [`PhysicsBodyMode.dynamic`](physicsbodymode/dynamic.md). This is the only kind of body that’s affected by physics simulations. For all others, modify the entity’s [`transform`](hastransform/transform.md) property directly.

Conversely, directly modifying the transform of a dynamic body has no effect because the physics simulation overwrites it on every frame.

## Parameters

- `transform`: The new transform to inject into the dynamic physics   simulation of the entity.
- `recursive`: Apply the reset to child entities.

## See Also

- [var physicsBody: PhysicsBodyComponent?](modelentity/physicsbody.md)
  A component that is used for physics simulations of the model entity in accordance with the laws of Newtonian mechanics.
- [var physicsMotion: PhysicsMotionComponent?](modelentity/physicsmotion.md)
  The physics motion component used by physics simulations of the model entity.
- [func addForce(SIMD3<Float>, relativeTo: Entity?)](modelentity/addforce(_:relativeto:).md)
  Applies a force to the physics body at its center of mass.
- [func addForce(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](modelentity/addforce(_:at:relativeto:).md)
  Applies a force to the physics body at the specified position.
- [func addTorque(SIMD3<Float>, relativeTo: Entity?)](modelentity/addtorque(_:relativeto:).md)
  Applies a torque to the physics body at its center of mass.
- [func clearForcesAndTorques()](modelentity/clearforcesandtorques.md)
  Clears all forces previously added to the physics body.
- [func applyLinearImpulse(SIMD3<Float>, relativeTo: Entity?)](modelentity/applylinearimpulse(_:relativeto:).md)
  Applies an impulse to the physics body at its center of mass.
- [func applyAngularImpulse(SIMD3<Float>, relativeTo: Entity?)](modelentity/applyangularimpulse(_:relativeto:).md)
  Applies an angular (torque) impulse to the physics body at its center of mass.
- [func applyImpulse(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](modelentity/applyimpulse(_:at:relativeto:).md)
  Applies an impulse to the physics body at the specified position.
- [func resetPhysicsTransform(recursive: Bool)](modelentity/resetphysicstransform(recursive:).md)
  Resets the position, orientation, and velocities of the simulated physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelentity/resetphysicstransform(_:recursive:))*