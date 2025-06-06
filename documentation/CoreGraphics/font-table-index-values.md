# Font Table Index Values

**Framework**: Core Graphics

Possible values for an index into a font table.

#### Overview

See [`CGFontIndex`](cgfontindex.md).

## Topics

### Constants
- [let kCGFontIndexMax: CGFontIndex](kcgfontindexmax.md)
  The maximum allowed value of a [`CGFontIndex`](cgfontindex.md).
- [let kCGFontIndexInvalid: CGFontIndex](kcgfontindexinvalid.md)
  An invalid font index (a value which never represents a valid glyph).
- [let kCGGlyphMax: CGFontIndex](kcgglyphmax.md)
  The maximum allowed value of a [`CGGlyph`](cgglyph.md).

## See Also

- [var tableTags: CFArray?](cgfont/tabletags.md)
  Returns an array of tags that correspond to the font tables for a font.
- [func table(for: UInt32) -> CFData?](cgfont/table(for:).md)
  Returns the font table that corresponds to the provided tag.
- [Obsolete Font Table Index Values](obsolete-font-table-index-values.md)
  Deprecated values for an index into a font table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/font-table-index-values)*