# colorBlendFactor

**Framework**: SpriteKit  
**Kind**: property

A floating-point value that describes how the color is blended with the sprite’s texture.

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
var colorBlendFactor: CGFloat { get set }
```

## Mentions

- [Tinting a Sprite](tinting-a-sprite.md)

#### Discussion

The value must be a number between `0.0` and `1.0`, inclusive. The default value (`0.0`) indicates the color property is ignored and that the texture’s values should be used unmodified. For values greater than `0.0`, the texture is blended with the color before being drawn to the scene.

## See Also

- [Tinting a Sprite](tinting-a-sprite.md)
  Provide a color and blend factor to additively color your sprite.
- [var color: UIColor](skspritenode/color.md)
  The sprite’s color.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/skspritenode/colorblendfactor)*