# anchorPoint

**Framework**: SpriteKit  
**Kind**: property  
**Role**: Instance Property

Defines the point in the sprite that corresponds to the node’s position.

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
var anchorPoint: CGPoint { get set }
```

```objc
@property (nonatomic) CGPoint anchorPoint;
```

## Mentions

- [Animating a Sprite by Changing its Texture](../animating-a-sprite-by-changing-its-texture.md)
- [Using the Anchor Point to Move a Sprite](../using-the-anchor-point-to-move-a-sprite.md)

## Discussion

You specify the value for this property in the unit coordinate space. The default value is `(0.5,0.5)`, which means that the sprite is centered on its position.

## See Also

### Setting a Sprite’s Size and Position
- [Using the Anchor Point to Move a Sprite](../using-the-anchor-point-to-move-a-sprite.md)
  Learn how the anchor point affects a sprite’s position.
- [var size: CGSize](./size.md)
  The dimensions of the sprite, in points.
- [func scale(to: CGSize)](./scale%28to%29.md)
  Scales the sprite node to a specified size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/anchorpoint)*