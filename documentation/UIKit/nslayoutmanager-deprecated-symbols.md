# Deprecated symbols

**Framework**: UIKit

Review unsupported symbols and their replacements.

## Topics

### Methods
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count: Int, font: UIFont, matrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any], in: CGContext)](nslayoutmanager/showcgglyphs(_:positions:count:font:matrix:attributes:in:).md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func invalidateGlyphs(onLayoutInvalidationForGlyphRange glyphRange: NSRange)](../AppKit/NSLayoutManager/invalidateGlyphs(onLayoutInvalidationForGlyphRange:).md)
  Specifies explicitly when portions of the glyph stream depend on layout.
- [func invalidateLayout(forCharacterRange charRange: NSRange, isSoft flag: Bool, actualCharacterRange actualCharRange: NSRangePointer?)](../AppKit/NSLayoutManager/invalidateLayout(forCharacterRange:isSoft:actualCharacterRange:).md)
  Invalidates the layout information for the glyphs mapped to the given range of characters.
- [func textStorage(_ str: NSTextStorage, edited editedMask: Int = [], range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)](../AppKit/NSLayoutManager/textStorage(_:edited:range:changeInLength:invalidatedRange:).md)
  Invalidates glyph and layout information for a portion of the text in the given text storage object.
- [func insertGlyph(_ glyph: NSGlyph, atGlyphIndex glyphIndex: Int, characterIndex charIndex: Int)](../AppKit/NSLayoutManager/insertGlyph(_:atGlyphIndex:characterIndex:).md)
  Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index.
- [func insertGlyphs(_ glyphs: UnsafePointer<NSGlyph>, length: Int, forStartingGlyphAt glyphIndex: Int, characterIndex charIndex: Int)](../AppKit/NSLayoutManager/insertGlyphs(_:length:forStartingGlyphAt:characterIndex:).md)
  Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index.
- [func glyph(at: Int) -> CGGlyph](nslayoutmanager/glyph(at:).md)
  Returns the glyph at the specified index.
- [func glyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> CGGlyph](nslayoutmanager/glyph(at:isvalidindex:).md)
  Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid.
- [func replaceGlyph(at glyphIndex: Int, withGlyph newGlyph: NSGlyph)](../AppKit/NSLayoutManager/replaceGlyph(at:withGlyph:).md)
  Replaces the glyph at the given index with a new glyph.
- [func getGlyphs(_ glyphArray: UnsafeMutablePointer<NSGlyph>?, range glyphRange: NSRange) -> Int](../AppKit/NSLayoutManager/getGlyphs(_:range:).md)
  Fills the passed-in buffer with a sequence of glyphs.
- [func getGlyphs(in glyphRange: NSRange, glyphs glyphBuffer: UnsafeMutablePointer<NSGlyph>?, characterIndexes charIndexBuffer: UnsafeMutablePointer<Int>?, glyphInscriptions inscribeBuffer: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits elasticBuffer: UnsafeMutablePointer<ObjCBool>?) -> Int](../AppKit/NSLayoutManager/getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:).md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func getGlyphs(in glyphRange: NSRange, glyphs glyphBuffer: UnsafeMutablePointer<NSGlyph>?, characterIndexes charIndexBuffer: UnsafeMutablePointer<Int>?, glyphInscriptions inscribeBuffer: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits elasticBuffer: UnsafeMutablePointer<ObjCBool>?, bidiLevels bidiLevelBuffer: UnsafeMutablePointer<UInt8>?) -> Int](../AppKit/NSLayoutManager/getGlyphs(in:glyphs:characterIndexes:glyphInscriptions:elasticBits:bidiLevels:).md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func deleteGlyphs(in glyphRange: NSRange)](../AppKit/NSLayoutManager/deleteGlyphs(in:).md)
  Deletes the glyphs in the given range from the receiver’s glyph store.
- [func setCharacterIndex(_ charIndex: Int, forGlyphAt glyphIndex: Int)](../AppKit/NSLayoutManager/setCharacterIndex(_:forGlyphAt:).md)
  Sets the index of the character corresponding to the glyph at the given glyph index.
- [func intAttribute(_ attributeTag: Int, forGlyphAt glyphIndex: Int) -> Int](../AppKit/NSLayoutManager/intAttribute(_:forGlyphAt:).md)
  Returns the value of the attribute identified by the given attribute tag for the glyph at the given index.
- [func setIntAttribute(_ attributeTag: Int, value val: Int, forGlyphAt glyphIndex: Int)](../AppKit/NSLayoutManager/setIntAttribute(_:value:forGlyphAt:).md)
  Sets a custom attribute value for a given glyph.
- [func setLocations(_ locations: NSPointArray, startingGlyphIndexes glyphIndexes: UnsafeMutablePointer<Int>, count: Int, forGlyphRange glyphRange: NSRange)](../AppKit/NSLayoutManager/setLocations(_:startingGlyphIndexes:count:forGlyphRange:).md)
  Sets locations for many glyph ranges at once.
- [func rectArray(forCharacterRange charRange: NSRange, withinSelectedCharacterRange selCharRange: NSRange, in container: NSTextContainer, rectCount: UnsafeMutablePointer<Int>) -> NSRectArray?](../AppKit/NSLayoutManager/rectArray(forCharacterRange:withinSelectedCharacterRange:in:rectCount:).md)
  Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given character range.
- [func rectArray(forGlyphRange glyphRange: NSRange, withinSelectedGlyphRange selGlyphRange: NSRange, in container: NSTextContainer, rectCount: UnsafeMutablePointer<Int>) -> NSRectArray?](../AppKit/NSLayoutManager/rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:).md)
  Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given glyph range.
- [func substituteFont(for originalFont: NSFont) -> NSFont](../AppKit/NSLayoutManager/substituteFont(for:).md)
  Replaces the specified font with a suitable screen font if one is available.
### Properties
- [var hyphenationFactor: CGFloat](nslayoutmanager/hyphenationfactor.md)
  The threshold controlling when hyphenation is done.
- [attributedString](nslayoutmanager-attributedstring.md)
  The text storage object from which the `NSGlyphGenerator` object procures characters for glyph generation.
- [layoutOptions](nslayoutmanager-layoutoptions.md)
  The layout manager’s current layout options.
- [var usesScreenFonts: Bool { get set }](../AppKit/NSLayoutManager/usesScreenFonts.md)
  A Boolean that controls using screen fonts to calculate layout and display text.
### Types
- [Glyph Attributes](../AppKit/glyph-attributes.md)
  Attributes that are used only inside the glyph generation machinery, but must also be shared between components.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager-deprecated-symbols)*