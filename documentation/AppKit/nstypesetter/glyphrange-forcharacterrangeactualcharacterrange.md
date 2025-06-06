# glyphRange(forCharacterRange:actualCharacterRange:)

**Framework**: AppKit  
**Kind**: method

Returns the range for the glyphs mapped to the characters of the text store in the specified range.

**Availability**:
- macOS ?+

## Declaration

```swift
func glyphRange(forCharacterRange charRange: NSRange, actualCharacterRange actualCharRange: NSRangePointer?) -> NSRange
```

#### Return Value

The range for the glyphs mapped to the characters of the text store in `charRange`.

#### Discussion

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `charRange`: The range of the characters whose glyph range is desired.
- `actualCharRange`: On return, all characters mapped to those glyphs; may be  .

## See Also

- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](nstypesetter/characterrange(forglyphrange:actualglyphrange:).md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](nstypesetter/setattachmentsize(_:forglyphrange:).md)
  Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.
- [func setBidiLevels(UnsafePointer<UInt8>!, forGlyphRange: NSRange)](nstypesetter/setbidilevels(_:forglyphrange:).md)
  Sets the direction of the specified glyphs for bidirectional text.
- [func setDrawsOutsideLineFragment(Bool, forGlyphRange: NSRange)](nstypesetter/setdrawsoutsidelinefragment(_:forglyphrange:).md)
  Sets whether the specified glyphs exceed the bounds of the line fragment in which they are laid out.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect, baselineOffset: CGFloat)](nstypesetter/setlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Sets the line fragment rectangle where the specified glyphs are laid out.
- [func setLocation(NSPoint, withAdvancements: UnsafePointer<CGFloat>!, forStartOfGlyphRange: NSRange)](nstypesetter/setlocation(_:withadvancements:forstartofglyphrange:).md)
  Sets the location where the specified glyphs are laid out.
- [func setNotShownAttribute(Bool, forGlyphRange: NSRange)](nstypesetter/setnotshownattribute(_:forglyphrange:).md)
  Sets whether the specified glyphs are not shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/glyphrange(forcharacterrange:actualcharacterrange:))*