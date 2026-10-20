# scale(to:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that changes the x and y scale values of a node to achieve

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
class func scale(to size: CGSize, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) scaleToSize:(CGSize) size duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`xScale`](../sknode/xscale.md) and [`yScale`](../sknode/yscale.md) properties are animated to achieve the specified size in its parent’s coordinate space.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `size`: The new size of the node.
- `duration`: The duration of the animation.

## See Also

### Animating the Scaling of a Node
- [class func scale(by: CGFloat, duration: TimeInterval) -> SKAction](./scale%28by,duration%29.md)
  Creates an action that changes the x and y scale values of a node by a relative value.
- [class func scale(to: CGFloat, duration: TimeInterval) -> SKAction](./scale%28to,duration%29-1xyzs.md)
  Creates an action that changes the x and y scale values of a node.
- [class func scaleX(by: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](./scalex%28by,y,duration%29.md)
  Creates an action that adds relative values to the x and y scale values of a node.
- [class func scaleX(to: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](./scalex%28to,y,duration%29.md)
  Creates an action that changes the x and y scale values of a node.
- [class func scaleX(to: CGFloat, duration: TimeInterval) -> SKAction](./scalex%28to,duration%29.md)
  Creates an action that changes the x scale value of a node to a new value.
- [class func scaleY(to: CGFloat, duration: TimeInterval) -> SKAction](./scaley%28to,duration%29.md)
  Creates an action that changes the y scale value of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/scale(to:duration:)-43bz6)*