# applyForce(_:at:)

**Framework**: SpriteKit  
**Kind**: method

Applies a force to a specific point of a physics body.

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
func applyForce(_ force: CGVector, at point: CGPoint)
```

#### Discussion

Because the force is applied to a specific point on the body, it may impart both linear acceleration and angular acceleration. The force is applied for a single simulation step (one frame).

## Parameters

- `force`: A vector that describes how much force was applied in each dimension. The force is measured in Newtons.
- `point`: A point in scene coordinates that defines where the force was applied to the physics body.

## See Also

- [Making Physics Bodies Move](making-physics-bodies-move.md)
  Move a body using various physics properties, like velocity, gravity or impulses.
- [func applyForce(CGVector)](skphysicsbody/applyforce(_:).md)
  Applies a force to the center of gravity of a physics body.
- [func applyTorque(CGFloat)](skphysicsbody/applytorque(_:).md)
  Applies torque to an object.
- [func applyImpulse(CGVector)](skphysicsbody/applyimpulse(_:).md)
  Applies an impulse to the center of gravity of a physics body.
- [func applyAngularImpulse(CGFloat)](skphysicsbody/applyangularimpulse(_:).md)
  Applies an impulse that imparts angular momentum to an object.
- [func applyImpulse(CGVector, at: CGPoint)](skphysicsbody/applyimpulse(_:at:).md)
  Applies an impulse to a specific point of a physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/applyforce(_:at:))*