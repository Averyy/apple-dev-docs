# traitMonoSpace

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

## Declaration

```swift
static var traitMonoSpace: CTFontSymbolicTraits { get }
```

```c
kCTFontTraitMonoSpace
```

#### Discussion

The font may have multiple glyph advances (many CJK glyphs contain two spaces).

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

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits/traitmonospace)*