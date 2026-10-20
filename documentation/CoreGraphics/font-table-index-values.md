# Font Table Index Values

**Framework**: Core Graphics  
**Role**: API Collection

Possible values for an index into a font table.

#### Overview

See [`CGFontIndex`](./cgfontindex.md).

## Topics

### Constants
- [var kCGFontIndexMax: CGFontIndex](./kcgfontindexmax.md)
  The maximum allowed value of a [`CGFontIndex`](./cgfontindex.md).
- [var kCGFontIndexInvalid: CGFontIndex](./kcgfontindexinvalid.md)
  An invalid font index (a value which never represents a valid glyph).
- [var kCGGlyphMax: CGFontIndex](./kcgglyphmax.md)
  The maximum allowed value of a [`CGGlyph`](./cgglyph.md).

## See Also

### Working with Font Tables
- [var tableTags: CFArray?](./cgfont/tabletags.md)
  Returns an array of tags that correspond to the font tables for a font.
- [func table(for: UInt32) -> CFData?](./cgfont/table%28for%29.md)
  Returns the font table that corresponds to the provided tag.
- [Obsolete Font Table Index Values](./obsolete-font-table-index-values.md)
  Deprecated values for an index into a font table.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/font-table-index-values)*