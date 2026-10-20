# setLayoutRect(_:for:glyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Sets the layout rectangle that encloses the specified text block and glyph range.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func setLayoutRect(_ rect: NSRect, for block: NSTextBlock, glyphRange: NSRange)
```

```objc
- (void) setLayoutRect:(NSRect) rect forTextBlock:(NSTextBlock *) block glyphRange:(NSRange) glyphRange;
```

#### Discussion

This method causes glyph generation but not layout. Block layout rectangles and bounds rectangles are always in container coordinates.

## Parameters

- `rect`: The layout rectangle to set.
- `block`: The text block whose layout rectangle is set.
- `glyphRange`: The range of glyphs in the text block.

## See Also

### Handling layout for text blocks
- [func layoutRect(for: NSTextBlock, glyphRange: NSRange) -> NSRect](./layoutrect%28for,glyphrange%29.md)
  Returns the rectangle for the layout of the specified text block and glyph range.
- [func setBoundsRect(NSRect, for: NSTextBlock, glyphRange: NSRange)](./setboundsrect%28_,for,glyphrange%29.md)
  Sets the bounding rectangle that encloses the specified text block and glyph range.
- [func boundsRect(for: NSTextBlock, glyphRange: NSRange) -> NSRect](./boundsrect%28for,glyphrange%29.md)
  Returns the bounding rectangle that encloses the specified text block and glyph range.
- [func layoutRect(for: NSTextBlock, at: Int, effectiveRange: NSRangePointer?) -> NSRect](./layoutrect%28for,at,effectiverange%29.md)
  Returns the rectangle for the layout of the specified text block and glyph.
- [func boundsRect(for: NSTextBlock, at: Int, effectiveRange: NSRangePointer?) -> NSRect](./boundsrect%28for,at,effectiverange%29.md)
  Returns the bounding rectangle for the specified text block and glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/setlayoutrect(_:for:glyphrange:))*