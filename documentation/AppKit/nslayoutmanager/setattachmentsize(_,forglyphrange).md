# setAttachmentSize(_:forGlyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the size to use when drawing a glyph that represents an attachment.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setAttachmentSize(_ attachmentSize: NSSize, forGlyphRange glyphRange: NSRange)
```

```objc
- (void) setAttachmentSize:(NSSize) attachmentSize forGlyphRange:(NSRange) glyphRange;
```

## Discussion

For a glyph corresponding to an attachment, this method should be called to set the size for the attachment cell to occupy. The glyph’s value should be [`NSControlGlyph`](../nscontrolglyph.md).

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `attachmentSize`: The glyph size to set.
- `glyphRange`: The attachment glyph’s position in the glyph stream.

## See Also

### Setting layout information
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](./setdrawsoutsidelinefragment%28_,forglyphat%29.md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(NSRect, usedRect: NSRect, textContainer: NSTextContainer)](./setextralinefragmentrect%28_,usedrect,textcontainer%29.md)
  Sets the bounds and container for the extra line fragment.
- [func setLineFragmentRect(NSRect, forGlyphRange: NSRange, usedRect: NSRect)](./setlinefragmentrect%28_,forglyphrange,usedrect%29.md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setLocation(NSPoint, forStartOfGlyphRange: NSRange)](./setlocation%28_,forstartofglyphrange%29.md)
  Sets the location for the first glyph in the specified range.
- [func setNotShownAttribute(Bool, forGlyphAt: Int)](./setnotshownattribute%28_,forglyphat%29.md)
  Sets the visibility of the glyph at the specified index.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setattachmentsize(_:forglyphrange:))*