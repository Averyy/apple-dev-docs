# HasPhysicsBody

**Framework**: RealityKit  
**Kind**: protocol

An interface that enables physics simulations based on the rules of Newtonian mechanics.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+ (Beta)
- visionOS ?+

## Declaration

```swift
@MainActor
@preconcurrency protocol HasPhysicsBody : HasCollision
```

## Topics

### Getting the component
- [var physicsBody: PhysicsBodyComponent?](hasphysicsbody/physicsbody.md)
  A component that is used for physics simulations of the model entity in accordance with the laws of Newtonian mechanics.
### Adding and clearing forces
- [func addForce(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/addforce(_:relativeto:).md)
  Applies a force to the physics body at its center of mass.
- [func addForce(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/addforce(_:at:relativeto:).md)
  Applies a force to the physics body at the specified position.
- [func addTorque(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/addtorque(_:relativeto:).md)
  Applies a torque to the physics body at its center of mass.
- [func clearForcesAndTorques()](hasphysicsbody/clearforcesandtorques.md)
  Clears all forces previously added to the physics body.
### Applying impulses
- [func applyLinearImpulse(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/applylinearimpulse(_:relativeto:).md)
  Applies an impulse to the physics body at its center of mass.
- [func applyAngularImpulse(SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/applyangularimpulse(_:relativeto:).md)
  Applies an angular (torque) impulse to the physics body at its center of mass.
- [func applyImpulse(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](hasphysicsbody/applyimpulse(_:at:relativeto:).md)
  Applies an impulse to the physics body at the specified position.
### Resetting physics simulations
- [func resetPhysicsTransform(recursive: Bool)](hasphysicsbody/resetphysicstransform(recursive:).md)
  Resets the position, orientation, and velocities of the simulated physics body.
- [func resetPhysicsTransform(Transform, recursive: Bool)](hasphysicsbody/resetphysicstransform(_:recursive:).md)
  Resets the position and velocities of the simulated physics body.

## Relationships

### Inherits From
- [HasCollision](hascollision.md)
- [HasTransform](hastransform.md)
### Inherited By
- [HasPhysics](hasphysics.md)
### Conforming Types
- [ModelEntity](modelentity.md)

## See Also

- [protocol HasPhysicsMotion](hasphysicsmotion.md)
  An interface that provides velocity properties for physics simulations.
- [protocol HasPhysics](hasphysics.md)
  An interface that combines the physics body and physics motion interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsbody)*