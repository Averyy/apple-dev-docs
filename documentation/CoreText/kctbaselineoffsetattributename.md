# kCTBaselineOffsetAttributeName

**Framework**: Core Text  
**Kind**: var

Vertical offset for text position.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
let kCTBaselineOffsetAttributeName: CFString
```

#### Discussion

The value of this attribute must be a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) float. The default is standard positioning, following the baselines of the fonts used.

The baseline offset attribute indicates how many points the characters should be shifted perpendicular to their baseline. For horizontal text, a positive baseline value indicates a shift above the text baseline, and a negative baseline value indicates a shift below the text baseline. For vertical text, a positive baseline value indicates a shift to the right of the text baseline, and a negative baseline value indicates a shift to the left of the text baseline. If this value is set to `0.0`, no baseline shift will be performed.

> ❗ **Important**: This attribute is different from [`baselineOffset`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1526427-baselineoffset). If you are writing code for [`TextKit`](https://developer.apple.com/documentation/AppKit/textkit), you need to use [`baselineOffset`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1526427-baselineoffset).

This attribute is different from [`baselineOffset`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1526427-baselineoffset). If you are writing code for [`TextKit`](https://developer.apple.com/documentation/AppKit/textkit), you need to use [`baselineOffset`](https://developer.apple.com/documentation/foundation/nsattributedstring/key/1526427-baselineoffset).

## See Also

- [let kCTCharacterShapeAttributeName: CFString](kctcharactershapeattributename.md)
  Controls glyph selection.
- [let kCTFontAttributeName: CFString](kctfontattributename.md)
  The font of the text to which this attribute applies.
- [let kCTKernAttributeName: CFString](kctkernattributename.md)
  The amount to kern the next character.
- [let kCTLigatureAttributeName: CFString](kctligatureattributename.md)
  The type of ligatures to use.
- [let kCTForegroundColorAttributeName: CFString](kctforegroundcolorattributename.md)
  The foreground color of the text to which this attribute applies.
- [let kCTForegroundColorFromContextAttributeName: CFString](kctforegroundcolorfromcontextattributename.md)
  Sets a foreground color using the context’s fill color.
- [let kCTParagraphStyleAttributeName: CFString](kctparagraphstyleattributename.md)
  The paragraph style of the text to which this attribute applies.
- [let kCTStrokeWidthAttributeName: CFString](kctstrokewidthattributename.md)
  The stroke width.
- [let kCTStrokeColorAttributeName: CFString](kctstrokecolorattributename.md)
  The stroke color.
- [let kCTSuperscriptAttributeName: CFString](kctsuperscriptattributename.md)
  Controls vertical text positioning.
- [let kCTUnderlineColorAttributeName: CFString](kctunderlinecolorattributename.md)
  The underline color.
- [let kCTUnderlineStyleAttributeName: CFString](kctunderlinestyleattributename.md)
  The style of underlining, to be applied at render time, for the text to which this attribute applies.
- [let kCTVerticalFormsAttributeName: CFString](kctverticalformsattributename.md)
  The orientation of the glyphs in the text to which this attribute applies.
- [let kCTGlyphInfoAttributeName: CFString](kctglyphinfoattributename.md)
  The glyph info object to apply to the text associated with this attribute.
- [let kCTRunDelegateAttributeName: CFString](kctrundelegateattributename.md)
  The run-delegate object to apply to an attribute range of the string.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctbaselineoffsetattributename)*