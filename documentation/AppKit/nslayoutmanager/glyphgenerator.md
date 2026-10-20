# glyphGenerator

**Framework**: AppKit  
**Kind**: property  
**Role**: Instance Property

The glyph generator that the layout manager uses.

**Availability**:
- macOS

## Declaration

```swift
var glyphGenerator: NSGlyphGenerator { get set }
```

```objc
@property (strong) NSGlyphGenerator * glyphGenerator;
```

#### Discussion

Setting the glyph generator invalidates all glyphs and layout in the layout manager.

## See Also

### Causing glyph generation and layout
- [func ensureGlyphs(forCharacterRange: NSRange)](./ensureglyphs%28forcharacterrange%29.md)
  Forces the layout manager to generate glyphs for the specified character range if it hasn’t already.
- [func ensureGlyphs(forGlyphRange: NSRange)](./ensureglyphs%28forglyphrange%29.md)
  Forces the layout manager to generate glyphs for the specified glyph range if it hasn’t already.
- [func ensureLayout(forBoundingRect: NSRect, in: NSTextContainer)](./ensurelayout%28forboundingrect,in%29.md)
  Forces the layout manager to perform layout for the specified area in the specified text container if it hasn’t already.
- [func ensureLayout(forCharacterRange: NSRange)](./ensurelayout%28forcharacterrange%29.md)
  Forces the layout manager to perform layout for the specified character range if it hasn’t already.
- [func ensureLayout(forGlyphRange: NSRange)](./ensurelayout%28forglyphrange%29.md)
  Forces the layout manager to perform layout for the specified glyph range if it hasn’t already.
- [func ensureLayout(for: NSTextContainer)](./ensurelayout%28for%29.md)
  Forces the layout manager to perform layout for the specified text container if it hasn’t already.


---

*[View on Apple Developer](https://developer.apple.com/documentation/appkit/nslayoutmanager/glyphgenerator)*