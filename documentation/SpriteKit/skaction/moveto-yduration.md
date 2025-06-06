# moveTo(y:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that moves a node vertically.

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
class func moveTo(y: CGFloat, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`position`](sknode/position.md) property animates from its current position to its new position.

This action is not reversible; the reverse of this action has the same duration but does not move the node.

## Parameters

- `y`: The y-value for the node’s new position.
- `duration`: The duration of the animation.

## See Also

- [class func moveBy(x: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](skaction/moveby(x:y:duration:).md)
  Creates an action that moves a node relative to its current position.
- [class func move(by: CGVector, duration: TimeInterval) -> SKAction](skaction/move(by:duration:).md)
  Creates an action that moves a node relative to its current position.
- [class func move(to: CGPoint, duration: TimeInterval) -> SKAction](skaction/move(to:duration:).md)
  Creates an action that moves a node to a new position.
- [class func moveTo(x: CGFloat, duration: TimeInterval) -> SKAction](skaction/moveto(x:duration:).md)
  Creates an action that moves a node horizontally.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/moveto(y:duration:))*