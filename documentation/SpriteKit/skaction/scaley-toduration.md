# scaleY(to:duration:)

**Framework**: SpriteKit  
**Kind**: method

Creates an action that changes the y scale value of a node to a new value.

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
class func scaleY(to scale: CGFloat, duration: TimeInterval) -> SKAction
```

#### Return Value

A new action object.

#### Discussion

When the action executes, the node’s [`yScale`](sknode/yscale.md) property animates to the new value.

This action is not reversible; the reverse of this action has the same duration but does not change anything.

## Parameters

- `scale`: The new value for the node’s y scale value.
- `duration`: The duration of the animation.

## See Also

- [class func scale(by: CGFloat, duration: TimeInterval) -> SKAction](skaction/scale(by:duration:).md)
  Creates an action that changes the x and y scale values of a node by a relative value.
- [class func scale(to: CGSize, duration: TimeInterval) -> SKAction](skaction/scale(to:duration:)-43bz6.md)
  Creates an action that changes the x and y scale values of a node to achieve
- [class func scale(to: CGFloat, duration: TimeInterval) -> SKAction](skaction/scale(to:duration:)-1xyzs.md)
  Creates an action that changes the x and y scale values of a node.
- [class func scaleX(by: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](skaction/scalex(by:y:duration:).md)
  Creates an action that adds relative values to the x and y scale values of a node.
- [class func scaleX(to: CGFloat, y: CGFloat, duration: TimeInterval) -> SKAction](skaction/scalex(to:y:duration:).md)
  Creates an action that changes the x and y scale values of a node.
- [class func scaleX(to: CGFloat, duration: TimeInterval) -> SKAction](skaction/scalex(to:duration:).md)
  Creates an action that changes the x scale value of a node to a new value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skaction/scaley(to:duration:))*