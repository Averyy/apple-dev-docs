# isValidGlyphIndex(_:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Indicates whether the specified index refers to a valid glyph.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func isValidGlyphIndex(_ glyphIndex: Int) -> Bool
```

```objc
- (BOOL) isValidGlyphIndex:(NSUInteger) glyphIndex;
```

## Return Value

[`true`](../../Swift/true.md) if the specified `glyphIndex` refers to a valid glyph, otherwise [`false`](../../Swift/false.md).

## Parameters

- `glyphIndex`: The index of a glyph in the receiver.

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
- [func characterIndexForGlyph(at: Int) -> Int](./characterindexforglyph%28at%29.md)
  Returns the index in the text storage for the first character of the specified glyph.
- [func glyphIndexForCharacter(at: Int) -> Int](./glyphindexforcharacter%28at%29.md)
  Returns the index of the first glyph of the character at the specified index.
- [var numberOfGlyphs: Int](./numberofglyphs.md)
  The number of glyphs in the layout manager.
- [func propertyForGlyph(at: Int) -> NSLayoutManager.GlyphProperty](./propertyforglyph%28at%29.md)
  Returns the glyph property of the glyph at the specified index.
- [NSLayoutManager.GlyphProperty](./glyphproperty.md)
  Glyph properties.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/isvalidglyphindex(_:))*