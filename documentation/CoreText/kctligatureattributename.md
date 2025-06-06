# kCTLigatureAttributeName

**Framework**: Core Text  
**Kind**: var

The type of ligatures to use.

**Availability**:
- iOS 3.2+
- iPadOS 3.2+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTLigatureAttributeName: CFString
```

#### Discussion

The value associated with this attribute must be a [`CFNumber`](https://developer.apple.com/documentation/CoreFoundation/CFNumber) object. Default is an integer value of `1`. The ligature attribute determines what kinds of ligatures should be used when displaying the string. A value of `0` indicates that only ligatures essential for proper rendering of text should be used. A value of `1` indicates that standard ligatures should be used, and `2` indicates that all available ligatures should be used. Which ligatures are standard depends on the script and possibly the font. Arabic text, for example, requires ligatures for many character sequences but has a rich set of additional ligatures that combine characters. English text has no essential ligatures, and typically has only two standard ligatures, those for “fi” and “fl”—all others are considered more advanced or fancy.

## See Also

- [let kCTCharacterShapeAttributeName: CFString](kctcharactershapeattributename.md)
  Controls glyph selection.
- [let kCTFontAttributeName: CFString](kctfontattributename.md)
  The font of the text to which this attribute applies.
- [let kCTKernAttributeName: CFString](kctkernattributename.md)
  The amount to kern the next character.
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
- [let kCTBaselineOffsetAttributeName: CFString](kctbaselineoffsetattributename.md)
  Vertical offset for text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctligatureattributename)*