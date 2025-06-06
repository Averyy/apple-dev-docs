# setBidiLevels(_:forGlyphRange:)

**Framework**: AppKit  
**Kind**: method

Sets the direction of the specified glyphs for bidirectional text.

**Availability**:
- macOS ?+

## Declaration

```swift
func setBidiLevels(_ levels: UnsafePointer<UInt8>!, forGlyphRange glyphRange: NSRange)
```

#### Discussion

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `levels`: Values in   can range from 0 to 61 as defined by Unicode Standard Annex #9.
- `glyphRange`: The range of glyphs for which the bidirectional text levels are desired.

## See Also

- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](nstypesetter/characterrange(forglyphrange:actualglyphrange:).md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](nstypesetter/glyphrange(forcharacterrange:actualcharacterrange:).md)
  Returns the range for the glyphs mapped to the characters of the text store in the specified range.
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](nstypesetter/setattachmentsize(_:forglyphrange:).md)
  Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.
- [func setDrawsOutsideLineFragment(Bool, forGlyphRange: NSRange)](nstypesetter/setdrawsoutsidelinefragment(_:forglyphrange:).md)
  Sets whether the specified glyphs exceed the bounds of the line fragment in which they are laid out.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect, baselineOffset: CGFloat)](nstypesetter/setlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Sets the line fragment rectangle where the specified glyphs are laid out.
- [func setLocation(NSPoint, withAdvancements: UnsafePointer<CGFloat>!, forStartOfGlyphRange: NSRange)](nstypesetter/setlocation(_:withadvancements:forstartofglyphrange:).md)
  Sets the location where the specified glyphs are laid out.
- [func setNotShownAttribute(Bool, forGlyphRange: NSRange)](nstypesetter/setnotshownattribute(_:forglyphrange:).md)
  Sets whether the specified glyphs are not shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/setbidilevels(_:forglyphrange:))*