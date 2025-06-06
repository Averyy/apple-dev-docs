# applyImpulse(_:at:)

**Framework**: SpriteKit  
**Kind**: method

Applies an impulse to a specific point of a physics body.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
func applyImpulse(_ impulse: CGVector, at point: CGPoint)
```

#### Discussion

Because this impulse is applied to a specific point on the object, it may change both the body’s velocity and angular velocity.

## Parameters

- `impulse`: A vector that describes how much momentum to impart to the body. The impulse is measured in Newton-seconds.
- `point`: A point in scene coordinates that defines where the impulse was applied to the physics body.

## See Also

- [Making Physics Bodies Move](making-physics-bodies-move.md)
  Move a body using various physics properties, like velocity, gravity or impulses.
- [func applyForce(CGVector)](skphysicsbody/applyforce(_:).md)
  Applies a force to the center of gravity of a physics body.
- [func applyTorque(CGFloat)](skphysicsbody/applytorque(_:).md)
  Applies torque to an object.
- [func applyForce(CGVector, at: CGPoint)](skphysicsbody/applyforce(_:at:).md)
  Applies a force to a specific point of a physics body.
- [func applyImpulse(CGVector)](skphysicsbody/applyimpulse(_:).md)
  Applies an impulse to the center of gravity of a physics body.
- [func applyAngularImpulse(CGFloat)](skphysicsbody/applyangularimpulse(_:).md)
  Applies an impulse that imparts angular momentum to an object.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/applyimpulse(_:at:))*