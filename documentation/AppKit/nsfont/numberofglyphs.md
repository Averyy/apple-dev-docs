# numberOfGlyphs

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The number of glyphs in the font.

**Availability**:
- macOS

## Declaration

```swift
var numberOfGlyphs: Int { get }
```

```objc
@property (readonly) NSUInteger numberOfGlyphs;
```

## Discussion

Glyphs are numbered starting at 0.

## See Also

### Getting Information About Glyphs
- [typealias NSGlyph](../nsglyph.md)
  The type used to specify glyphs.
- [var NSControlGlyph: Int](../nscontrolglyph.md)
  The reserved code for a control glyph.
- [var NSNullGlyph: Int](../nsnullglyph.md)
  The reserved code for a null glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nsfont/numberofglyphs)*