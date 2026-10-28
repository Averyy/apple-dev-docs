# setBoundsRect(_:for:glyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the bounding rectangle that encloses the specified text block and glyph range.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setBoundsRect(_ rect: NSRect, for block: NSTextBlock, glyphRange: NSRange)
```

```objc
- (void) setBoundsRect:(NSRect) rect forTextBlock:(NSTextBlock *) block glyphRange:(NSRange) glyphRange;
```

## Discussion

This method causes glyph generation but not layout. Block layout rectangles and bounds rectangles are always in container coordinates.

## Parameters

- `rect`: The bounding rectangle to set.
- `block`: The text block whose bounding rectangle is set.
- `glyphRange`: The range of glyphs in the text block.

## See Also

### Handling layout for text blocks
- [func setLayoutRect(NSRect, for: NSTextBlock, glyphRange: NSRange)](./setlayoutrect%28_,for,glyphrange%29.md)
  Sets the layout rectangle that encloses the specified text block and glyph range.
- [func layoutRect(for: NSTextBlock, glyphRange: NSRange) -> NSRect](./layoutrect%28for,glyphrange%29.md)
  Returns the rectangle for the layout of the specified text block and glyph range.
- [func boundsRect(for: NSTextBlock, glyphRange: NSRange) -> NSRect](./boundsrect%28for,glyphrange%29.md)
  Returns the bounding rectangle that encloses the specified text block and glyph range.
- [func layoutRect(for: NSTextBlock, at: Int, effectiveRange: NSRangePointer?) -> NSRect](./layoutrect%28for,at,effectiverange%29.md)
  Returns the rectangle for the layout of the specified text block and glyph.
- [func boundsRect(for: NSTextBlock, at: Int, effectiveRange: NSRangePointer?) -> NSRect](./boundsrect%28for,at,effectiverange%29.md)
  Returns the bounding rectangle for the specified text block and glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setboundsrect(_:for:glyphrange:))*