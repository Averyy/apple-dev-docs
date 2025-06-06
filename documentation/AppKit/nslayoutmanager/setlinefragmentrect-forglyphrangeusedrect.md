# setLineFragmentRect(_:forGlyphRange:usedRect:)

**Framework**: AppKit  
**Kind**: method

Associates the line fragment bounds for the specified range of glyphs.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setLineFragmentRect(_ fragmentRect: NSRect, forGlyphRange glyphRange: NSRange, usedRect: NSRect)
```

#### Discussion

The typesetter must specify the text container first with [`setTextContainer(_:forGlyphRange:)`](nslayoutmanager/settextcontainer(_:forglyphrange:).md), and it sets the exact positions of the glyphs afterwards with [`setLocation(_:forStartOfGlyphRange:)`](nslayoutmanager/setlocation(_:forstartofglyphrange:).md).

In the course of layout, all glyphs should end up being included in a range passed to this method, but only glyphs that start a new line fragment should be at the start of such ranges.

Line fragment rectangles and line fragment used rectangles are always in container coordinates.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `fragmentRect`: The rectangle of the line fragment.
- `glyphRange`: The range of glyphs to be associated with  .
- `usedRect`: The portion of   that actually contains glyphs or other marks that are drawn (including the text container’s line fragment padding. Must be equal to or contained within  .

## See Also

- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](nslayoutmanager/setattachmentsize(_:forglyphrange:).md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:).md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(NSRect, usedRect: NSRect, textContainer: NSTextContainer)](nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:).md)
  Sets the bounds and container for the extra line fragment.
- [func setLocation(NSPoint, forStartOfGlyphRange: NSRange)](nslayoutmanager/setlocation(_:forstartofglyphrange:).md)
  Sets the location for the first glyph in the specified range.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](nslayoutmanager/setnotshownattribute(_:forglyphat:).md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:))*