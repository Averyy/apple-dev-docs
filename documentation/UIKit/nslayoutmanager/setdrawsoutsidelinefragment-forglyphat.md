# setDrawsOutsideLineFragment(_:forGlyphAt:)

**Framework**: UIKit  
**Kind**: method

Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS ?+
- visionOS 1.0+

## Declaration

```swift
func setDrawsOutsideLineFragment(_ flag: Bool, forGlyphAt glyphIndex: Int)
```

#### Discussion

This can happen when text is set at a fixed line height. For example, if the user specifies a fixed line height of 12 points and sets the font size to 24 points, the glyphs will exceed their layout rectangles. This information is important for determining whether additional lines need to be redrawn as a result of changes to any given line fragment.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `flag`: If  , sets the given glyph to draw outside its line fragment; if  , the glyph does not draw outside.
- `glyphIndex`: Index of the glyph to set.

## See Also

- [func drawsOutsideLineFragment(forGlyphAt: Int) -> Bool](nslayoutmanager/drawsoutsidelinefragment(forglyphat:).md)
  Indicates whether the glyph draws outside its line fragment rectangle.
- [func setAttachmentSize(CGSize, forGlyphRange: NSRange)](nslayoutmanager/setattachmentsize(_:forglyphrange:).md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setExtraLineFragmentRect(CGRect, usedRect: CGRect, textContainer: NSTextContainer)](nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:).md)
  Sets the bounds and container for the extra line fragment.
- [func setLineFragmentRect(CGRect, forGlyphRange: NSRange, usedRect: CGRect)](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setLocation(CGPoint, forStartOfGlyphRange: NSRange)](nslayoutmanager/setlocation(_:forstartofglyphrange:).md)
  Sets the location for the first glyph in the specified range.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](nslayoutmanager/setnotshownattribute(_:forglyphat:).md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:))*