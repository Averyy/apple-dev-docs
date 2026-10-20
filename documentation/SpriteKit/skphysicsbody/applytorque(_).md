# applyTorque(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Applies torque to an object.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
func applyTorque(_ torque: CGFloat)
```

```objc
- (void) applyTorque:(CGFloat) torque;
```

#### Discussion

This method generates an angular acceleration on the body without causing any linear acceleration. The force is applied for a single simulation step (one frame).

## Parameters

- `torque`: The amount of torque, in Newton-meters.

## See Also

### Applying Forces and Impulses to a Physics Body
- [Making Physics Bodies Move](../making-physics-bodies-move.md)
  Move a body using various physics properties, like velocity, gravity or impulses.
- [func applyForce(CGVector)](./applyforce%28_%29.md)
  Applies a force to the center of gravity of a physics body.
- [func applyForce(CGVector, at: CGPoint)](./applyforce%28_,at%29.md)
  Applies a force to a specific point of a physics body.
- [func applyImpulse(CGVector)](./applyimpulse%28_%29.md)
  Applies an impulse to the center of gravity of a physics body.
- [func applyAngularImpulse(CGFloat)](./applyangularimpulse%28_%29.md)
  Applies an impulse that imparts angular momentum to an object.
- [func applyImpulse(CGVector, at: CGPoint)](./applyimpulse%28_,at%29.md)
  Applies an impulse to a specific point of a physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/applytorque(_:))*