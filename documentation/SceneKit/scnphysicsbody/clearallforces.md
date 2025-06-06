# clearAllForces()

**Framework**: SceneKit  
**Kind**: method

Cancels all continuous forces and torques acting on the physics body during the current simulation step.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func clearAllForces()
```

#### Discussion

When you pass [`false`](https://developer.apple.com/documentation/swift/false) for the `impulse` parameter in the [`applyForce(_:asImpulse:)`](scnphysicsbody/applyforce(_:asimpulse:).md), [`applyForce(_:at:asImpulse:)`](scnphysicsbody/applyforce(_:at:asimpulse:).md), or [`applyTorque(_:asImpulse:)`](scnphysicsbody/applytorque(_:asimpulse:).md) method, SceneKit waits until the end of the current simulation step before applying its effect. At that time, SceneKit sums all forces and torques applied during that simulation step and changes the velocity or angular velocity of the body according to the net effect of those forces and torques.

Call [`clearAllForces()`](scnphysicsbody/clearallforces().md) to cancel any forces and torques previously applied during the current simulation step.

## See Also

- [func applyForce(SCNVector3, asImpulse: Bool)](scnphysicsbody/applyforce(_:asimpulse:).md)
  Applies a force or impulse to the body at its center of mass.
- [func applyForce(SCNVector3, at: SCNVector3, asImpulse: Bool)](scnphysicsbody/applyforce(_:at:asimpulse:).md)
  Applies a force or impulse to the body at a specific point.
- [func applyTorque(SCNVector4, asImpulse: Bool)](scnphysicsbody/applytorque(_:asimpulse:).md)
  Applies a net torque or a change in angular momentum to the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/clearallforces())*