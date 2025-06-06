# descent

**Framework**: Core Graphics  
**Kind**: property

Returns the descent of a font.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS ?+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var descent: Int32 { get }
```

#### Discussion

The descent is the maximum distance below the baseline of glyphs in a font. The value is specified in glyph space units.

## See Also

- [var ascent: Int32](cgfont/ascent.md)
  Returns the ascent of a font.
- [var capHeight: Int32](cgfont/capheight.md)
  Returns the cap height of a font.
- [var fontBBox: CGRect](cgfont/fontbbox.md)
  Returns the bounding box of a font.
- [var italicAngle: CGFloat](cgfont/italicangle.md)
  Returns the italic angle of a font.
- [var leading: Int32](cgfont/leading.md)
  Returns the leading of a font.
- [var stemV: CGFloat](cgfont/stemv.md)
  Returns the thickness of the dominant vertical stems of glyphs in a font.
- [var unitsPerEm: Int32](cgfont/unitsperem.md)
  Returns the number of glyph space units per em for the provided font.
- [var xHeight: Int32](cgfont/xheight.md)
  Returns the x-height of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/descent)*