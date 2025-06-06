# setAttachmentSize(_:forGlyphRange:)

**Framework**: AppKit  
**Kind**: method

Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.

**Availability**:
- macOS ?+

## Declaration

```swift
func setAttachmentSize(_ attachmentSize: NSSize, forGlyphRange glyphRange: NSRange)
```

#### Discussion

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `attachmentSize`: The size the glyphs in   (assumed to be attachments) will be asked to draw themselves at.
- `glyphRange`: The range of glyphs the attachment size applies to.

## See Also

- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](nstypesetter/characterrange(forglyphrange:actualglyphrange:).md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](nstypesetter/glyphrange(forcharacterrange:actualcharacterrange:).md)
  Returns the range for the glyphs mapped to the characters of the text store in the specified range.
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

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/setattachmentsize(_:forglyphrange:))*