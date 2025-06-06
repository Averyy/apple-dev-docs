# scale(to:duration:)

**Framework**: SpriteKit  
**Kind**: method

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

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`xScale`](sknode/xscale.md) and [`yScale`](sknode/yscale.md) properties are animated to achieve the specified size in its parent’s coordinate space.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `size`: The new size of the node.
- `duration`: The duration of the animation.

## See Also

- [class func scale(by: CGFloat, duration: TimeInterval) -> SKAction](skaction/scale(by:duration:).md)
  Creates an action that changes the x and y scale values of a node by a relative value.
- [class func scale(to: CGFloat, duration: TimeInterval) -> SKAction](skaction/scale(to:duration:)-1xyzs.md)
  Creates an action that changes the x and y scale values of a node.
- [class func scaleX(by: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](skaction/scalex(by:y:duration:).md)
  Creates an action that adds relative values to the x and y scale values of a node.
- [class func scaleX(to: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](skaction/scalex(to:y:duration:).md)
  Creates an action that changes the x and y scale values of a node.
- [class func scaleX(to: CGFloat, duration: TimeInterval) -> SKAction](skaction/scalex(to:duration:).md)
  Creates an action that changes the x scale value of a node to a new value.
- [class func scaleY(to: CGFloat, duration: TimeInterval) -> SKAction](skaction/scaley(to:duration:).md)
  Creates an action that changes the y scale value of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/scale(to:duration:)-43bz6)*