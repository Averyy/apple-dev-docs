# applyForce(_:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that applies a force to the center of gravity of a node’s physics body.

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
class func applyForce(_ force: CGVector, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) applyForce:(CGVector) force duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

When the action executes, the force is applied continuously to the physics body for the duration of the action. This action accelerates the body without imparting any angular acceleration to it.

This action is reversible; it applies an equal force in the opposite direction.

## Parameters

- `force`: A vector that describes how much force is applied in each dimension. The force is measured in Newtons.
- `duration`: The duration over which the force is applied to the physics body.

## See Also

### Animating Properties of a Node’s Physics Body
- [class func applyTorque(CGFloat, duration: TimeInterval) -> SKAction](./applytorque%28_,duration%29.md)
  Creates an action that applies a torque to a node’s physics body.
- [class func applyForce(CGVector, at: CGPoint, duration: TimeInterval) -> SKAction](./applyforce%28_,at,duration%29.md)
  Creates an action that applies a force to a specific point on a node’s physics body.
- [class func applyImpulse(CGVector, duration: TimeInterval) -> SKAction](./applyimpulse%28_,duration%29.md)
  Creates an action that applies an impulse to the center of gravity of a physics body.
- [class func applyAngularImpulse(CGFloat, duration: TimeInterval) -> SKAction](./applyangularimpulse%28_,duration%29.md)
  Creates an action that applies an angular impulse to a node’s physics body.
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/applyforce(_:duration:))*