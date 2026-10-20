# setLocation(_:forStartOfGlyphRange:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the location for the first glyph in the specified range.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setLocation(_ location: CGPoint, forStartOfGlyphRange glyphRange: NSRange)
```

```objc
- (void) setLocation:(CGPoint) location forStartOfGlyphRange:(NSRange) glyphRange;
```

#### Discussion

Setting the location for a glyph range implies that its first glyph is not nominally spaced with respect to the previous glyph. In the course of layout, all glyphs should end up being included in a range passed to this method, but only glyphs that start a new nominal range should be at the start of such ranges. The first glyph in a line fragment should always start a new nominal range. Glyph locations are given relative to their line fragment rectangle’s origin.

Before setting the location for a glyph range, you must specify the text container with [`setTextContainer(_:forGlyphRange:)`](./settextcontainer%28_,forglyphrange%29.md) and the line fragment rectangle with [`setLineFragmentRect(_:forGlyphRange:usedRect:)`](./setlinefragmentrect%28_,forglyphrange,usedrect%29.md).

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `location`: The location to which the first glyph is set, relative to the origin of the glyph’s line fragment origin.
- `glyphRange`: The glyphs whose location is set.

## See Also

### Setting layout information
- [func setAttachmentSize(CGSize, forGlyphRange: NSRange)](./setattachmentsize%28_,forglyphrange%29.md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](./setdrawsoutsidelinefragment%28_,forglyphat%29.md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(CGRect, usedRect: CGRect, textContainer: NSTextContainer)](./setextralinefragmentrect%28_,usedrect,textcontainer%29.md)
  Sets the bounds and container for the extra line fragment.
- [func setLineFragmentRect(CGRect, forGlyphRange: NSRange, usedRect: CGRect)](./setlinefragmentrect%28_,forglyphrange,usedrect%29.md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](./setnotshownattribute%28_,forglyphat%29.md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/setlocation(_:forstartofglyphrange:))*