# setLineFragmentRect(_:forGlyphRange:usedRect:)

**Framework**: UIKit  
**Kind**: method

Associates the line fragment bounds for the specified range of glyphs.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setLineFragmentRect(_ fragmentRect: CGRect, forGlyphRange glyphRange: NSRange, usedRect: CGRect)
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

- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> CGRect](nslayoutmanager/linefragmentusedrect(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> CGRect](nslayoutmanager/linefragmentrect(forglyphat:effectiverange:).md)
  Returns the rectangle for the line fragment where the glyph lies and (optionally), by reference, the entire range of glyphs in that fragment.
- [func lineFragmentRect(forGlyphAt: Int, effectiveRange: NSRangePointer?, withoutAdditionalLayout: Bool) -> CGRect](nslayoutmanager/linefragmentrect(forglyphat:effectiverange:withoutadditionallayout:).md)
  Returns the line fragment rectangle that contains the glyph at the specified glyph index.
- [func lineFragmentUsedRect(forGlyphAt: Int, effectiveRange: NSRangePointer?) -> CGRect](nslayoutmanager/linefragmentusedrect(forglyphat:effectiverange:).md)
  Returns the usage rectangle for the line fragment and (optionally) returns the entire range of glyphs in that fragment.
- [func setAttachmentSize(CGSize, forGlyphRange: NSRange)](nslayoutmanager/setattachmentsize(_:forglyphrange:).md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:).md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(CGRect, usedRect: CGRect, textContainer: NSTextContainer)](nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:).md)
  Sets the bounds and container for the extra line fragment.
- [func setLocation(CGPoint, forStartOfGlyphRange: NSRange)](nslayoutmanager/setlocation(_:forstartofglyphrange:).md)
  Sets the location for the first glyph in the specified range.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](nslayoutmanager/setnotshownattribute(_:forglyphat:).md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:))*