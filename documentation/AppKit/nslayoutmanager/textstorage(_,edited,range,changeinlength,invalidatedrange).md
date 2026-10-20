# textStorage(_:edited:range:changeInLength:invalidatedRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Invalidates glyph and layout information for a portion of the text in the given text storage object.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use [`processEditing(for:edited:range:changeInLength:invalidatedRange:)`](./processediting%28for,edited,range,changeinlength,invalidatedrange%29.md) instead.

## Declaration

```swift
func textStorage(_ str: NSTextStorage, edited editedMask: Int = [], range newCharRange: NSRange, changeInLength delta: Int, invalidatedRange invalidatedCharRange: NSRange)
```

```objc
- (void) textStorage:(NSTextStorage *) str edited:(NSTextStorageEditedOptions) editedMask range:(NSRange) newCharRange changeInLength:(NSInteger) delta invalidatedRange:(NSRange) invalidatedCharRange;
```

#### Discussion

This message is sent from the `NSTextStorage`object’s [`processEditing()`](../nstextstorage/processediting%28%29.md) method to indicate that its characters or attributes have changed. This method invalidates glyphs and layout for the affected characters.

For example, after replacing “The” with “Several” to produce the string “Several files couldn’t be saved”, `newCharRange` is {0, 7} and `delta` is 4. The receiver uses this information to update its character-to-glyph mapping and to update the selection range based on the change.

The [`textStorage(_:edited:range:changeInLength:invalidatedRange:)`](./textstorage%28_,edited,range,changeinlength,invalidatedrange%29.md) messages are sent in a series to each `NSLayoutManager` object associated with the text storage object, so the layout managers receiving them shouldn’t edit `aTextStorage` while this method is executing. If one of them does, the `newCharRange`, `delta`, and `invalidatedCharRange` arguments are incorrect for all following layout managers that receive the message.

## Parameters

- `str`: The text storage whose information is invalidated.
- `editedMask`: Specifies the nature of the changes. Its value is made by combining with the C bitwise OR operator the constants described in “Change notifications” in [`NSTextStorage`](../nstextstorage.md) ([`editedAttributes`](../nstextstorageeditactions/editedattributes.md) and [`editedCharacters`](../nstextstorageeditactions/editedcharacters.md)).
- `newCharRange`: Indicates the extent of characters resulting from the edits.
- `delta`: If the `NSTextStorageEditedCharacters` bit of `mask` is set, gives the number of characters added to or removed from the original range (otherwise its value is irrelevant).
- `invalidatedCharRange`: Represents the range of characters affected after attributes have been fixed. Is either equal to `newCharRange` or larger. For example, deleting a paragraph separator character invalidates the layout information for all characters in the paragraphs that precede and follow the separator.

## See Also

### Deprecated methods
- [func showCGGlyphs(UnsafePointer<CGGlyph>, positions: UnsafePointer<NSPoint>, count: Int, font: NSFont, matrix: AffineTransform, attributes: [NSAttributedString.Key : Any], in: NSGraphicsContext)](./showcgglyphs%28_,positions,count,font,matrix,attributes,in%29.md)
  Renders the glyphs at the specified positions, using the specified attributes.
- [func invalidateGlyphs(onLayoutInvalidationForGlyphRange: NSRange)](./invalidateglyphs%28onlayoutinvalidationforglyphrange%29.md)
  Specifies explicitly when portions of the glyph stream depend on layout.
- [func invalidateLayout(forCharacterRange: NSRange, isSoft: Bool, actualCharacterRange: NSRangePointer?)](./invalidatelayout%28forcharacterrange,issoft,actualcharacterrange%29.md)
  Invalidates the layout information for the glyphs mapped to the given range of characters.
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
- [func setIntAttribute(Int, value: Int, forGlyphAt: Int)](./setintattribute%28_,value,forglyphat%29.md)
  Sets a custom attribute value for a given glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/textstorage(_:edited:range:changeinlength:invalidatedrange:))*