# numberOfGlyphs

**Framework**: AppKit  
**Kind**: property

The number of glyphs in the layout manager.

**Availability**:
- macOS 10.7+

## Declaration

```swift
var numberOfGlyphs: Int { get }
```

## See Also

- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>?, properties: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes: UnsafeMutablePointer<Int>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](nslayoutmanager/getglyphs(in:glyphs:properties:characterindexes:bidilevels:).md)
  Fills a passed-in buffer with a sequence of glyphs.
- [func cgGlyph(at: Int) -> CGGlyph](nslayoutmanager/cgglyph(at:).md)
  Returns the glyph at the specified index.
- [func cgGlyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](nslayoutmanager/cgglyph(at:isvalidindex:).md)
  Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [func setGlyphs(UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange)](nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:).md)
  Stores the initial glyphs and glyph properties for a character range.
- [func characterIndexForGlyph(at: Int) -> Int](nslayoutmanager/characterindexforglyph(at:).md)
  Returns the index in the text storage for the first character of the specified glyph.
- [func glyphIndexForCharacter(at: Int) -> Int](nslayoutmanager/glyphindexforcharacter(at:).md)
  Returns the index of the first glyph of the character at the specified index.
- [func isValidGlyphIndex(Int) -> Bool](nslayoutmanager/isvalidglyphindex(_:).md)
  Indicates whether the specified index refers to a valid glyph.
- [func propertyForGlyph(at: Int) -> NSLayoutManager.GlyphProperty](nslayoutmanager/propertyforglyph(at:).md)
  Returns the glyph property of the glyph at the specified index.
- [NSLayoutManager.GlyphProperty](nslayoutmanager/glyphproperty.md)
  Glyph properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/numberofglyphs)*