# scale(to:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that changes the x and y scale values of a node.

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
class func scale(to scale: CGFloat, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) scaleTo:(CGFloat) scale duration:(NSTimeInterval) duration;
```

## Return Value

A new action object.

## Discussion

When the action executes, the node’s [`xScale`](../sknode/xscale.md) and [`yScale`](../sknode/yscale.md) properties are animated to the new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `scale`: The new value for the node’s x and y scale values.
- `duration`: The duration of the animation.

## See Also

### Animating the Scaling of a Node
- [class func scale(by: CGFloat, duration: TimeInterval) -> SKAction](./scale%28by,duration%29.md)
  Creates an action that changes the x and y scale values of a node by a relative value.
- [class func scale(to: CGSize, duration: TimeInterval) -> SKAction](./scale%28to,duration%29-43bz6.md)
  Creates an action that changes the x and y scale values of a node to achieve
- [class func scaleX(by: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](./scalex%28by,y,duration%29.md)
  Creates an action that adds relative values to the x and y scale values of a node.
- [class func scaleX(to: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](./scalex%28to,y,duration%29.md)
  Creates an action that changes the x and y scale values of a node.
- [class func scaleX(to: CGFloat, duration: TimeInterval) -> SKAction](./scalex%28to,duration%29.md)
  Creates an action that changes the x scale value of a node to a new value.
- [class func scaleY(to: CGFloat, duration: TimeInterval) -> SKAction](./scaley%28to,duration%29.md)
  Creates an action that changes the y scale value of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/scale(to:duration:)-1xyzs)*