# monoSpaceTrait

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

The font uses fixed-pitch glyphs if available.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

> **Deprecated**: Use [`traitMonoSpace`](./traitmonospace.md).

## Declaration

```swift
static var monoSpaceTrait: CTFontSymbolicTraits { get }
```

```c
kCTFontMonoSpaceTrait
```

#### Discussion

The font may have multiple glyph advances (many CJK glyphs contain two spaces).

## See Also

### Deprecated Constants
- [static var italicTrait: CTFontSymbolicTraits](./italictrait.md)
  The font typestyle is italic.
- [static var boldTrait: CTFontSymbolicTraits](./boldtrait.md)
  The font typestyle is boldface.
- [static var expandedTrait: CTFontSymbolicTraits](./expandedtrait.md)
  The font typestyle is expanded.
- [static var condensedTrait: CTFontSymbolicTraits](./condensedtrait.md)
  The font typestyle is condensed.
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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/monospacetrait)*