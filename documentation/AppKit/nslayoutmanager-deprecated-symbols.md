# Deprecated Symbols

**Framework**: AppKit

Review unsupported symbols and their replacements.

## Topics

### Methods
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<NSPoint>, count: Int, font: NSFont, matrix: AffineTransform, attributes: [NSAttributedString.Key : Any], in: NSGraphicsContext)](nslayoutmanager/showcgglyphs(_:positions:count:font:matrix:attributes:in:).md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func invalidateGlyphs(onLayoutInvalidationForGlyphRange: NSRange)](nslayoutmanager/invalidateglyphs(onlayoutinvalidationforglyphrange:).md)
  Specifies explicitly when portions of the glyph stream depend on layout.
- [func invalidateLayout(forCharacterRange: NSRange, isSoft: Bool, actualCharacterRange: NSRangePointer?)](nslayoutmanager/invalidatelayout(forcharacterrange:issoft:actualcharacterrange:).md)
  Invalidates the layout information for the glyphs mapped to the given range of characters.
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
- [func setLocations(NSPointArray, startingGlyphIndexes: UnsafeMutablePointer<Int>, count: Int, forGlyphRange: NSRange)](nslayoutmanager/setlocations(_:startingglyphindexes:count:forglyphrange:).md)
  Sets locations for many glyph ranges at once.
- [func rectArray(forCharacterRange: NSRange, withinSelectedCharacterRange: NSRange, in: NSTextContainer, rectCount: UnsafeMutablePointer<Int>) -> NSRectArray?](nslayoutmanager/rectarray(forcharacterrange:withinselectedcharacterrange:in:rectcount:).md)
  Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given character range.
- [func rectArray(forGlyphRange: NSRange, withinSelectedGlyphRange: NSRange, in: NSTextContainer, rectCount: UnsafeMutablePointer<Int>) -> NSRectArray?](nslayoutmanager/rectarray(forglyphrange:withinselectedglyphrange:in:rectcount:).md)
  Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given glyph range.
- [func substituteFont(for: NSFont) -> NSFont](nslayoutmanager/substitutefont(for:).md)
  Replaces the specified font with a suitable screen font if one is available.
### Properties
- [var hyphenationFactor: Float](nslayoutmanager/hyphenationfactor.md)
  The threshold controlling when hyphenation is done.
- [var usesScreenFonts: Bool](nslayoutmanager/usesscreenfonts.md)
  A Boolean that controls using screen fonts to calculate layout and display text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager-deprecated-symbols)*