# NSControlGlyph

**Framework**: AppKit  
**Kind**: var  
**Role**: Global Variable

The reserved code for a control glyph.

**Availability**:
- macOS

## Declaration

```swift
var NSControlGlyph: Int { get }
```

```c
NSControlGlyph
```

## Discussion

An [`NSGlyphGenerator`](./nsglyphgenerator.md) objects generates [`NSControlGlyph`](./nscontrolglyph.md) for all characters in the Unicode General Category C* and U200B (ZERO WIDTH SPACE).

## See Also

### Getting Information About Glyphs
- [var numberOfGlyphs: Int](./nsfont/numberofglyphs.md)
  The number of glyphs in the font.
- [typealias NSGlyph](./nsglyph.md)
  The type used to specify glyphs.
- [var NSNullGlyph: Int](./nsnullglyph.md)
  The reserved code for a null glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nscontrolglyph)*