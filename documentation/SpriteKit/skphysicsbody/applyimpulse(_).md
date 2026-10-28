# applyImpulse(_:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Instance Method

Applies an impulse to the center of gravity of a physics body.

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
func applyImpulse(_ impulse: CGVector)
```

```objc
- (void) applyImpulse:(CGVector) impulse;
```

## Discussion

This method affects the body’s linear velocity without changing the body’s angular velocity.

## Parameters

- `impulse`: A vector that describes how much momentum was imparted in each dimension. The impulse is measured in Newton-seconds.

## See Also

### Applying Forces and Impulses to a Physics Body
- [Making Physics Bodies Move](../making-physics-bodies-move.md)
  Move a body using various physics properties, like velocity, gravity or impulses.
- [func applyForce(CGVector)](./applyforce%28_%29.md)
  Applies a force to the center of gravity of a physics body.
- [func applyTorque(CGFloat)](./applytorque%28_%29.md)
  Applies torque to an object.
- [func applyForce(CGVector, at: CGPoint)](./applyforce%28_,at%29.md)
  Applies a force to a specific point of a physics body.
- [func applyAngularImpulse(CGFloat)](./applyangularimpulse%28_%29.md)
  Applies an impulse that imparts angular momentum to an object.
- [func applyImpulse(CGVector, at: CGPoint)](./applyimpulse%28_,at%29.md)
  Applies an impulse to a specific point of a physics body.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skphysicsbody/applyimpulse(_:))*