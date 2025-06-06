# setLocation(_:withAdvancements:forStartOfGlyphRange:)

**Framework**: AppKit  
**Kind**: method

Sets the location where the specified glyphs are laid out.

**Availability**:
- macOS ?+

## Declaration

```swift
func setLocation(_ location: NSPoint, withAdvancements advancements: UnsafePointer<CGFloat>!, forStartOfGlyphRange glyphRange: NSRange)
```

#### Discussion

Setting the location for a series of glyphs implies that the glyphs preceding it can’t be included in a single `show` operation.

Before setting the location for a glyph range, you must specify line fragment rectangle with [`setLineFragmentRect(_:forGlyphRange:usedRect:baselineOffset:)`](nstypesetter/setlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md).

A subclass can override this method to interact with custom glyph storage.

## Parameters

- `location`: The location where the glyphs in   are laid out. The x-coordinate of   is expressed relative to the line fragment rectangle origin, and the y-coordinate is expressed relative to the baseline previously specified by  .
- `advancements`: The nominal glyph advance width specified in the font metric information.
- `glyphRange`: The range of glyphs whose layout location is being set. This series of glyphs can be displayed with a single PostScript   operation (a nominal range).

## See Also

- [func characterRange(forGlyphRange: NSRange, actualGlyphRange: NSRangePointer?) -> NSRange](nstypesetter/characterrange(forglyphrange:actualglyphrange:).md)
  Returns the range for the characters in the receiver’s text store that are mapped to the specified glyphs.
- [func glyphRange(forCharacterRange: NSRange, actualCharacterRange: NSRangePointer?) -> NSRange](nstypesetter/glyphrange(forcharacterrange:actualcharacterrange:).md)
  Returns the range for the glyphs mapped to the characters of the text store in the specified range.
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](nstypesetter/setattachmentsize(_:forglyphrange:).md)
  Sets the size the specified glyphs (assumed to be attachments) will be asked to draw themselves at.
- [func setBidiLevels(UnsafePointer<UInt8>!, forGlyphRange: NSRange)](nstypesetter/setbidilevels(_:forglyphrange:).md)
  Sets the direction of the specified glyphs for bidirectional text.
- [func setDrawsOutsideLineFragment(Bool, forGlyphRange: NSRange)](nstypesetter/setdrawsoutsidelinefragment(_:forglyphrange:).md)
  Sets whether the specified glyphs exceed the bounds of the line fragment in which they are laid out.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect, baselineOffset: CGFloat)](nstypesetter/setlinefragmentrect(_:forglyphrange:usedrect:baselineoffset:).md)
  Sets the line fragment rectangle where the specified glyphs are laid out.
- [func setNotShownAttribute(Bool, forGlyphRange: NSRange)](nstypesetter/setnotshownattribute(_:forglyphrange:).md)
  Sets whether the specified glyphs are not shown.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/setlocation(_:withadvancements:forstartofglyphrange:))*