# applyAngularImpulse(_:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that applies an angular impulse to a node’s physics body.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func applyAngularImpulse(_ impulse: CGFloat, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) applyAngularImpulse:(CGFloat) impulse duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

When the action executes, applies a constant torque to the physics body for the duration of the action. The torque is calculated by dividing the impulse strength by the duration of the action. This action affects the body’s angular velocity without changing the body’s linear velocity.

This action is reversible; it applies an equal angular impulse in the opposite direction.

## Parameters

- `impulse`: The total impulse to apply to the physics body. The impulse is measured in Newton-seconds.
- `duration`: The number of seconds over which to apply the impulse. For example, if you specify a duration of four seconds, one quarter of the impulse will be applied each second.

## See Also

### Animating Properties of a Node’s Physics Body
- [class func applyForce(CGVector, duration: TimeInterval) -> SKAction](./applyforce%28_,duration%29.md)
  Creates an action that applies a force to the center of gravity of a node’s physics body.
- [class func applyTorque(CGFloat, duration: TimeInterval) -> SKAction](./applytorque%28_,duration%29.md)
  Creates an action that applies a torque to a node’s physics body.
- [class func applyForce(CGVector, at: CGPoint, duration: TimeInterval) -> SKAction](./applyforce%28_,at,duration%29.md)
  Creates an action that applies a force to a specific point on a node’s physics body.
- [class func applyImpulse(CGVector, duration: TimeInterval) -> SKAction](./applyimpulse%28_,duration%29.md)
  Creates an action that applies an impulse to the center of gravity of a physics body.
- [class func applyImpulse(CGVector, at: CGPoint, duration: TimeInterval) -> SKAction](./applyimpulse%28_,at,duration%29.md)
  Creates an action that applies an impulse to a specific point of a node’s physics body.
- [class func applyImpulse(CGVector, duration: TimeInterval) -> SKAction](./applyimpulse%28_,duration%29.md)
  Creates an action that applies an impulse to the center of gravity of a physics body.
- [class func changeCharge(to: Float, duration: TimeInterval) -> SKAction](./changecharge%28to,duration%29.md)
  Creates an action that changes the charge of a node’s physics body to a new value.
- [class func changeCharge(by: Float, duration: TimeInterval) -> SKAction](./changecharge%28by,duration%29.md)
  Creates an action that changes the charge of a node’s physics body by a relative value.
- [class func changeMass(to: Float, duration: TimeInterval) -> SKAction](./changemass%28to,duration%29.md)
  Creates an action that changes the mass of a node’s physics body to a new value.
- [class func changeMass(by: Float, duration: TimeInterval) -> SKAction](./changemass%28by,duration%29.md)
  Creates an action that changes the mass of a node’s physics body by a relative value.
- [class func strength(to: Float, duration: TimeInterval) -> SKAction](./strength%28to,duration%29.md)
  Creates an action that animates a change of a physics field’s strength.
- [class func strength(by: Float, duration: TimeInterval) -> SKAction](./strength%28by,duration%29.md)
  Creates an action that animates a change of a physics field’s strength to a value relative to the existing value.
- [class func falloff(to: Float, duration: TimeInterval) -> SKAction](./falloff%28to,duration%29.md)
  Creates an action that animates a change of a physics field’s falloff.
- [class func falloff(by: Float, duration: TimeInterval) -> SKAction](./falloff%28by,duration%29.md)
  Creates an action that animates a change of a physics field’s falloff to a value relative to the existing value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/applyangularimpulse(_:duration:))*