# invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:)

**Framework**: AppKit  
**Kind**: method

Invalidates the layout information for the glyphs mapped to the given range of characters.

**Availability**:
- macOS 10.0+

## Declaration

```swift
func invalidateLayout(forCharacterRange charRange: NSRange, isSoft flag: Bool, actualCharacterRange actualCharRange: NSRangePointer?)
```

#### Discussion

This method only invalidates information; it performs no glyph generation or layout. You should rarely need to invoke this method.

For code that needs to work on both OS X v10.5 and previous releases, the following procedures should be used. For OS X v10.4 and before, invalidation should consist of

1. Calling this method with the `flag` set to [`true`](https://developer.apple.com/documentation/Swift/true), for the range that has actually become invalid.
2. Calling this method with the `flag` set to [`false`](https://developer.apple.com/documentation/Swift/false), for the range (if any) that follows that range, usually extending to the end of the text, that might need to be moved due to relayout of the invalidated range.

As of OS X v10.5, the semantics of the `flag` parameter are slightly different. Soft layout holes are obsolete in macOS 10.5 and later, so the flag is no longer necessary. If the method is called with `flag` set to [`false`](https://developer.apple.com/documentation/Swift/false), then it has the effect of invalidating layout.  If it’s called with the `flag` set to [`true`](https://developer.apple.com/documentation/Swift/true), then it does not actually invalidate layout; it invalidates a number of internal caches, but otherwise has no effect, and in general is unnecessary.

This method is superseded by [`invalidateLayout(forCharacterRange:actualCharacterRange:)`](nslayoutmanager/invalidatelayout(forcharacterrange:actualcharacterrange:).md) and will be deprecated in a future release.

## Parameters

- `charRange`: The character range for which glyphs are invalidated.
- `flag`: If  , invalidates internal caches in the layout manager; if  , invalidates layout. See the discussion section.
- `actualCharRange`: If not  , on output, the range of characters mapped to the glyphs whose layout information is invalidated. This range can be larger than the range of characters given due to the effect of context on glyphs and layout.

## See Also

- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<NSPoint>, count: Int, font: NSFont, matrix: AffineTransform, attributes: [NSAttributedString.Key : Any], in: NSGraphicsContext)](nslayoutmanager/showcgglyphs(_:positions:count:font:matrix:attributes:in:).md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func invalidateGlyphs(onLayoutInvalidationForGlyphRange: NSRange)](nslayoutmanager/invalidateglyphs(onlayoutinvalidationforglyphrange:).md)
  Specifies explicitly when portions of the glyph stream depend on layout.
- [func textStorage(NSTextStorage, edited: Int, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](nslayoutmanager/textstorage(_:edited:range:changeinlength:invalidatedrange:).md)
  Invalidates glyph and layout information for a portion of the text in the given text storage object.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](nslayoutmanager/insertglyph(_:atglyphindex:characterindex:).md)
  Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index.
- [func insertGlyphs(UnsafePointer<NSGlyph>, length: Int, forStartingGlyphAt: Int, characterIndex: Int)](nslayoutmanager/insertglyphs(_:length:forstartingglyphat:characterindex:).md)
  Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index.
- [func glyph(at: Int) -> NSGlyph](nslayoutmanager/glyph(at:).md)
  Returns the glyph at the specified index.
- [func glyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> NSGlyph](nslayoutmanager/glyph(at:isvalidindex:).md)
  Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid.
- [func replaceGlyph(at: Int, withGlyph: NSGlyph)](nslayoutmanager/replaceglyph(at:withglyph:).md)
  Replaces the glyph at the given index with a new glyph.
- [func getGlyphs(UnsafeMutablePointer<NSGlyph>?, range: NSRange) -> Int](nslayoutmanager/getglyphs(_:range:).md)
  Fills the passed-in buffer with a sequence of glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>?, characterIndexes: UnsafeMutablePointer<Int>?, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits: UnsafeMutablePointer<ObjCBool>?) -> Int](nslayoutmanager/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:).md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>?, characterIndexes: UnsafeMutablePointer<Int>?, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits: UnsafeMutablePointer<ObjCBool>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](nslayoutmanager/getglyphs(in:glyphs:characterindexes:glyphinscriptions:elasticbits:bidilevels:).md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func deleteGlyphs(in: NSRange)](nslayoutmanager/deleteglyphs(in:).md)
  Deletes the glyphs in the given range from the receiver’s glyph store.
- [func setCharacterIndex(Int, forGlyphAt: Int)](nslayoutmanager/setcharacterindex(_:forglyphat:).md)
  Sets the index of the character corresponding to the glyph at the given glyph index.
- [func intAttribute(Int, forGlyphAt: Int) -> Int](nslayoutmanager/intattribute(_:forglyphat:).md)
  Returns the value of the attribute identified by the given attribute tag for the glyph at the given index.
- [func setIntAttribute(Int, value: Int, forGlyphAt: Int)](nslayoutmanager/setintattribute(_:value:forglyphat:).md)
  Sets a custom attribute value for a given glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/invalidatelayout(forcharacterrange:issoft:actualcharacterrange:))*