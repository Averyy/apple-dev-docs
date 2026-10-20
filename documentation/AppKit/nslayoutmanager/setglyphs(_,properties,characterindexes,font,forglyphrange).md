# setGlyphs(_:properties:characterIndexes:font:forGlyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Stores the initial glyphs and glyph properties for a character range.

**Availability**:
- macOS 10.11+

## Declaration

```swift
func setGlyphs(_ glyphs: UnsafePointer<CGGlyph>, properties props: UnsafePointer<NSLayoutManager.GlyphProperty>, characterIndexes charIndexes: UnsafePointer<Int>, font aFont: NSFont, forGlyphRange glyphRange: NSRange)
```

```objc
- (void) setGlyphs:(const CGGlyph *) glyphs properties:(const NSGlyphProperty *) props characterIndexes:(const NSUInteger *) charIndexes font:(NSFont *) aFont forGlyphRange:(NSRange) glyphRange;
```

#### Discussion

This method is invoked by text system during the glyph generation process. The only place apps are allowed to call this method directly is from an implementation of the `NSLayoutManagerDelegate` protocol method [`layoutManager(_:shouldGenerateGlyphs:properties:characterIndexes:font:forGlyphRange:)`](../nslayoutmanagerdelegate/layoutmanager%28_,shouldgenerateglyphs,properties,characterindexes,font,forglyphrange%29.md).

Each array has `glyphRange.length` items. The specified `charIndexes` must be contiguous (no skipped indexes), enabling multiple items to have a same character index (as when one character index generates multiple glyph IDs). Due to font substitution, `aFont` passed into this method might not match the font in the attributes dictionary. Calling this method for a character range that has previously calculated layout information invalidates the layout and display.

## Parameters

- `glyphs`: A pointer to the layout manager’s glyph cache.
- `props`: A pointer to a buffer containing glyph properties for the glyphs in the cache.
- `charIndexes`: A pointer to the starting index for the characters in the text storage for which glyphs are generated.
- `aFont`: A font to override the font attributes in the text storage for the specified character range.
- `glyphRange`: The range of glyphs in the glyph cache to set.

## See Also

### Accessing glyphs
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<CGGlyph>?, properties: UnsafeMutablePointer<NSLayoutManager.GlyphProperty>?, characterIndexes: UnsafeMutablePointer<Int>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](./getglyphs%28in,glyphs,properties,characterindexes,bidilevels%29.md)
  Fills a passed-in buffer with a sequence of glyphs.
- [func cgGlyph(at: Int) -> CGGlyph](./cgglyph%28at%29.md)
  Returns the glyph at the specified index.
- [func cgGlyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](./cgglyph%28at,isvalidindex%29.md)
  Returns the glyph at the specified index along with information about whether the glyph index is valid.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setglyphs(_:properties:characterindexes:font:forglyphrange:))*