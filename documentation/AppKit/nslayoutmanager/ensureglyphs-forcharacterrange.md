# ensureGlyphs(forCharacterRange:)

**Framework**: AppKit  
**Kind**: method

Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.

**Availability**:
- macOS 10.7+

## Declaration

```swift
func ensureGlyphs(forCharacterRange charRange: NSRange)
```

#### Discussion

The layout manager reserves the right to perform glyph generation for larger ranges. If noncontiguous layout is disabled, then the affected range is always effectively extended to start at the beginning of the text.

## Parameters

- `charRange`: The character range for which glyphs are generated.

## See Also

- [func ensureGlyphs(forGlyphRange: NSRange)](nslayoutmanager/ensureglyphs(forglyphrange:).md)
  Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.
- [func ensureLayout(forBoundingRect: NSRect, in: NSTextContainer)](nslayoutmanager/ensurelayout(forboundingrect:in:).md)
  Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.
- [func ensureLayout(forCharacterRange: NSRange)](nslayoutmanager/ensurelayout(forcharacterrange:).md)
  Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [func ensureLayout(forGlyphRange: NSRange)](nslayoutmanager/ensurelayout(forglyphrange:).md)
  Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.
- [func ensureLayout(for: NSTextContainer)](nslayoutmanager/ensurelayout(for:).md)
  Forces the layout manager to perform layout for the specified text container if it hasn’t already.
- [var glyphGenerator: NSGlyphGenerator](nslayoutmanager/glyphgenerator.md)
  The glyph generator that the layout manager uses.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/ensureglyphs(forcharacterrange:))*