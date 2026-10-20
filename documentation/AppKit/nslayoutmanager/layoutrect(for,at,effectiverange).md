# layoutRect(for:at:effectiveRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the rectangle for the layout of the specified text block and glyph.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func layoutRect(for block: NSTextBlock, at glyphIndex: Int, effectiveRange effectiveGlyphRange: NSRangePointer?) -> NSRect
```

```objc
- (NSRect) layoutRectForTextBlock:(NSTextBlock *) block atIndex:(NSUInteger) glyphIndex effectiveRange:(NSRangePointer) effectiveGlyphRange;
```

#### Return Value

The layout rectangle of the text block, or `NSZeroRect` if no rectangle has been set for the specified block since the last invalidation.

#### Discussion

This method causes glyph generation but not layout. Block layout rectangles and bounds rectangles are always in container coordinates.

## Parameters

- `block`: The text block whose layout rectangle is returned.
- `glyphIndex`: Index of the glyph.
- `effectiveGlyphRange`: If not `NULL`, on output, the range for all glyphs in the text block.

## See Also

### Handling layout for text blocks
- [func setLayoutRect(NSRect, for: NSTextBlock, glyphRange: NSRange)](./setlayoutrect%28_,for,glyphrange%29.md)
  Sets the layout rectangle that encloses the specified text block and glyph range.
- [func layoutRect(for: NSTextBlock, glyphRange: NSRange) -> NSRect](./layoutrect%28for,glyphrange%29.md)
  Returns the rectangle for the layout of the specified text block and glyph range.
- [func setBoundsRect(NSRect, for: NSTextBlock, glyphRange: NSRange)](./setboundsrect%28_,for,glyphrange%29.md)
  Sets the bounding rectangle that encloses the specified text block and glyph range.
- [func boundsRect(for: NSTextBlock, glyphRange: NSRange) -> NSRect](./boundsrect%28for,glyphrange%29.md)
  Returns the bounding rectangle that encloses the specified text block and glyph range.
- [func boundsRect(for: NSTextBlock, at: Int, effectiveRange: NSRangePointer?) -> NSRect](./boundsrect%28for,at,effectiverange%29.md)
  Returns the bounding rectangle for the specified text block and glyph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/layoutrect(for:at:effectiverange:))*