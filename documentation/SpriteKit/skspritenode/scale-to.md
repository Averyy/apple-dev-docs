# scale(to:)

**Framework**: SpriteKit  
**Kind**: method

Scales the sprite node to a specified size.

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
@MainActor
func scale(to size: CGSize)
```

#### Discussion

This method works by setting the sprite node’s [`xScale`](sknode/xscale.md) and [`yScale`](sknode/yscale.md) to achieve the specified size in its parent’s coordinate space.

## See Also

- [Using the Anchor Point to Move a Sprite](using-the-anchor-point-to-move-a-sprite.md)
  Learn how the anchor point affects a sprite’s position.
- [var size: CGSize](skspritenode/size.md)
  The dimensions of the sprite, in points.
- [var anchorPoint: CGPoint](skspritenode/anchorpoint.md)
  Defines the point in the sprite that corresponds to the node’s position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/scale(to:))*