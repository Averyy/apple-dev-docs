# boundsRect(for:glyphRange:)

**Framework**: AppKit  
**Kind**: method

Returns the bounding rectangle that encloses the specified text block and glyph range.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func boundsRect(for block: NSTextBlock, glyphRange: NSRange) -> NSRect
```

#### Return Value

The bounding rectangle, or `NSZeroRect` if no rectangle has been set for the specified block since the last invalidation

#### Discussion

This method causes glyph generation but not layout. Block layout rectangles and bounds rectangles are always in container coordinates.

## Parameters

- `block`: The text block whose bounds rectangle is returned.
- `glyphRange`: The range of glyphs in the text block.

## See Also

- [func setLayoutRect(NSRect, for: NSTextBlock, glyphRange: NSRange)](nslayoutmanager/setlayoutrect(_:for:glyphrange:).md)
  Sets the layout rectangle that encloses the specified text block and glyph range.
- [func layoutRect(for: NSTextBlock, glyphRange: NSRange) -> NSRect](nslayoutmanager/layoutrect(for:glyphrange:).md)
  Returns the rectangle for the layout of the specified text block and glyph range.
- [func setBoundsRect(NSRect, for: NSTextBlock, glyphRange: NSRange)](nslayoutmanager/setboundsrect(_:for:glyphrange:).md)
  Sets the bounding rectangle that encloses the specified text block and glyph range.
- [func layoutRect(for: NSTextBlock, at: Int, effectiveRange: NSRangePointer?) -> NSRect](nslayoutmanager/layoutrect(for:at:effectiverange:).md)
  Returns the rectangle for the layout of the specified text block and glyph.
- [func boundsRect(for: NSTextBlock, at: Int, effectiveRange: NSRangePointer?) -> NSRect](nslayoutmanager/boundsrect(for:at:effectiverange:).md)
  Returns the bounding rectangle for the specified text block and glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/boundsrect(for:glyphrange:))*