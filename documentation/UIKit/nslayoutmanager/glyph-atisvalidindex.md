# glyph(at:isValidIndex:)

**Framework**: UIKit  
**Kind**: method

Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+

## Declaration

```swift
func glyph(at glyphIndex: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph
```

#### Return Value

The glyph at the requested index, or `NSNullGlyph` if the requested index is out of the range `{ 0,` [`numberOfGlyphs`](nslayoutmanager/numberofglyphs.md) `}`.

#### Discussion

If noncontiguous layout is not enabled, this method causes generation of all glyphs up to and including `glyphIndex`.

## Parameters

- `glyphIndex`: The index of the glyph to be returned.
- `isValidIndex`: If not  , on output,   if the requested index is in range; otherwise  .

## See Also

- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: UIFont, matrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](nslayoutmanager/showcgglyphs(_:positions:count:font:matrix:attributes:in:).md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func invalidateGlyphs(onLayoutInvalidationForGlyphRange: NSRange)](../AppKit/NSLayoutManager/invalidateGlyphs(onLayoutInvalidationForGlyphRange:).md)
  Specifies explicitly when portions of the glyph stream depend on layout.
- [func invalidateLayout(forCharacterRange: NSRange, isSoft: Bool, actualCharacterRange: NSRangePointer?)](../AppKit/NSLayoutManager/invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:).md)
  Invalidates the layout information for the glyphs mapped to the given range of characters.
- [func textStorage(NSTextStorage, edited: Int, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](../AppKit/NSLayoutManager/textStorage(_:edited:range:changeInLength:invalidatedRange:).md)
  Invalidates glyph and layout information for a portion of the text in the given text storage object.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](../AppKit/NSLayoutManager/insertGlyph(_:atGlyphIndex:characterIndex:).md)
  Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index.
- [func insertGlyphs(UnsafePointer<NSGlyph>, length: Int, forStartingGlyphAt: Int, characterIndex: Int)](../AppKit/NSLayoutManager/insertGlyphs(_:length:forStartingGlyphAt:characterIndex:).md)
  Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index.
- [func glyph(at: Int) -> CGGlyph](nslayoutmanager/glyph(at:).md)
  Returns the glyph at the specified index.
- [func replaceGlyph(at: Int, withGlyph: NSGlyph)](../AppKit/NSLayoutManager/replaceGlyph(at:withGlyph:).md)
  Replaces the glyph at the given index with a new glyph.
- [func getGlyphs(UnsafeMutablePointer<NSGlyph>?, range: NSRange) -> Int](../AppKit/NSLayoutManager/getGlyphs(_:range:).md)
  Fills the passed-in buffer with a sequence of glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>?, characterIndexes: UnsafeMutablePointer<Int>?, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits: UnsafeMutablePointer<ObjCBool>?) -> Int](../AppKit/NSLayoutManager/getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:).md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>?, characterIndexes: UnsafeMutablePointer<Int>?, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits: UnsafeMutablePointer<ObjCBool>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](../AppKit/NSLayoutManager/getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:).md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func deleteGlyphs(in: NSRange)](../AppKit/NSLayoutManager/deleteGlyphs(in:).md)
  Deletes the glyphs in the given range from the receiver’s glyph store.
- [func setCharacterIndex(Int, forGlyphAt: Int)](../AppKit/NSLayoutManager/setCharacterIndex(_:forGlyphAt:).md)
  Sets the index of the character corresponding to the glyph at the given glyph index.
- [func intAttribute(Int, forGlyphAt: Int) -> Int](../AppKit/NSLayoutManager/intAttribute(_:forGlyphAt:).md)
  Returns the value of the attribute identified by the given attribute tag for the glyph at the given index.
- [func setIntAttribute(Int, value: Int, forGlyphAt: Int)](../AppKit/NSLayoutManager/setIntAttribute(_:value:forGlyphAt:).md)
  Sets a custom attribute value for a given glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/glyph(at:isvalidindex:))*