# traitCondensed

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

The font typestyle is condensed.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
static var traitCondensed: CTFontSymbolicTraits { get }
```

```c
kCTFontTraitCondensed
```

## Discussion

Additional detail is available via [`kCTFontWidthTrait`](../kctfontwidthtrait.md).

> ❗ **Important**:  [`expandedTrait`](./expandedtrait.md) and [`condensedTrait`](./condensedtrait.md) are mutually exclusive.

## See Also

### Related Documentation
- [let kCTFontWidthTrait: CFString](../kctfontwidthtrait.md)
  The normalized proportion (width condense or expand) trait from the font traits dictionary.
### Symbolic Traits
- [static var traitItalic: CTFontSymbolicTraits](./traititalic.md)
  The font typestyle is italic.
- [static var traitBold: CTFontSymbolicTraits](./traitbold.md)
  The font typestyle is boldface.
- [static var traitExpanded: CTFontSymbolicTraits](./traitexpanded.md)
  The font typestyle is expanded.
- [static var traitMonoSpace: CTFontSymbolicTraits](./traitmonospace.md)
  The font uses fixed-pitch glyphs if available.
- [static var traitVertical: CTFontSymbolicTraits](./traitvertical.md)
  The font uses vertical glyph variants and metrics.
- [static var traitUIOptimized: CTFontSymbolicTraits](./traituioptimized.md)
  The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [static var traitColorGlyphs: CTFontSymbolicTraits](./traitcolorglyphs.md)
  The font contains color glyphs.
- [static var traitComposite: CTFontSymbolicTraits](./traitcomposite.md)
  The font is in Composite Font Reference format.
- [static var traitClassMask: CTFontSymbolicTraits](./traitclassmask.md)
  Mask for the font class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/traitcondensed)*