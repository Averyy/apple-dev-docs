# rotate(byAngle:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that rotates the node by a relative value.

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
class func rotate(byAngle radians: CGFloat, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`zRotation`](sknode/zrotation.md) property animates to the new angle.

This action is reversible; the reverse is created as if the following code is executed:

## Parameters

- `radians`: The amount to rotate the node, in radians.
- `duration`: The duration of the animation.

## See Also

- [class func rotate(toAngle: CGFloat, duration: TimeInterval) -> SKAction](skaction/rotate(toangle:duration:).md)
  Creates an action that rotates the node counterclockwise to an absolute angle.
- [class func rotate(toAngle: CGFloat, duration: TimeInterval, shortestUnitArc: Bool) -> SKAction](skaction/rotate(toangle:duration:shortestunitarc:).md)
  Creates an action that rotates the node to an absolute value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/rotate(byangle:duration:))*