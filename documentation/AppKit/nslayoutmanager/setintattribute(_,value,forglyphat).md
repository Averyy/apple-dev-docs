# setIntAttribute(_:value:forGlyphAt:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets a custom attribute value for a given glyph.

**Availability**:
- macOS 10.0+ - Deprecated in 10.11

> **Deprecated**: Use -setGlyphs:properties:characterIndexes:font:forGlyphRange instead

## Declaration

```swift
func setIntAttribute(_ attributeTag: Int, value val: Int, forGlyphAt glyphIndex: Int)
```

```objc
- (void) setIntAttribute:(NSInteger) attributeTag value:(NSInteger) val forGlyphAtIndex:(NSUInteger) glyphIndex;
```

## Discussion

Custom attributes are glyph attributes such as `NSGlyphInscription` or attributes defined by subclasses. Nonnegative tags are reserved by Apple; you can define your own attributes with negative tags and set values using this method.

This method is part of the `NSGlyphStorage` protocol, for use by the glyph generator to set attributes. It is not usually necessary for anyone but the glyph generator (and perhaps the typesetter) to call it. It is provided as a public method so subclasses can extend it to accept other glyph attributes. To add new glyph attributes to the text system you must do two things. First, you need to arrange for the glyph generator or typesetter to generate and interpret it. Second, you need to subclass `NSLayoutManager` to provide someplace to store the new attribute, overriding this method and [`intAttribute(_:forGlyphAt:)`](./intattribute%28_,forglyphat%29.md) to recognize the new attribute tags and respond to them, while passing any other attributes to the superclass implementation. The `NSLayoutManager` implementation understands the glyph attributes which it is prepared to store, as enumerated in [Glyph Attributes](../glyph-attributes.md).

## Parameters

- `attributeTag`: The custom attribute.
- `val`: The new attribute value.
- `glyphIndex`: Index of the glyph whose attribute is set.

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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setintattribute(_:value:forglyphat:))*