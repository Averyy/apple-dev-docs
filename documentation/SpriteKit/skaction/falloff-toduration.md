# falloff(to:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that animates a change of a physics field’s falloff.

**Availability**:
- iOS 8.0+
- iPadOS 8.0+
- Mac Catalyst 13.1+
- macOS 10.10+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 1.0+

## Declaration

```swift
class func falloff(to falloff: Float, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action runs, the field node’s [`falloff`](skfieldnode/falloff.md) property animates from its current value to its new value. This action is not reversible.

## Parameters

- `falloff`: The new falloff for the field.
- `duration`: The duration of the animation, in seconds.

## See Also

- [class func applyForce(CGVector, duration: TimeInterval) -> SKAction](skaction/applyforce(_:duration:).md)
  Creates an action that applies a force to the center of gravity of a node’s physics body.
- [class func applyTorque(CGFloat, duration: TimeInterval) -> SKAction](skaction/applytorque(_:duration:).md)
  Creates an action that applies a torque to a node’s physics body.
- [class func applyForce(CGVector, at: CGPoint, duration: TimeInterval) -> SKAction](skaction/applyforce(_:at:duration:).md)
  Creates an action that applies a force to a specific point on a node’s physics body.
- [class func applyImpulse(CGVector, duration: TimeInterval) -> SKAction](skaction/applyimpulse(_:duration:).md)
  Creates an action that applies an impulse to the center of gravity of a physics body.
- [class func applyAngularImpulse(CGFloat, duration: TimeInterval) -> SKAction](skaction/applyangularimpulse(_:duration:).md)
  Creates an action that applies an angular impulse to a node’s physics body.
- [class func applyImpulse(CGVector, at: CGPoint, duration: TimeInterval) -> SKAction](skaction/applyimpulse(_:at:duration:).md)
  Creates an action that applies an impulse to a specific point of a node’s physics body.
- [class func applyImpulse(CGVector, duration: TimeInterval) -> SKAction](skaction/applyimpulse(_:duration:).md)
  Creates an action that applies an impulse to the center of gravity of a physics body.
- [class func changeCharge(to: Float, duration: TimeInterval) -> SKAction](skaction/changecharge(to:duration:).md)
  Creates an action that changes the charge of a node’s physics body to a new value.
- [class func changeCharge(by: Float, duration: TimeInterval) -> SKAction](skaction/changecharge(by:duration:).md)
  Creates an action that changes the charge of a node’s physics body by a relative value.
- [class func changeMass(to: Float, duration: TimeInterval) -> SKAction](skaction/changemass(to:duration:).md)
  Creates an action that changes the mass of a node’s physics body to a new value.
- [class func changeMass(by: Float, duration: TimeInterval) -> SKAction](skaction/changemass(by:duration:).md)
  Creates an action that changes the mass of a node’s physics body by a relative value.
- [class func strength(to: Float, duration: TimeInterval) -> SKAction](skaction/strength(to:duration:).md)
  Creates an action that animates a change of a physics field’s strength.
- [class func strength(by: Float, duration: TimeInterval) -> SKAction](skaction/strength(by:duration:).md)
  Creates an action that animates a change of a physics field’s strength to a value relative to the existing value.
- [class func falloff(by: Float, duration: TimeInterval) -> SKAction](skaction/falloff(by:duration:).md)
  Creates an action that animates a change of a physics field’s falloff to a value relative to the existing value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/falloff(to:duration:))*