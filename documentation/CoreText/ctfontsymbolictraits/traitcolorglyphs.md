# traitColorGlyphs

**Framework**: Core Text  
**Kind**: property  
**Role**: Type Property

The font contains color glyphs.

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
static var traitColorGlyphs: CTFontSymbolicTraits { get }
```

```c
kCTFontTraitColorGlyphs
```

## Discussion

Possible font tables that can contain color glyphs include ‘[sbix](https://developer.apple.com/fonts/TrueType-Reference-Manual/RM06/Chap6sbix.html)’, ‘`COLR`’, and ‘`SVG_`’.

## See Also

### Symbolic Traits
- [static var traitItalic: CTFontSymbolicTraits](./traititalic.md)
  The font typestyle is italic.
- [static var traitBold: CTFontSymbolicTraits](./traitbold.md)
  The font typestyle is boldface.
- [static var traitExpanded: CTFontSymbolicTraits](./traitexpanded.md)
  The font typestyle is expanded.
- [static var traitCondensed: CTFontSymbolicTraits](./traitcondensed.md)
  The font typestyle is condensed.
- [static var traitMonoSpace: CTFontSymbolicTraits](./traitmonospace.md)
  The font uses fixed-pitch glyphs if available.
- [static var traitVertical: CTFontSymbolicTraits](./traitvertical.md)
  The font uses vertical glyph variants and metrics.
- [static var traitUIOptimized: CTFontSymbolicTraits](./traituioptimized.md)
  The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [static var traitComposite: CTFontSymbolicTraits](./traitcomposite.md)
  The font is in Composite Font Reference format.
- [static var traitClassMask: CTFontSymbolicTraits](./traitclassmask.md)
  Mask for the font class.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/traitcolorglyphs)*