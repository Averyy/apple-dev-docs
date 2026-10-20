# scale(by:duration:)

**Framework**: SpriteKit  
**Kind**: method  
**Role**: Type Method

Creates an action that changes the x and y scale values of a node by a relative value.

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
class func scale(by scale: CGFloat, duration: TimeInterval) -> SKAction
```

```objc
+ (SKAction *) scaleBy:(CGFloat) scale duration:(NSTimeInterval) duration;
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`xScale`](../sknode/xscale.md) and [`yScale`](../sknode/yscale.md) properties are animated to the new value.

This action is reversible; the reverse is created as if the following code is executed:

**Swift**:

```swift
let action = SKAction.scale(by: -scale, duration: sec)
```

**Obj-C**:

```objc
[SKAction scaleBy: -scale duration: sec];
```

## Parameters

- `scale`: The amount to add to the node’s x and y scale values.
- `duration`: The duration of the animation.

## See Also

### Animating the Scaling of a Node
- [class func scale(to: CGSize, duration: TimeInterval) -> SKAction](./scale%28to,duration%29-43bz6.md)
  Creates an action that changes the x and y scale values of a node to achieve
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

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/scale(by:duration:))*