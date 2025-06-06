# setLocation(_:forStartOfGlyphRange:)

**Framework**: AppKit  
**Kind**: method

Sets the location for the first glyph in the specified range.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setLocation(_ location: NSPoint, forStartOfGlyphRange glyphRange: NSRange)
```

#### Discussion

Setting the location for a glyph range implies that its first glyph is not nominally spaced with respect to the previous glyph. In the course of layout, all glyphs should end up being included in a range passed to this method, but only glyphs that start a new nominal range should be at the start of such ranges. The first glyph in a line fragment should always start a new nominal range. Glyph locations are given relative to their line fragment rectangle’s origin.

Before setting the location for a glyph range, you must specify the text container with [`setTextContainer(_:forGlyphRange:)`](nslayoutmanager/settextcontainer(_:forglyphrange:).md) and the line fragment rectangle with [`setLineFragmentRect(_:forGlyphRange:usedRect:)`](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md).

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `location`: The location to which the first glyph is set, relative to the origin of the glyph’s line fragment origin.
- `glyphRange`: The glyphs whose location is set.

## See Also

- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](nslayoutmanager/setattachmentsize(_:forglyphrange:).md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:).md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(NSRect, usedRect: NSRect, textContainer: NSTextContainer)](nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:).md)
  Sets the bounds and container for the extra line fragment.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect)](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](nslayoutmanager/setnotshownattribute(_:forglyphat:).md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setlocation(_:forstartofglyphrange:))*