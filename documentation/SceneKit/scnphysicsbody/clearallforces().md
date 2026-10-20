# clearAllForces()

**Framework**: SceneKit  
**Kind**: method  
**Role**: Instance Method

Cancels all continuous forces and torques acting on the physics body during the current simulation step.

**Availability**:
- iOS 8.0+ - Deprecated in 26.0
- iPadOS 8.0+ - Deprecated in 26.0
- Mac Catalyst 13.1+ - Deprecated in 26.0
- macOS 10.8+ - Deprecated in 26.0
- tvOS 9.0+ - Deprecated in 26.0
- visionOS 1.0+ - Deprecated in 26.0
- watchOS 3.0+ - Deprecated in 26.0

## Declaration

```swift
func clearAllForces()
```

```objc
- (void) clearAllForces;
```

#### Discussion

When you pass [`false`](../../Swift/false.md) for the `impulse` parameter in the [`applyForce(_:asImpulse:)`](./applyforce%28_,asimpulse%29.md), [`applyForce(_:at:asImpulse:)`](./applyforce%28_,at,asimpulse%29.md), or [`applyTorque(_:asImpulse:)`](./applytorque%28_,asimpulse%29.md) method, SceneKit waits until the end of the current simulation step before applying its effect. At that time, SceneKit sums all forces and torques applied during that simulation step and changes the velocity or angular velocity of the body according to the net effect of those forces and torques.

Call [`clearAllForces()`](./clearallforces%28%29.md) to cancel any forces and torques previously applied during the current simulation step.

## See Also

### Applying Forces, Impulses, and Torques
- [func applyForce(SCNVector3, asImpulse: Bool)](./applyforce%28_,asimpulse%29.md)
  Applies a force or impulse to the body at its center of mass.
- [func applyForce(SCNVector3, at: SCNVector3, asImpulse: Bool)](./applyforce%28_,at,asimpulse%29.md)
  Applies a force or impulse to the body at a specific point.
- [func applyTorque(SCNVector4, asImpulse: Bool)](./applytorque%28_,asimpulse%29.md)
  Applies a net torque or a change in angular momentum to the body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/scenekit/scnphysicsbody/clearallforces())*