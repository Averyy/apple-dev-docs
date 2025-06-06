# kCTRunDelegateAttributeName

**Framework**: Core Text  
**Kind**: var

The run-delegate object to apply to an attribute range of the string.

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
let kCTRunDelegateAttributeName: CFString
```

#### Discussion

The value must be a [`CTRunDelegate`](ctrundelegate.md) object. The run delegate controls such typographic traits as glyph ascent, descent, and width. The values returned by the embedded run delegate apply to each glyph resulting from the text in that range. Because an embedded object is only a display-time modification, you should avoid applying this attribute to a range of text with complex behavior, such as text having a change of writing direction or having combining marks. It is thus recommended you apply this attribute to a range containing the single character U+FFFC.

## See Also

- [class CTRunDelegate](ctrundelegate.md)
  A run delegate.
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
- [let kCTBaselineOffsetAttributeName: CFString](kctbaselineoffsetattributename.md)
  Vertical offset for text position.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/kctrundelegateattributename)*