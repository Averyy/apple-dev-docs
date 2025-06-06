# showCGGlyphs(_:positions:count:font:matrix:attributes:in:)

**Framework**: UIKit  
**Kind**: method

Renders the glyphs at the specified positions, using the specified attributes.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- tvOS 9.0+

## Declaration

```swift
func showCGGlyphs(_ glyphs: UnsafePointer<CGGlyph>, positions: UnsafePointer<CGPoint>, count glyphCount: Int, font: UIFont, matrix textMatrix: CGAffineTransform, attributes: [NSAttributedString.Key : Any] = [:], in graphicsContext: CGContext)
```

#### Discussion

`NSLayoutManager` invokes this primitive method unless an override implementation of the deprecated [`showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:`](https://developer.apple.com/documentation/AppKit/NSLayoutManager/showPackedGlyphs:length:glyphRange:atPoint:font:color:printingAdjustment:) method exists and this method is not overridden.

## Parameters

- `glyphs`: The glyphs to draw; may contain embedded   bytes.
- `positions`: The positions at which to draw the glyphs in the user space coordinate system.
- `glyphCount`: The number of glyphs.
- `font`: The font applied to the graphics state. This value can be different from the   value in the   argument because of various font substitutions that the system automatically executes.
- `textMatrix`: The affine transform mapping the text space coordinate system to the user space coordinate system. The   and   components of   are ignored since Quartz overrides them with the glyph positions.
- `attributes`: A dictionary of glyph attributes. See   for supported keys and values.
- `graphicsContext`: If non- ,   is already configured according to the text attributes arguments:  ,  , and  .

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/showcgglyphs(_:positions:count:font:matrix:attributes:in:))*