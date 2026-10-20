# NSFontRenderingMode

**Framework**: AppKit  
**Kind**: enum  
**Role**: Enumeration

The font rendering mode.

**Availability**:
- macOS

## Declaration

```swift
enum NSFontRenderingMode
```

```c
enum NSFontRenderingMode : NSUInteger;
```

## Topics

### Constants
- [NSFontRenderingMode.defaultRenderingMode](./nsfontrenderingmode/defaultrenderingmode.md)
  Determines the actual mode based on the user preference settings.
- [NSFontRenderingMode.antialiasedRenderingMode](./nsfontrenderingmode/antialiasedrenderingmode.md)
  Specifies antialiased, floating-point advancements rendering mode (synonymous with printerFont).
- [NSFontRenderingMode.integerAdvancementsRenderingMode](./nsfontrenderingmode/integeradvancementsrenderingmode.md)
  Specifies integer advancements rendering mode.
- [NSFontRenderingMode.antialiasedIntegerAdvancementsRenderingMode](./nsfontrenderingmode/antialiasedintegeradvancementsrenderingmode.md)
  Specifies antialiased, integer advancements rendering mode.
### Initializers
- [init?(rawValue: UInt)](./nsfontrenderingmode/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Glyphs
- [typealias NSGlyph](./nsglyph.md)
  The type used to specify glyphs.
- [protocol NSGlyphStorage](./nsglyphstorage.md)
  A set of methods that a glyph storage object must implement to interact properly with [`NSGlyphGenerator`](./nsglyphgenerator.md).
- [class NSGlyphGenerator](./nsglyphgenerator.md)
  An object that performs the initial, nominal glyph generation phase in the layout process.
- [class NSGlyphInfo](./nsglyphinfo.md)
  A glyph attribute in an attributed string.
- [Reserved Glyph Codes](./reserved-glyph-codes.md)
  These constants define reserved glyph codes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfontrenderingmode)*