# rotate(toAngle:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that rotates the node counterclockwise to an absolute angle.

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
class func rotate(toAngle radians: CGFloat, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) rotateToAngle:(CGFloat) radians duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`zRotation`](../sknode/zrotation.md) property is interpolated to the new angle.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `radians`: The angle to rotate the node to, in radians.
- `duration`: The duration of the animation.

## See Also

### Animating the Rotation of a Node
- [class func rotate(byAngle: CGFloat, duration: TimeInterval) -> SKAction](./rotate%28byangle,duration%29.md)
  Creates an action that rotates the node by a relative value.
- [class func rotate(toAngle: CGFloat, duration: TimeInterval, shortestUnitArc: Bool) -> SKAction](./rotate%28toangle,duration,shortestunitarc%29.md)
  Creates an action that rotates the node to an absolute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/rotate(toangle:duration:))*