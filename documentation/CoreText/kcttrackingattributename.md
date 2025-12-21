# kCTTrackingAttributeName

**Framework**: Core Text  
**Kind**: var

The tracking for the text.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```swift
let kCTTrackingAttributeName: CFString
```

#### Discussion

The value associated with this attribute must be a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) float. The default is `0` (no tracking).

Tracking adds space, in points, between the specified [`character cluster`](https://developer.apple.comhttps://unicode.org/reports/tr29/#Grapheme_Cluster_Boundaries). A positive value increases the spacing between characters, while a negative value brings the characters closer together. For example, setting [`kCTTrackingAttributeName`](kcttrackingattributename.md) to 0.1 adds 0.1 point of spacing between each character of the text.

The effect of this attribute is similar to [`kCTKernAttributeName`](kctkernattributename.md), but it treats tracking as trailing whitespace and a nonzero amount disables nonessential ligatures, unless overridden by the presence of [`kCTLigatureAttributeName`](kctligatureattributename.md).

> ❗ **Important**:  If you apply both [`kCTTrackingAttributeName`](kcttrackingattributename.md) and [`kCTKernAttributeName`](kctkernattributename.md), [`kCTTrackingAttributeName`](kcttrackingattributename.md) supersedes [`kCTKernAttributeName`](kctkernattributename.md).

## See Also

- [let kCTKernAttributeName: CFString](kctkernattributename.md)
  The amount to kern the next character.
- [let kCTLigatureAttributeName: CFString](kctligatureattributename.md)
  The type of ligatures to use.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kcttrackingattributename)*