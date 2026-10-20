# rectArray(forGlyphRange:withinSelectedGlyphRange:in:rectCount:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns an array of rectangles and, by reference, the number of such rectangles, that define the region in the given container enclosing the given glyph range.

**Availability**:
- macOS

## Declaration

```swift
func rectArray(forGlyphRange glyphRange: NSRange, withinSelectedGlyphRange selGlyphRange: NSRange, in container: NSTextContainer, rectCount: UnsafeMutablePointer<Int>) -> NSRectArray?
```

```objc
- (NSRectArray) rectArrayForGlyphRange:(NSRange) glyphRange withinSelectedGlyphRange:(NSRange) selGlyphRange inTextContainer:(NSTextContainer *) container rectCount:(NSUInteger *) rectCount;
```

#### Return Value

The array of rectangles enclosing the given range.

#### Discussion

These rectangles can be used to draw the text background or highlight for the given range of characters. If a selected range is given in `selGlyphRange`, the rectangles returned are correct for drawing the selection.  Selection rectangles are generally more complicated than enclosing rectangles and supplying a selected range is the clue this method uses to determine whether to go to the trouble of doing this special work.

The number of rectangles returned isn’t necessarily the number of lines enclosing the specified range. Contiguous lines can share an enclosing rectangle, and lines broken into several fragments have a separate enclosing rectangle for each fragment.

This method will do the minimum amount of work required to answer the question.  The resulting array is owned by the layout manager and will be reused when this method, [`rectArray(forCharacterRange:withinSelectedCharacterRange:in:rectCount:)`](./rectarray%28forcharacterrange,withinselectedcharacterrange,in,rectcount%29.md), or [`boundingRect(forGlyphRange:in:)`](./boundingrect%28forglyphrange,in%29.md) is called.  One of these methods may be called indirectly. If you aren’t going to use the rectangles right away, you should copy them to another location. These rectangles are always in container coordinates.

The purpose of this method is to calculate line rectangles for drawing the text background and highlighting. These rectangles don’t necessarily enclose glyphs that draw outside their line fragment rectangles; use [`boundingRect(forGlyphRange:in:)`](./boundingrect%28forglyphrange,in%29.md) to determine the area that contains all drawing performed for a range of glyphs.

Performs glyph generation and layout if needed.

## Parameters

- `glyphRange`: The glyph range for which to return rectangles.
- `selGlyphRange`: Selected glyphs within `glyphRange`, which can affect the size of the rectangles; it must be equal to or contain `glyphRange`. If the caller is interested in this more from an enclosing point of view rather than a selection point of view, pass `{NSNotFound, 0}` as the selected range.
- `container`: The text container in which the text is laid out.
- `rectCount`: The number of rectangles returned.

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
- [func setCharacterIndex(Int, forGlyphAt: Int)](./setcharacterindex%28_,forglyphat%29.md)
  Sets the index of the character corresponding to the glyph at the given glyph index.
- [func intAttribute(Int, forGlyphAt: Int) -> Int](./intattribute%28_,forglyphat%29.md)
  Returns the value of the attribute identified by the given attribute tag for the glyph at the given index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/rectarray(forglyphrange:withinselectedglyphrange:in:rectcount:))*