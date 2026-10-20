# CGGlyph

**Framework**: Core Graphics  
**Kind**: typealias  
**Role**: Type Alias

An index into the internal glyph table of a font.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
typealias CGGlyph = CGFontIndex
```

```c
typedef CGFontIndex CGGlyph;
```

#### Discussion

When drawing text, you typically specify a sequence of characters. However, Core Graphics also allows you to use [`CGGlyph`](./cgglyph.md) values to specify glyphs. In either case, Core Graphics renders the text using font data provided by the Apple Type Services (ATS) framework.

You provide [`CGGlyph`](./cgglyph.md) values to the functions [`showGlyphs(g:count:)`](./cgcontext/showglyphs%28g,count%29.md) and [`showGlyphsAtPoint(x:y:glyphs:count:)`](./cgcontext/showglyphsatpoint%28x,y,glyphs,count%29.md). These functions display an array of glyphs at the current text position or at a position you specify, respectively.

## See Also

### Working with Glyphs
- [var numberOfGlyphs: Int](./cgfont/numberofglyphs.md)
  Returns the number of glyphs in a font.
- [func name(for: CGGlyph) -> CFString?](./cgfont/name%28for%29.md)
  Returns the glyph name of the specified glyph in the specified font.
- [func getGlyphWithGlyphName(name: CFString) -> CGGlyph](./cgfont/getglyphwithglyphname%28name%29.md)
  Returns the glyph for the glyph name associated with the specified font object.
- [func getGlyphBBoxes(glyphs: UnsafePointer<CGGlyph>, count: Int, bboxes: UnsafeMutablePointer<CGRect>) -> Bool](./cgfont/getglyphbboxes%28glyphs,count,bboxes%29.md)
  Get the bounding box of each glyph in an array.
- [func getGlyphAdvances(glyphs: UnsafePointer<CGGlyph>, count: Int, advances: UnsafeMutablePointer<Int32>) -> Bool](./cgfont/getglyphadvances%28glyphs,count,advances%29.md)
  Gets the advance width of each glyph in the provided array.
- [var kCGGlyphMax: CGFontIndex](./kcgglyphmax.md)
  The maximum allowed value of a [`CGGlyph`](./cgglyph.md).
- [typealias CGFontIndex](./cgfontindex.md)
  An index into a font table.
- [var kCGFontIndexMax: CGFontIndex](./kcgfontindexmax.md)
  The maximum allowed value of a [`CGFontIndex`](./cgfontindex.md).
- [var kCGFontIndexInvalid: CGFontIndex](./kcgfontindexinvalid.md)
  An invalid font index (a value which never represents a valid glyph).


---

*[View on Apple Developer](https://developer.apple.com/documentation/coregraphics/cgglyph)*