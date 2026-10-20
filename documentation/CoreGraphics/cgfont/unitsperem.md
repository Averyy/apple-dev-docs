# unitsPerEm

**Framework**: Core Graphics  
**Kind**: property  
**Role**: Instance Property

Returns the number of glyph space units per em for the provided font.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.1+
- macOS 10.0+
- tvOS
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var unitsPerEm: Int32 { get }
```

```c
extern int CGFontGetUnitsPerEm(CGFontRef font);
```

## See Also

### Examining Font Metrics
- [var ascent: Int32](./ascent.md)
  Returns the ascent of a font.
- [var capHeight: Int32](./capheight.md)
  Returns the cap height of a font.
- [var descent: Int32](./descent.md)
  Returns the descent of a font.
- [var fontBBox: CGRect](./fontbbox.md)
  Returns the bounding box of a font.
- [var italicAngle: CGFloat](./italicangle.md)
  Returns the italic angle of a font.
- [var leading: Int32](./leading.md)
  Returns the leading of a font.
- [var stemV: CGFloat](./stemv.md)
  Returns the thickness of the dominant vertical stems of glyphs in a font.
- [var xHeight: Int32](./xheight.md)
  Returns the x-height of a font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgfont/unitsperem)*