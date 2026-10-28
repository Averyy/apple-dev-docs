# cgGlyph(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the glyph at the specified index.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func cgGlyph(at glyphIndex: Int) -> CGGlyph
```

```objc
- (CGGlyph) CGGlyphAtIndex:(NSUInteger) glyphIndex;
```

## Return Value

The glyph at the specified index.

## Discussion

Calling this method generates all of the glyphs (as needed) up to and including the glyph at the specified index.

## Parameters

- `glyphIndex`: The index of the glyph that you want. If the index is out of range, this method raises an exception with the error [`rangeException`](../../Foundation/nsexceptionname/rangeexception.md).

## See Also

### Accessing glyphs
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>?, properties: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes: UnsafeMutablePointer<Int>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](./getglyphs%28in,glyphs,properties,characterindexes,bidilevels%29.md)
  Fills a passed-in buffer with a sequence of glyphs.
- [func cgGlyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](./cgglyph%28at,isvalidindex%29.md)
  Returns the glyph at the specified index along with information about whether the glyph index is valid.
- [func setGlyphs(UnsafePointer<CGGlyph>, properties: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes: UnsafePointer<Int>, font: NSFont, forGlyphRange: NSRange)](./setglyphs%28_,properties,characterindexes,font,forglyphrange%29.md)
  Stores the initial glyphs and glyph properties for a character range.
- [func characterIndexForGlyph(at: Int) -> Int](./characterindexforglyph%28at%29.md)
  Returns the index in the text storage for the first character of the specified glyph.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/cgglyph(at:))*