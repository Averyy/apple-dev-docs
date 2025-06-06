# color

**Framework**: SpriteKit  
**Kind**: property

The sprite’s color.

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
@MainActor
var color: UIColor { get set }
```

## Mentions

- [Tinting a Sprite](tinting-a-sprite.md)

#### Discussion

If the [`texture`](skspritenode/texture.md) property is non-`nil`, the red, green, and blue values of the color property are blended with the texture before the texture is drawn and the alpha property is ignored. If the [`texture`](skspritenode/texture.md) property is `nil`, the color (including the alpha component) is used to draw a single-color rectangle.

## See Also

- [Tinting a Sprite](tinting-a-sprite.md)
  Provide a color and blend factor to additively color your sprite.
- [var colorBlendFactor: CGFloat](skspritenode/colorblendfactor.md)
  A floating-point value that describes how the color is blended with the sprite’s texture.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/color)*