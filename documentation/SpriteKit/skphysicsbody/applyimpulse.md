# applyImpulse(_:)

**Framework**: SpriteKit  
**Kind**: method

Applies an impulse to the center of gravity of a physics body.

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
func applyImpulse(_ impulse: CGVector)
```

#### Discussion

This method affects the body’s linear velocity without changing the body’s angular velocity.

## Parameters

- `impulse`: A vector that describes how much momentum was imparted in each dimension. The impulse is measured in Newton-seconds.

## See Also

- [Making Physics Bodies Move](making-physics-bodies-move.md)
  Move a body using various physics properties, like velocity, gravity or impulses.
- [func applyForce(CGVector)](skphysicsbody/applyforce(_:).md)
  Applies a force to the center of gravity of a physics body.
- [func applyTorque(CGFloat)](skphysicsbody/applytorque(_:).md)
  Applies torque to an object.
- [func applyForce(CGVector, at: CGPoint)](skphysicsbody/applyforce(_:at:).md)
  Applies a force to a specific point of a physics body.
- [func applyAngularImpulse(CGFloat)](skphysicsbody/applyangularimpulse(_:).md)
  Applies an impulse that imparts angular momentum to an object.
- [func applyImpulse(CGVector, at: CGPoint)](skphysicsbody/applyimpulse(_:at:).md)
  Applies an impulse to a specific point of a physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/applyimpulse(_:))*