# italicTrait

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

The font typestyle is italic.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use [`traitItalic`](./traititalic.md).

## Declaration

```swift
static var italicTrait: CTFontSymbolicTraits { get }
```

```c
kCTFontItalicTrait
```

#### Discussion

Additional detail is available via [`kCTFontSlantTrait`](../kctfontslanttrait.md).

## See Also

### Related Documentation
- [let kCTFontSlantTrait: CFString](../kctfontslanttrait.md)
  The normalized slant angle from the font traits dictionary.
### Deprecated Constants
- [static var boldTrait: CTFontSymbolicTraits](./boldtrait.md)
  The font typestyle is boldface.
- [static var expandedTrait: CTFontSymbolicTraits](./expandedtrait.md)
  The font typestyle is expanded.
- [static var condensedTrait: CTFontSymbolicTraits](./condensedtrait.md)
  The font typestyle is condensed.
- [static var monoSpaceTrait: CTFontSymbolicTraits](./monospacetrait.md)
  The font uses fixed-pitch glyphs if available.
- [static var verticalTrait: CTFontSymbolicTraits](./verticaltrait.md)
  The font uses vertical glyph variants and metrics.
- [static var uiOptimizedTrait: CTFontSymbolicTraits](./uioptimizedtrait.md)
  The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [static var colorGlyphsTrait: CTFontSymbolicTraits](./colorglyphstrait.md)
  The font contains color glyphs.
- [static var compositeTrait: CTFontSymbolicTraits](./compositetrait.md)
  The font is in Composite Font Reference format.
- [static var classMaskTrait: CTFontSymbolicTraits](./classmasktrait.md)
  Mask for the font class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/italictrait)*