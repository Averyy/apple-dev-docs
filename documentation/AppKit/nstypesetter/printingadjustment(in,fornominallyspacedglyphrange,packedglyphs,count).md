# printingAdjustment(in:forNominallySpacedGlyphRange:packedGlyphs:count:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Type Method

Returns the interglyph spacing in the specified range when sent to a printer.

**Availability**:
- macOS

## Declaration

```swift
class func printingAdjustment(in layoutMgr: NSLayoutManager, forNominallySpacedGlyphRange nominallySpacedGlyphsRange: NSRange, packedGlyphs: UnsafePointer<UInt8>, count packedGlyphsCount: Int) -> NSSize
```

```objc
+ (NSSize) printingAdjustmentInLayoutManager:(NSLayoutManager *) layoutMgr forNominallySpacedGlyphRange:(NSRange) nominallySpacedGlyphsRange packedGlyphs:(const unsigned char *) packedGlyphs count:(NSUInteger) packedGlyphsCount;
```

## Return Value

The interglyph spacing in the specified range when sent to a printer. If the font metrics of the font used for displaying text on the screen is different from the font metrics of the font used in printing, then this interglyph spacing may need to be adjusted slightly to match that used on the screen.

## Parameters

- `layoutMgr`: The layout manager that will do the drawing.
- `nominallySpacedGlyphsRange`: The range of the glyphs whose spacing is desired.
- `packedGlyphs`: The glyphs as they are packed for sending to be drawn in `layoutMgr`.
- `packedGlyphsCount`: The number of glyphs in `packedGlyphs`.

## See Also

### Getting information about glyphs
- [func baselineOffset(in: NSLayoutManager, glyphIndex: Int) -> CGFloat](./baselineoffset%28in,glyphindex%29.md)
  Returns the distance from the bottom of the line fragment rectangle in which the glyph resides to the glyph baseline.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nstypesetter/printingadjustment(in:fornominallyspacedglyphrange:packedglyphs:count:))*