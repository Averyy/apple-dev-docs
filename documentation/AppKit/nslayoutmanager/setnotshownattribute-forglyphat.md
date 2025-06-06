# setNotShownAttribute(_:forGlyphAt:)

**Framework**: AppKit  
**Kind**: method

Sets the visibility of the glyph at the specified index.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setNotShownAttribute(_ flag: Bool, forGlyphAt glyphIndex: Int)
```

#### Discussion

The typesetter decides which glyphs are not shown and sets this attribute in the layout manager to ensure that those glyphs are not displayed. For example, a tab or newline character doesn’t leave any marks; it just indicates where following glyphs are laid out.

Raises an `NSRangeException` if `glyphIndex` is out of bounds.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `flag`: If  , the glyph is not shown; if  , it is shown.
- `glyphIndex`: Index of the glyph whose attribute is set.

## See Also

- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](nslayoutmanager/setattachmentsize(_:forglyphrange:).md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](nslayoutmanager/setdrawsoutsidelinefragment(_:forglyphat:).md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(NSRect, usedRect: NSRect, textContainer: NSTextContainer)](nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:).md)
  Sets the bounds and container for the extra line fragment.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect)](nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:).md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setLocation(NSPoint, forStartOfGlyphRange: NSRange)](nslayoutmanager/setlocation(_:forstartofglyphrange:).md)
  Sets the location for the first glyph in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setnotshownattribute(_:forglyphat:))*