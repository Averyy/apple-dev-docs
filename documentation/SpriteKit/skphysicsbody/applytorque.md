# applyTorque(_:)

**Framework**: SpriteKit  
**Kind**: method

Applies torque to an object.

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
func applyTorque(_ torque: CGFloat)
```

#### Discussion

This method generates an angular acceleration on the body without causing any linear acceleration. The force is applied for a single simulation step (one frame).

## Parameters

- `torque`: The amount of torque, in Newton-meters.

## See Also

- [Making Physics Bodies Move](making-physics-bodies-move.md)
  Move a body using various physics properties, like velocity, gravity or impulses.
- [func applyForce(CGVector)](skphysicsbody/applyforce(_:).md)
  Applies a force to the center of gravity of a physics body.
- [func applyForce(CGVector, at: CGPoint)](skphysicsbody/applyforce(_:at:).md)
  Applies a force to a specific point of a physics body.
- [func applyImpulse(CGVector)](skphysicsbody/applyimpulse(_:).md)
  Applies an impulse to the center of gravity of a physics body.
- [func applyAngularImpulse(CGFloat)](skphysicsbody/applyangularimpulse(_:).md)
  Applies an impulse that imparts angular momentum to an object.
- [func applyImpulse(CGVector, at: CGPoint)](skphysicsbody/applyimpulse(_:at:).md)
  Applies an impulse to a specific point of a physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/applytorque(_:))*