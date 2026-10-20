# ensureGlyphs(forGlyphRange:)

**Framework**: AppKit  
**Kind**: method  
**Role**: Instance Method

Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func ensureGlyphs(forGlyphRange glyphRange: NSRange)
```

```objc
- (void) ensureGlyphsForGlyphRange:(NSRange) glyphRange;
```

#### Discussion

The layout manager reserves the right to perform glyph generation for larger ranges. If noncontiguous layout is disabled, then the affected range is always effectively extended to start at the beginning of the text.

## Parameters

- `glyphRange`: The glyph range for which glyphs are generated.

## See Also

### Causing glyph generation and layout
- [func ensureGlyphs(forCharacterRange: NSRange)](./ensureglyphs%28forcharacterrange%29.md)
  Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
- [func ensureLayout(forBoundingRect: NSRect, in: NSTextContainer)](./ensurelayout%28forboundingrect,in%29.md)
  Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.
- [func ensureLayout(forCharacterRange: NSRange)](./ensurelayout%28forcharacterrange%29.md)
  Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [func ensureLayout(forGlyphRange: NSRange)](./ensurelayout%28forglyphrange%29.md)
  Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.
- [func ensureLayout(for: NSTextContainer)](./ensurelayout%28for%29.md)
  Forces the layout manager to perform layout for the specified text container if it hasn’t already.
- [var glyphGenerator: NSGlyphGenerator](./glyphgenerator.md)
  The glyph generator that the layout manager uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/ensureglyphs(forglyphrange:))*