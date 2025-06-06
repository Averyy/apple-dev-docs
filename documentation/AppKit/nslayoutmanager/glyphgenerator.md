# glyphGenerator

**Framework**: AppKit  
**Kind**: property

The glyph generator that the layout manager uses.

**Availability**:
- macOS ?+

## Declaration

```swift
var glyphGenerator: NSGlyphGenerator { get set }
```

#### Discussion

Setting the glyph generator invalidates all glyphs and layout in the layout manager.

## See Also

- [func ensureGlyphs(forCharacterRange: NSRange)](nslayoutmanager/ensureglyphs(forcharacterrange:).md)
  Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphgenerator)*