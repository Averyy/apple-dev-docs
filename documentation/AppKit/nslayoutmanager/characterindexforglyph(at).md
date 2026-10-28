# characterIndexForGlyph(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the index in the text storage for the first character of the specified glyph.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func characterIndexForGlyph(at glyphIndex: Int) -> Int
```

```objc
- (NSUInteger) characterIndexForGlyphAtIndex:(NSUInteger) glyphIndex;
```

## Return Value

The index of the first character associated with the glyph at the specified index.

## Discussion

If noncontiguous layout is not enabled, this method causes generation of all glyphs up to and including `glyphIndex`. This method accepts an index beyond the last glyph, returning an index extrapolated from the last actual glyph index.

In many cases it’s better to use the range-mapping methods, [`characterRange(forGlyphRange:actualGlyphRange:)`](./characterrange%28forglyphrange,actualglyphrange%29.md) and [`glyphRange(forCharacterRange:actualCharacterRange:)`](./glyphrange%28forcharacterrange,actualcharacterrange%29.md), which provide more comprehensive information.

## Parameters

- `glyphIndex`: The index of the glyph for which to return the associated character.

## See Also

### Accessing glyphs
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>?, properties: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes: UnsafeMutablePointer<Int>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](./getglyphs%28in,glyphs,properties,characterindexes,bidilevels%29.md)
  Fills a passed-in buffer with a sequence of glyphs.
- [func cgGlyph(at: Int) -> CGGlyph](./cgglyph%28at%29.md)
  Returns the glyph at the specified index.
- [func cgGlyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](./cgglyph%28at,isvalidindex%29.md)
  Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [func setGlyphs(UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange)](./setglyphs%28_,properties,characterindexes,font,forglyphrange%29.md)
  Stores the initial glyphs and glyph properties for a character range.
- [func glyphIndexForCharacter(at: Int) -> Int](./glyphindexforcharacter%28at%29.md)
  Returns the index of the first glyph of the character at the specified index.
- [func isValidGlyphIndex(Int) -> Bool](./isvalidglyphindex%28_%29.md)
  Indicates whether the specified index refers to a valid glyph.
- [var numberOfGlyphs: Int](./numberofglyphs.md)
  The number of glyphs in the layout manager.
- [func propertyForGlyph(at: Int) -> NSLayoutManager.GlyphProperty](./propertyforglyph%28at%29.md)
  Returns the glyph property of the glyph at the specified index.
- [NSLayoutManager.GlyphProperty](./glyphproperty.md)
  Glyph properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/characterindexforglyph(at:))*