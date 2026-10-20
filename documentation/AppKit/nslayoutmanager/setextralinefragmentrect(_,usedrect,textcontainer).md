# setExtraLineFragmentRect(_:usedRect:textContainer:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the bounds and container for the extra line fragment.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setExtraLineFragmentRect(_ fragmentRect: NSRect, usedRect: NSRect, textContainer container: NSTextContainer)
```

```objc
- (void) setExtraLineFragmentRect:(NSRect) fragmentRect usedRect:(NSRect) usedRect textContainer:(NSTextContainer *) container;
```

#### Discussion

The extra line fragment is used when the text backing ends with a hard line break or when the text backing is totally empty, to define the extra line which needs to be displayed at the end of the text. If the text backing is not empty and does not end with a hard line break, this should be set to [`NSZeroRect`](../../Foundation/nszerorect.md) and `nil`.

Line fragment rectangles and line fragment used rectangles are always in container coordinates.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `fragmentRect`: The rectangle to set.
- `usedRect`: Indicates where the insertion point is drawn.
- `container`: The text container where the rectangle is to be laid out.

## See Also

### Setting layout information
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](./setattachmentsize%28_,forglyphrange%29.md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](./setdrawsoutsidelinefragment%28_,forglyphat%29.md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect)](./setlinefragmentrect%28_,forglyphrange,usedrect%29.md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setLocation(NSPoint, forStartOfGlyphRange: NSRange)](./setlocation%28_,forstartofglyphrange%29.md)
  Sets the location for the first glyph in the specified range.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](./setnotshownattribute%28_,forglyphat%29.md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setextralinefragmentrect(_:usedrect:textcontainer:))*