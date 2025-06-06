# rotate(toAngle:duration:shortestUnitArc:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that rotates the node to an absolute value.

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
class func rotate(toAngle radians: CGFloat, duration: TimeInterval, shortestUnitArc: Bool) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`zRotation`](sknode/zrotation.md) property is animated to the new angle.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `radians`: The angle to rotate the node to, in radians.
- `duration`: The duration of the animation.
- `shortestUnitArc`: If  , the rotation is performed in whichever direction results in the smallest rotation. If  , the rotation is interpolated.

## See Also

- [class func rotate(byAngle: CGFloat, duration: TimeInterval) -> SKAction](skaction/rotate(byangle:duration:).md)
  Creates an action that rotates the node by a relative value.
- [class func rotate(toAngle: CGFloat, duration: TimeInterval) -> SKAction](skaction/rotate(toangle:duration:).md)
  Creates an action that rotates the node counterclockwise to an absolute angle.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/rotate(toangle:duration:shortestunitarc:))*