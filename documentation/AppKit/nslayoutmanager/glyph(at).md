# glyph(at:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the glyph at the specified index.

**Availability**:
- macOS

> **Deprecated**: Use [`cgGlyph(at:)`](./cgglyph%28at%29.md) instead.

## Declaration

```swift
func glyph(at glyphIndex: Int) -> NSGlyph
```

```objc
- (NSGlyph) glyphAtIndex:(NSUInteger) glyphIndex;
```

## Return Value

The glyph at `glyphIndex`.

## Discussion

Raises an `NSRangeException` if `glyphIndex` is out of bounds.

Performs glyph generation if needed. To avoid an exception with [`glyph(at:)`](./glyph%28at%29.md) you must first check the glyph index against the number of glyphs, which requires generating all glyphs. Another method, [`glyph(at:isValidIndex:)`](./glyph%28at,isvalidindex%29.md), generates glyphs only up to the one requested, so using it can be more efficient.

## Parameters

- `glyphIndex`: The index of a glyph in the receiver. This value must not exceed the bounds of the receiver’s glyph array.

## See Also

### Deprecated methods
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<NSPoint>, count: Int, font: NSFont, matrix: AffineTransform, attributes: [NSAttributedString.Key : Any], in: NSGraphicsContext)](./showcgglyphs%28_,positions,count,font,matrix,attributes,in%29.md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func invalidateGlyphs(onLayoutInvalidationForGlyphRange: NSRange)](./invalidateglyphs%28onlayoutinvalidationforglyphrange%29.md)
  Specifies explicitly when portions of the glyph stream depend on layout.
- [func invalidateLayout(forCharacterRange: NSRange, isSoft: Bool, actualCharacterRange: NSRangePointer?)](./invalidatelayout%28forcharacterrange,issoft,actualcharacterrange%29.md)
  Invalidates the layout information for the glyphs mapped to the given range of characters.
- [func textStorage(NSTextStorage, edited: Int, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](./textstorage%28_,edited,range,changeinlength,invalidatedrange%29.md)
  Invalidates glyph and layout information for a portion of the text in the given text storage object.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](./insertglyph%28_,atglyphindex,characterindex%29.md)
  Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index.
- [func insertGlyphs(UnsafePointer<NSGlyph>, length: Int, forStartingGlyphAt: Int, characterIndex: Int)](./insertglyphs%28_,length,forstartingglyphat,characterindex%29.md)
  Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index.
- [func glyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> NSGlyph](./glyph%28at,isvalidindex%29.md)
  Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid.
- [func replaceGlyph(at: Int, withGlyph: NSGlyph)](./replaceglyph%28at,withglyph%29.md)
  Replaces the glyph at the given index with a new glyph.
- [func getGlyphs(UnsafeMutablePointer<NSGlyph>?, range: NSRange) -> Int](./getglyphs%28_,range%29.md)
  Fills the passed-in buffer with a sequence of glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>?, characterIndexes: UnsafeMutablePointer<Int>?, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits: UnsafeMutablePointer<ObjCBool>?) -> Int](./getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits%29.md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>?, characterIndexes: UnsafeMutablePointer<Int>?, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits: UnsafeMutablePointer<ObjCBool>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](./getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits,bidilevels%29.md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func deleteGlyphs(in: NSRange)](./deleteglyphs%28in%29.md)
  Deletes the glyphs in the given range from the receiver’s glyph store.
- [func setCharacterIndex(Int, forGlyphAt: Int)](./setcharacterindex%28_,forglyphat%29.md)
  Sets the index of the character corresponding to the glyph at the given glyph index.
- [func intAttribute(Int, forGlyphAt: Int) -> Int](./intattribute%28_,forglyphat%29.md)
  Returns the value of the attribute identified by the given attribute tag for the glyph at the given index.
- [func setIntAttribute(Int, value: Int, forGlyphAt: Int)](./setintattribute%28_,value,forglyphat%29.md)
  Sets a custom attribute value for a given glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyph(at:))*