# symbolicClass

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

The font’s style is generally design independent.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use [`classSymbolic`](./classsymbolic.md).

## Declaration

```swift
static var symbolicClass: CTFontStylisticClass { get }
```

```c
kCTFontSymbolicClass
```

#### Discussion

Typically assigned to fonts for special characters, such as icons, dingbats, technical symbols, and so on.

## See Also

### Deprecated Constants
- [static var oldStyleSerifsClass: CTFontStylisticClass](./oldstyleserifsclass.md)
  The font’s style is based on the Latin printing style of the 15th to 17th century.
- [static var transitionalSerifsClass: CTFontStylisticClass](./transitionalserifsclass.md)
  The font’s style is based on the Latin printing style of the 18th to 19th century.
- [static var modernSerifsClass: CTFontStylisticClass](./modernserifsclass.md)
  The font’s style is based on the Latin printing style of the 20th century.
- [static var clarendonSerifsClass: CTFontStylisticClass](./clarendonserifsclass.md)
  The font’s style is a variation of the Oldstyle Serifs and the Transitional Serifs.
- [static var slabSerifsClass: CTFontStylisticClass](./slabserifsclass.md)
  The font’s style is characterized by serifs with a square transition between the strokes and the serifs (no brackets).
- [static var freeformSerifsClass: CTFontStylisticClass](./freeformserifsclass.md)
  The font’s style includes serifs but expresses a design freedom that doesn’t generally fit within the other serif design classifications.
- [static var sansSerifClass: CTFontStylisticClass](./sansserifclass.md)
  The font’s style includes most basic letter forms (excluding Scripts and Ornamentals) that do not have serifs on the strokes.
- [static var ornamentalsClass: CTFontStylisticClass](./ornamentalsclass.md)
  The font’s style includes highly decorated or stylized character shapes such as those typically used in headlines.
- [static var scriptsClass: CTFontStylisticClass](./scriptsclass.md)
  The font’s style is among those typefaces designed to simulate handwriting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontstylisticclass/symbolicclass)*