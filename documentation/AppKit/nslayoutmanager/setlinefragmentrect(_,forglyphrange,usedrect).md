# setLineFragmentRect(_:forGlyphRange:usedRect:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Associates the line fragment bounds for the specified range of glyphs.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setLineFragmentRect(_ fragmentRect: NSRect, forGlyphRange glyphRange: NSRange, usedRect: NSRect)
```

```objc
- (void) setLineFragmentRect:(NSRect) fragmentRect forGlyphRange:(NSRange) glyphRange usedRect:(NSRect) usedRect;
```

## Discussion

The typesetter must specify the text container first with [`setTextContainer(_:forGlyphRange:)`](./settextcontainer%28_,forglyphrange%29.md), and it sets the exact positions of the glyphs afterwards with [`setLocation(_:forStartOfGlyphRange:)`](./setlocation%28_,forstartofglyphrange%29.md).

In the course of layout, all glyphs should end up being included in a range passed to this method, but only glyphs that start a new line fragment should be at the start of such ranges.

Line fragment rectangles and line fragment used rectangles are always in container coordinates.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `fragmentRect`: The rectangle of the line fragment.
- `glyphRange`: The range of glyphs to be associated with `fragmentRect`.
- `usedRect`: The portion of `fragmentRect` that actually contains glyphs or other marks that are drawn (including the text container’s line fragment padding. Must be equal to or contained within `fragmentRect`.

## See Also

### Setting layout information
- [func setAttachmentSize(NSSize, forGlyphRange: NSRange)](./setattachmentsize%28_,forglyphrange%29.md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](./setdrawsoutsidelinefragment%28_,forglyphat%29.md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(NSRect, usedRect: NSRect, textContainer: NSTextContainer)](./setextralinefragmentrect%28_,usedrect,textcontainer%29.md)
  Sets the bounds and container for the extra line fragment.
- [func setLocation(NSPoint, forStartOfGlyphRange: NSRange)](./setlocation%28_,forstartofglyphrange%29.md)
  Sets the location for the first glyph in the specified range.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](./setnotshownattribute%28_,forglyphat%29.md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setlinefragmentrect(_:forglyphrange:usedrect:))*