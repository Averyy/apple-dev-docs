# CGGlyph

**Framework**: Core Graphics  
**Kind**: typealias

An index into the internal glyph table of a font.

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
typealias CGGlyph = CGFontIndex
```

#### Discussion

When drawing text, you typically specify a sequence of characters. However, Core Graphics also allows you to use [`CGGlyph`](cgglyph.md) values to specify glyphs. In either case, Core Graphics renders the text using font data provided by the Apple Type Services (ATS) framework.

You provide [`CGGlyph`](cgglyph.md) values to the functions [`showGlyphs(g:count:)`](cgcontext/showglyphs(g:count:).md) and [`showGlyphsAtPoint(x:y:glyphs:count:)`](cgcontext/showglyphsatpoint(x:y:glyphs:count:).md). These functions display an array of glyphs at the current text position or at a position you specify, respectively.

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
- [let kCGGlyphMax: CGFontIndex](kcgglyphmax.md)
  The maximum allowed value of a [`CGGlyph`](cgglyph.md).
- [typealias CGFontIndex](cgfontindex.md)
  An index into a font table.
- [let kCGFontIndexMax: CGFontIndex](kcgfontindexmax.md)
  The maximum allowed value of a [`CGFontIndex`](cgfontindex.md).
- [let kCGFontIndexInvalid: CGFontIndex](kcgfontindexinvalid.md)
  An invalid font index (a value which never represents a valid glyph).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgglyph)*