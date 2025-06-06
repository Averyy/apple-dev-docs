# kCGFontIndexInvalid

**Framework**: Core Graphics  
**Kind**: var

An invalid font index (a value which never represents a valid glyph).

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
let kCGFontIndexInvalid: CGFontIndex
```

## See Also

- [var numberOfGlyphs: Int](cgfont/numberofglyphs.md)
  Returns the number of glyphs in a font.
- [func name(for: CGGlyph) -> CFString?](cgfont/name(for:).md)
  Returns the glyph name of the specified glyph in the specified font.
- [func getGlyphWithGlyphName(name: CFString) -> CGGlyph](cgfont/getglyphwithglyphname(name:).md)
  Returns the glyph for the glyph name associated with the specified font object.
- [func getGlyphBBoxes(glyphs: UnsafePointer<CGGlyph>, count: Int, bboxes: UnsafeMutablePointer<CGRect>) -> Bool](cgfont/getglyphbboxes(glyphs:count:bboxes:).md)
  Get the bounding box of each glyph in an array.
- [func getGlyphAdvances(glyphs: UnsafePointer<CGGlyph>, count: Int, advances: UnsafeMutablePointer<Int32>) -> Bool](cgfont/getglyphadvances(glyphs:count:advances:).md)
  Gets the advance width of each glyph in the provided array.
- [typealias CGGlyph](cgglyph.md)
  An index into the internal glyph table of a font.
- [let kCGGlyphMax: CGFontIndex](kcgglyphmax.md)
  The maximum allowed value of a [`CGGlyph`](cgglyph.md).
- [typealias CGFontIndex](cgfontindex.md)
  An index into a font table.
- [let kCGFontIndexMax: CGFontIndex](kcgfontindexmax.md)
  The maximum allowed value of a [`CGFontIndex`](cgfontindex.md).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/kcgfontindexinvalid)*