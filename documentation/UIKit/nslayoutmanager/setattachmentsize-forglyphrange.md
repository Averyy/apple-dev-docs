# setAttachmentSize(_:forGlyphRange:)

**Framework**: UIKit  
**Kind**: method

Sets the size to use when drawing a glyph that represents an attachment.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setAttachmentSize(_ attachmentSize: CGSize, forGlyphRange glyphRange: NSRange)
```

#### Discussion

For a glyph corresponding to an attachment, this method should be called to set the size for the attachment cell to occupy. The glyph’s value should be [`NSControlGlyph`](https://developer.apple.com/documentation/AppKit/NSControlGlyph).

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `attachmentSize`: The glyph size to set.
- `glyphRange`: The attachment glyph’s position in the glyph stream.

## See Also

- [func attachmentSize(forGlyphAt: Int) -> CGSize](nslayoutmanager/attachmentsize(forglyphat:).md)
  Returns the size of the attachment glyph at the specified index.
- [var defaultAttachmentScaling: NSImageScaling { get set }](../AppKit/NSLayoutManager/defaultAttachmentScaling.md)
  The default amount of scaling to apply when an attachment image is too large to fit in a text container.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:).md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(CGRect, usedRect: CGRect, textContainer: NSTextContainer)](nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:).md)
  Sets the bounds and container for the extra line fragment.
- [func setLineFragmentRect(CGRect, forGlyphRange: NSRange, usedRect: CGRect)](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setLocation(CGPoint, forStartOfGlyphRange: NSRange)](nslayoutmanager/setlocation(_:forstartofglyphrange:).md)
  Sets the location for the first glyph in the specified range.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](nslayoutmanager/setnotshownattribute(_:forglyphat:).md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/setattachmentsize(_:forglyphrange:))*