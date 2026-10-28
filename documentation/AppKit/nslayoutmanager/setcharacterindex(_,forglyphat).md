# setCharacterIndex(_:forGlyphAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the index of the character corresponding to the glyph at the given glyph index.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use -setGlyphs:properties:characterIndexes:font:forGlyphRange instead

## Declaration

```swift
func setCharacterIndex(_ charIndex: Int, forGlyphAt glyphIndex: Int)
```

```objc
- (void) setCharacterIndex:(NSUInteger) charIndex forGlyphAtIndex:(NSUInteger) glyphIndex;
```

## Discussion

This method is for use by the glyph-generation mechanism and doesn’t perform any invalidation or generation of the glyphs or layout. This method should be invoked only during glyph generation and typesetting, in almost all cases only by the glyph generator or typesetter. For example, a custom glyph generator or typesetter might invoke it.

## Parameters

- `charIndex`: The index to set.
- `glyphIndex`: The glyph corresponding to the character whose index is set. The glyph must already be present.

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
- [func glyph(at: Int) -> NSGlyph](./glyph%28at%29.md)
  Returns the glyph at the specified index.
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
- [func intAttribute(Int, forGlyphAt: Int) -> Int](./intattribute%28_,forglyphat%29.md)
  Returns the value of the attribute identified by the given attribute tag for the glyph at the given index.
- [func setIntAttribute(Int, value: Int, forGlyphAt: Int)](./setintattribute%28_,value,forglyphat%29.md)
  Sets a custom attribute value for a given glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setcharacterindex(_:forglyphat:))*