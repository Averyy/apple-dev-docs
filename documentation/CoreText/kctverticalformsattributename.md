# kCTVerticalFormsAttributeName

**Framework**: Core Text  
**Kind**: var

The orientation of the glyphs in the text to which this attribute applies.

**Availability**:
- iOS 4.3+
- iPadOS 4.3+
- Mac Catalyst 13.1+
- macOS 10.5+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
let kCTVerticalFormsAttributeName: CFString
```

#### Discussion

Value must be a [`CFBoolean`](https://developer.apple.com/documentation/CoreFoundation/CFBoolean) object. Default is [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse). A value of [`kCFBooleanFalse`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanFalse) indicates that horizontal glyph forms are to be used; [`kCFBooleanTrue`](https://developer.apple.com/documentation/CoreFoundation/kCFBooleanTrue) indicates that vertical glyph forms are to be used.

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
- [let kCTGlyphInfoAttributeName: CFString](kctglyphinfoattributename.md)
  The glyph info object to apply to the text associated with this attribute.
- [let kCTRunDelegateAttributeName: CFString](kctrundelegateattributename.md)
  The run-delegate object to apply to an attribute range of the string.
- [let kCTBaselineOffsetAttributeName: CFString](kctbaselineoffsetattributename.md)
  Vertical offset for text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctverticalformsattributename)*