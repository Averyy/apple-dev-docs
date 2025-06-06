# NSFontRenderingMode

**Framework**: AppKit  
**Kind**: enum

The font rendering mode.

**Availability**:
- macOS ?+

## Declaration

```swift
enum NSFontRenderingMode
```

## Topics

### Constants
- [NSFontRenderingMode.defaultRenderingMode](nsfontrenderingmode/defaultrenderingmode.md)
  Determines the actual mode based on the user preference settings.
- [NSFontRenderingMode.antialiasedRenderingMode](nsfontrenderingmode/antialiasedrenderingmode.md)
  Specifies antialiased, floating-point advancements rendering mode (synonymous with printerFont).
- [NSFontRenderingMode.integerAdvancementsRenderingMode](nsfontrenderingmode/integeradvancementsrenderingmode.md)
  Specifies integer advancements rendering mode.
- [NSFontRenderingMode.antialiasedIntegerAdvancementsRenderingMode](nsfontrenderingmode/antialiasedintegeradvancementsrenderingmode.md)
  Specifies antialiased, integer advancements rendering mode.
### Initializers
- [init?(rawValue: UInt)](nsfontrenderingmode/init(rawvalue:).md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias NSGlyph](nsglyph.md)
  The type used to specify glyphs.
- [protocol NSGlyphStorage](nsglyphstorage.md)
  A set of methods that a glyph storage object must implement to interact properly with [`NSGlyphGenerator`](nsglyphgenerator.md).
- [class NSGlyphGenerator](nsglyphgenerator.md)
  An object that performs the initial, nominal glyph generation phase in the layout process.
- [class NSGlyphInfo](nsglyphinfo.md)
  A glyph attribute in an attributed string.
- [Reserved Glyph Codes](reserved-glyph-codes.md)
  These constants define reserved glyph codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontrenderingmode)*