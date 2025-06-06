# characterIndexForGlyph(at:)

**Framework**: AppKit  
**Kind**: method

Returns the index in the text storage for the first character of the specified glyph.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func characterIndexForGlyph(at glyphIndex: Int) -> Int
```

#### Return Value

The index of the first character associated with the glyph at the specified index.

#### Discussion

If noncontiguous layout is not enabled, this method causes generation of all glyphs up to and including `glyphIndex`. This method accepts an index beyond the last glyph, returning an index extrapolated from the last actual glyph index.

In many cases it’s better to use the range-mapping methods, [`characterRange(forGlyphRange:actualGlyphRange:)`](nslayoutmanager/characterrange(forglyphrange:actualglyphrange:).md) and [`glyphRange(forCharacterRange:actualCharacterRange:)`](nslayoutmanager/glyphrange(forcharacterrange:actualcharacterrange:).md), which provide more comprehensive information.

## Parameters

- `glyphIndex`: The index of the glyph for which to return the associated character.

## See Also

- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>?, properties: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes: UnsafeMutablePointer<Int>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](nslayoutmanager/getglyphs(in:glyphs:properties:characterindexes:bidilevels:).md)
  Fills a passed-in buffer with a sequence of glyphs.
- [func cgGlyph(at: Int) -> CGGlyph](nslayoutmanager/cgglyph(at:).md)
  Returns the glyph at the specified index.
- [func cgGlyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](nslayoutmanager/cgglyph(at:isvalidindex:).md)
  Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [func setGlyphs(UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange)](nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:).md)
  Stores the initial glyphs and glyph properties for a character range.
- [func glyphIndexForCharacter(at: Int) -> Int](nslayoutmanager/glyphindexforcharacter(at:).md)
  Returns the index of the first glyph of the character at the specified index.
- [func isValidGlyphIndex(Int) -> Bool](nslayoutmanager/isvalidglyphindex(_:).md)
  Indicates whether the specified index refers to a valid glyph.
- [var numberOfGlyphs: Int](nslayoutmanager/numberofglyphs.md)
  The number of glyphs in the layout manager.
- [func propertyForGlyph(at: Int) -> NSLayoutManager.GlyphProperty](nslayoutmanager/propertyforglyph(at:).md)
  Returns the glyph property of the glyph at the specified index.
- [NSLayoutManager.GlyphProperty](nslayoutmanager/glyphproperty.md)
  Glyph properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/characterindexforglyph(at:))*