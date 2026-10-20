# HasPhysicsBody

**Framework**: RealityKit  
**Kind**: protocol  
**Role**: Protocol

An interface that enables physics simulations based on the rules of Newtonian mechanics.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 26.0+
- visionOS

## Declaration

```swift
@MainActor
@preconcurrency protocol HasPhysicsBody : HasCollision
```

## Topics

### Getting the component
- [var physicsBody: PhysicsBodyComponent?](./hasphysicsbody/physicsbody.md)
  A component that is used for physics simulations of the model entity in accordance with the laws of Newtonian mechanics.
### Adding and clearing forces
- [func addForce(SIMD3<Float>, relativeTo: Entity?)](./hasphysicsbody/addforce%28_,relativeto%29.md)
  Applies a force to the physics body at its center of mass.
- [func addForce(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](./hasphysicsbody/addforce%28_,at,relativeto%29.md)
  Applies a force to the physics body at the specified position.
- [func addTorque(SIMD3<Float>, relativeTo: Entity?)](./hasphysicsbody/addtorque%28_,relativeto%29.md)
  Applies a torque to the physics body at its center of mass.
- [func clearForcesAndTorques()](./hasphysicsbody/clearforcesandtorques%28%29.md)
  Clears all forces previously added to the physics body.
### Applying impulses
- [func applyLinearImpulse(SIMD3<Float>, relativeTo: Entity?)](./hasphysicsbody/applylinearimpulse%28_,relativeto%29.md)
  Applies an impulse to the physics body at its center of mass.
- [func applyAngularImpulse(SIMD3<Float>, relativeTo: Entity?)](./hasphysicsbody/applyangularimpulse%28_,relativeto%29.md)
  Applies an angular (torque) impulse to the physics body at its center of mass.
- [func applyImpulse(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](./hasphysicsbody/applyimpulse%28_,at,relativeto%29.md)
  Applies an impulse to the physics body at the specified position.
### Resetting physics simulations
- [func resetPhysicsTransform(recursive: Bool)](./hasphysicsbody/resetphysicstransform%28recursive%29.md)
  Resets the position, orientation, and velocities of the simulated physics body.
- [func resetPhysicsTransform(Transform, recursive: Bool)](./hasphysicsbody/resetphysicstransform%28_,recursive%29.md)
  Resets the position and velocities of the simulated physics body.

## Relationships

### Inherits From
- [HasCollision](./hascollision.md)
- [HasTransform](./hastransform.md)
### Inherited By
- [HasPhysics](./hasphysics.md)
### Conforming Types
- [ModelEntity](./modelentity.md)

## See Also

### Entity compliance
- [protocol HasPhysicsMotion](./hasphysicsmotion.md)
  An interface that provides velocity properties for physics simulations.
- [protocol HasPhysics](./hasphysics.md)
  An interface that combines the physics body and physics motion interfaces.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/hasphysicsbody)*