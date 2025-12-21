# colorBlendFactor

**Framework**: SpriteKit  
**Kind**: property

A floating-point value that describes how the color is blended with the font color.

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

#### Discussion

The value must be a number between `0.0` and `1.0`, inclusive. The default value (`0.0`) indicates that the color property is ignored and that the label’s font color should be used unmodified. For values greater than `0.0`, the font color is blended with the blend color, with the maximum value of 1.0 determining that the font color is 100% of the blend color.

## See Also

- [var color: UIColor?](sklabelnode/color.md)
  An alternative to the font color that can be used for animations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/spritekit/sklabelnode/colorblendfactor)*