# baselineOffset(in:glyphIndex:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Returns the distance from the bottom of the line fragment rectangle in which the glyph resides to the glyph baseline.

**Availability**:
- macOS

## Declaration

```swift
func baselineOffset(in layoutMgr: NSLayoutManager, glyphIndex: Int) -> CGFloat
```

```objc
- (CGFloat) baselineOffsetInLayoutManager:(NSLayoutManager *) layoutMgr glyphIndex:(NSUInteger) glyphIndex;
```

## Return Value

The distance from the bottom of the line fragment rectangle in which the glyph resides to the glyph baseline.

## Discussion

The text system uses this value to calculate the vertical position of underlines.

## Parameters

- `layoutMgr`: The layout manager used for the drawing.
- `glyphIndex`: The index of the glyph in question.

## See Also

### Getting information about glyphs
- [class func printingAdjustment(in: NSLayoutManager, forNominallySpacedGlyphRange: NSRange, packedGlyphs: UnsafePointer<UInt8>, count: Int) -> NSSize](./printingadjustment%28in,fornominallyspacedglyphrange,packedglyphs,count%29.md)
  Returns the interglyph spacing in the specified range when sent to a printer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/baselineoffset(in:glyphindex:))*