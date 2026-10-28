# Deprecated symbols

**Framework**: AppKit  
**Role**: API Collection

Review symbols that are no longer in active development, and their recommended replacements.

## Overview

Although these symbols are available for use, Apple is no longer actively developing them, and may remove them in a future release. Apple recommends moving away from these symbols and using their indicated replacements instead. Check the individual symbol pages for the recommended replacements.

## Topics

### Deprecated methods
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<NSPoint>, count: Int, font: NSFont, matrix: AffineTransform, attributes: [NSAttributedString.Key : Any], in: NSGraphicsContext)](./nslayoutmanager/showcgglyphs%28_,positions,count,font,matrix,attributes,in%29.md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func invalidateGlyphs(onLayoutInvalidationForGlyphRange: NSRange)](./nslayoutmanager/invalidateglyphs%28onlayoutinvalidationforglyphrange%29.md)
  Specifies explicitly when portions of the glyph stream depend on layout.
- [func invalidateLayout(forCharacterRange: NSRange, isSoft: Bool, actualCharacterRange: NSRangePointer?)](./nslayoutmanager/invalidatelayout%28forcharacterrange,issoft,actualcharacterrange%29.md)
  Invalidates the layout information for the glyphs mapped to the given range of characters.
- [func textStorage(NSTextStorage, edited: Int, range: NSRange, changeInLength: Int, invalidatedRange: NSRange)](./nslayoutmanager/textstorage%28_,edited,range,changeinlength,invalidatedrange%29.md)
  Invalidates glyph and layout information for a portion of the text in the given text storage object.
- [func insertGlyph(NSGlyph, atGlyphIndex: Int, characterIndex: Int)](./nslayoutmanager/insertglyph%28_,atglyphindex,characterindex%29.md)
  Inserts a single glyph into the glyph stream at the given index and maps it to the character at the given character index.
- [func insertGlyphs(UnsafePointer<NSGlyph>, length: Int, forStartingGlyphAt: Int, characterIndex: Int)](./nslayoutmanager/insertglyphs%28_,length,forstartingglyphat,characterindex%29.md)
  Inserts the given glyphs into the glyph cache at the given index and maps them to characters beginning at the given character index.
- [func glyph(at: Int) -> NSGlyph](./nslayoutmanager/glyph%28at%29.md)
  Returns the glyph at the specified index.
- [func glyph(at: Int, isValidIndex: UnsafeMutablePointer<ObjCBool>?) -> NSGlyph](./nslayoutmanager/glyph%28at,isvalidindex%29.md)
  Returns the glyph at a specified index, and optionally returns a flag indicating whether the requested index is valid.
- [func replaceGlyph(at: Int, withGlyph: NSGlyph)](./nslayoutmanager/replaceglyph%28at,withglyph%29.md)
  Replaces the glyph at the given index with a new glyph.
- [func getGlyphs(UnsafeMutablePointer<NSGlyph>?, range: NSRange) -> Int](./nslayoutmanager/getglyphs%28_,range%29.md)
  Fills the passed-in buffer with a sequence of glyphs.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>?, characterIndexes: UnsafeMutablePointer<Int>?, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits: UnsafeMutablePointer<ObjCBool>?) -> Int](./nslayoutmanager/getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits%29.md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func getGlyphs(in: NSRange, glyphs: UnsafeMutablePointer<NSGlyph>?, characterIndexes: UnsafeMutablePointer<Int>?, glyphInscriptions: UnsafeMutablePointer<NSGlyphInscription>?, elasticBits: UnsafeMutablePointer<ObjCBool>?, bidiLevels: UnsafeMutablePointer<UInt8>?) -> Int](./nslayoutmanager/getglyphs%28in,glyphs,characterindexes,glyphinscriptions,elasticbits,bidilevels%29.md)
  Returns the glyphs and information needed to perform layout for the given glyph range.
- [func deleteGlyphs(in: NSRange)](./nslayoutmanager/deleteglyphs%28in%29.md)
  Deletes the glyphs in the given range from the receiver’s glyph store.
- [func setCharacterIndex(Int, forGlyphAt: Int)](./nslayoutmanager/setcharacterindex%28_,forglyphat%29.md)
  Sets the index of the character corresponding to the glyph at the given glyph index.
- [func intAttribute(Int, forGlyphAt: Int) -> Int](./nslayoutmanager/intattribute%28_,forglyphat%29.md)
  Returns the value of the attribute identified by the given attribute tag for the glyph at the given index.
- [func setIntAttribute(Int, value: Int, forGlyphAt: Int)](./nslayoutmanager/setintattribute%28_,value,forglyphat%29.md)
  Sets a custom attribute value for a given glyph.
- [func setLocations(NSPointArray, startingGlyphIndexes: UnsafeMutablePointer<Int>, count: Int, forGlyphRange: NSRange)](./nslayoutmanager/setlocations%28_,startingglyphindexes,count,forglyphrange%29.md)
  Sets locations for many glyph ranges at once.
- [func rectArray(forCharacterRange: NSRange, withinSelectedCharacterRange: NSRange, in: NSTextContainer, rectCount: UnsafeMutablePointer<Int>) -> NSRectArray?](./nslayoutmanager/rectarray%28forcharacterrange,withinselectedcharacterrange,in,rectcount%29.md)
  Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given character range.
- [func rectArray(forGlyphRange: NSRange, withinSelectedGlyphRange: NSRange, in: NSTextContainer, rectCount: UnsafeMutablePointer<Int>) -> NSRectArray?](./nslayoutmanager/rectarray%28forglyphrange,withinselectedglyphrange,in,rectcount%29.md)
  Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given glyph range.
- [func substituteFont(for: NSFont) -> NSFont](./nslayoutmanager/substitutefont%28for%29.md)
  Replaces the specified font with a suitable screen font if one is available.
- [- showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:](./nslayoutmanager/showpackedglyphs_length_glyphrange_atpoint_font_color_printingadjustment_.md)
  Draws a range of glyphs.
### Deprecated properties
- [var hyphenationFactor: Float](./nslayoutmanager/hyphenationfactor.md)
  The threshold controlling when hyphenation is done.
- [var usesScreenFonts: Bool](./nslayoutmanager/usesscreenfonts.md)
  A Boolean that controls using screen fonts to calculate layout and display text.
### Deprecated types
- [NSGlyphInscription](./nsglyphinscription.md)
  Constants that specify how a glyph is laid out relative to the previous glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager-deprecated-symbols)*