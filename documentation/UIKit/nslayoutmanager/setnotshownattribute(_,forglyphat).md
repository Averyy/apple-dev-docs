# setNotShownAttribute(_:forGlyphAt:)

**Framework**: UIKit  
**Kind**: method  
**Role**: Instance Method

Sets the visibility of the glyph at the specified index.

**Availability**:
- iOS 7.0+
- iPadOS 7.0+
- Mac Catalyst 13.1+
- tvOS
- visionOS 1.0+

## Declaration

```swift
func setNotShownAttribute(_ flag: Bool, forGlyphAt glyphIndex: Int)
```

```objc
- (void) setNotShownAttribute:(BOOL) flag forGlyphAtIndex:(NSUInteger) glyphIndex;
```

#### Discussion

The typesetter decides which glyphs are not shown and sets this attribute in the layout manager to ensure that those glyphs are not displayed. For example, a tab or newline character doesn’t leave any marks; it just indicates where following glyphs are laid out.

Raises an `NSRangeException` if `glyphIndex` is out of bounds.

This method is used by the layout mechanism and should be invoked only during typesetting, in almost all cases only by the typesetter. For example, a custom typesetter might invoke it.

## Parameters

- `flag`: If [`true`](../../Swift/true.md), the glyph is not shown; if [`false`](../../Swift/false.md), it is shown.
- `glyphIndex`: Index of the glyph whose attribute is set.

## See Also

### Related Documentation
- [func notShownAttribute(forGlyphAt: Int) -> Bool](./notshownattribute%28forglyphat%29.md)
  Indicates whether the glyph at the specified index has a visible representation.
### Setting layout information
- [func setAttachmentSize(CGSize, forGlyphRange: NSRange)](./setattachmentsize%28_,forglyphrange%29.md)
  Sets the size to use when drawing a glyph that represents an attachment.
- [func setDrawsOutsideLineFragment(Bool, forGlyphAt: Int)](./setdrawsoutsidelinefragment%28_,forglyphat%29.md)
  Indicates whether the specified glyph exceeds the bounds of the line fragment for its layout.
- [func setExtraLineFragmentRect(CGRect, usedRect: CGRect, textContainer: NSTextContainer)](./setextralinefragmentrect%28_,usedrect,textcontainer%29.md)
  Sets the bounds and container for the extra line fragment.
- [func setLineFragmentRect(CGRect, forGlyphRange: NSRange, usedRect: CGRect)](./setlinefragmentrect%28_,forglyphrange,usedrect%29.md)
  Associates the line fragment bounds for the specified range of glyphs.
- [func setLocation(CGPoint, forStartOfGlyphRange: NSRange)](./setlocation%28_,forstartofglyphrange%29.md)
  Sets the location for the first glyph in the specified range.


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/nslayoutmanager/setnotshownattribute(_:forglyphat:))*