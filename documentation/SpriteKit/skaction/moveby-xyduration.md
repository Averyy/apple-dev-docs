# moveBy(x:y:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that moves a node relative to its current position.

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
class func moveBy(x deltaX: CGFloat, y deltaY: CGFloat, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`position`](sknode/position.md) property animates from its current position to its new position.

This action is reversible; the reverse is created as if the following code is executed:

## Parameters

- `deltaX`: The x-value, in points, to add to the node’s position.
- `deltaY`: The y-value, in points, to add to the node’s position.
- `duration`: The duration of the animation.

## See Also

- [class func move(by: CGVector, duration: TimeInterval) -> SKAction](skaction/move(by:duration:).md)
  Creates an action that moves a node relative to its current position.
- [class func move(to: CGPoint, duration: TimeInterval) -> SKAction](skaction/move(to:duration:).md)
  Creates an action that moves a node to a new position.
- [class func moveTo(x: CGFloat, duration: TimeInterval) -> SKAction](skaction/moveto(x:duration:).md)
  Creates an action that moves a node horizontally.
- [class func moveTo(y: CGFloat, duration: TimeInterval) -> SKAction](skaction/moveto(y:duration:).md)
  Creates an action that moves a node vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/moveby(x:y:duration:))*