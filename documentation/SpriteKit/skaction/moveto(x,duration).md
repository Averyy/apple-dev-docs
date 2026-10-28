# moveTo(x:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that moves a node horizontally.

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
class func moveTo(x: CGFloat, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) moveToX:(CGFloat) x duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`position`](../sknode/position.md) property animates from its current position to its new position.

This action is not reversible; the reverse of this action has the same duration but does not move the node.

## Parameters

- `x`: The x-value for the node’s new position.
- `duration`: The duration of the animation.

## See Also

### Animating a Node’s Position in a Linear Path
- [class func moveBy(x: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](./moveby%28x,y,duration%29.md)
  Creates an action that moves a node relative to its current position.
- [class func move(by: CGVector, duration: TimeInterval) -> SKAction](./move%28by,duration%29.md)
  Creates an action that moves a node relative to its current position.
- [class func move(to: CGPoint, duration: TimeInterval) -> SKAction](./move%28to,duration%29.md)
  Creates an action that moves a node to a new position.
- [class func moveTo(y: CGFloat, duration: TimeInterval) -> SKAction](./moveto%28y,duration%29.md)
  Creates an action that moves a node vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/moveto(x:duration:))*