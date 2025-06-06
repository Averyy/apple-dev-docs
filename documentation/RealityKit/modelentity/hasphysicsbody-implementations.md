# HasPhysicsBody Implementations

**Framework**: RealityKit

## Topics

### Instance Properties
- [var physicsBody: PhysicsBodyComponent?](modelentity/physicsbody.md)
  A component that is used for physics simulations of the model entity in accordance with the laws of Newtonian mechanics.
### Instance Methods
- [func addForce(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](modelentity/addforce(_:at:relativeto:).md)
  Applies a force to the physics body at the specified position.
- [func addForce(SIMD3<Float>, relativeTo: Entity?)](modelentity/addforce(_:relativeto:).md)
  Applies a force to the physics body at its center of mass.
- [func addTorque(SIMD3<Float>, relativeTo: Entity?)](modelentity/addtorque(_:relativeto:).md)
  Applies a torque to the physics body at its center of mass.
- [func applyAngularImpulse(SIMD3<Float>, relativeTo: Entity?)](modelentity/applyangularimpulse(_:relativeto:).md)
  Applies an angular (torque) impulse to the physics body at its center of mass.
- [func applyImpulse(SIMD3<Float>, at: SIMD3<Float>, relativeTo: Entity?)](modelentity/applyimpulse(_:at:relativeto:).md)
  Applies an impulse to the physics body at the specified position.
- [func applyLinearImpulse(SIMD3<Float>, relativeTo: Entity?)](modelentity/applylinearimpulse(_:relativeto:).md)
  Applies an impulse to the physics body at its center of mass.
- [func clearForcesAndTorques()](modelentity/clearforcesandtorques.md)
  Clears all forces previously added to the physics body.
- [func resetPhysicsTransform(Transform, recursive: Bool)](modelentity/resetphysicstransform(_:recursive:).md)
  Resets the position and velocities of the simulated physics body.
- [func resetPhysicsTransform(recursive: Bool)](modelentity/resetphysicstransform(recursive:).md)
  Resets the position, orientation, and velocities of the simulated physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/realitykit/modelentity/hasphysicsbody-implementations)*