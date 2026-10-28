# moveBy(x:y:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that moves a node relative to its current position.

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
class func moveBy(x deltaX: CGFloat, y deltaY: CGFloat, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) moveByX:(CGFloat) deltaX y:(CGFloat) deltaY duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`position`](../sknode/position.md) property animates from its current position to its new position.

This action is reversible; the reverse is created as if the following code is executed:

**Swift**:

```swift
let negDelta = CGVector(dx: -deltaX, dy: -deltaY)
let action = SKAction.moveBy(x: -deltaX, y: -deltaX, duration: sec)
```

**Obj-C**:

```objc
[SKAction moveByX: -deltaX y: -deltaY duration: sec];
```

## Parameters

- `deltaX`: The x-value, in points, to add to the node’s position.
- `deltaY`: The y-value, in points, to add to the node’s position.
- `duration`: The duration of the animation.

## See Also

### Animating a Node’s Position in a Linear Path
- [class func move(by: CGVector, duration: TimeInterval) -> SKAction](./move%28by,duration%29.md)
  Creates an action that moves a node relative to its current position.
- [class func move(to: CGPoint, duration: TimeInterval) -> SKAction](./move%28to,duration%29.md)
  Creates an action that moves a node to a new position.
- [class func moveTo(x: CGFloat, duration: TimeInterval) -> SKAction](./moveto%28x,duration%29.md)
  Creates an action that moves a node horizontally.
- [class func moveTo(y: CGFloat, duration: TimeInterval) -> SKAction](./moveto%28y,duration%29.md)
  Creates an action that moves a node vertically.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/moveby(x:y:duration:))*