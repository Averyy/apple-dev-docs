# applyLinearImpulse(_:relativeTo:)

**Framework**: RealityKit  
**Kind**: method

Applies an impulse to the physics body at its center of mass.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency func applyLinearImpulse(_ impulse: SIMD3<Float>, relativeTo referenceEntity: Entity?)
```

## Parameters

- `impulse`: An impulse in newton seconds.
- `referenceEntity`: The reference entity that defines the coordinate   space in which   is defined.

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
- [func applyAngularImpulse(SIMD3<Float>, relativeTo: Entity?)](modelentity/applyangularimpulse(_:relativeto:).md)
  Applies an angular (torque) impulse to the physics body at its center of mass.
- [func applyImpulse(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](modelentity/applyimpulse(_:at:relativeto:).md)
  Applies an impulse to the physics body at the specified position.
- [func resetPhysicsTransform(recursive: Bool)](modelentity/resetphysicstransform(recursive:).md)
  Resets the position, orientation, and velocities of the simulated physics body.
- [func resetPhysicsTransform(Transform, recursive: Bool)](modelentity/resetphysicstransform(_:recursive:).md)
  Resets the position and velocities of the simulated physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelentity/applylinearimpulse(_:relativeto:))*