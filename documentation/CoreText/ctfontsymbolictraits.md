# CTFontSymbolicTraits

**Framework**: Core Text  
**Kind**: struct

The symbolic representation of stylistic font attributes.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct CTFontSymbolicTraits
```

#### Overview

`CTFontSymbolicTraits` symbolically describes stylistic aspects of a font. The upper 16 bits are used to describe appearance of the font, whereas the lower 16 bits are for typeface information. The font appearance information represented by the upper 16 bits can be used for stylistic font matching.

## Topics

### Initializers
- [init(rawValue: UInt32)](ctfontsymbolictraits/init(rawvalue:).md)
  Creates a symbolic traits structure with the specified raw value.
### Symbolic Traits
- [static var traitItalic: CTFontSymbolicTraits](ctfontsymbolictraits/traititalic.md)
  The font typestyle is italic.
- [static var traitBold: CTFontSymbolicTraits](ctfontsymbolictraits/traitbold.md)
  The font typestyle is boldface.
- [static var traitExpanded: CTFontSymbolicTraits](ctfontsymbolictraits/traitexpanded.md)
  The font typestyle is expanded.
- [static var traitCondensed: CTFontSymbolicTraits](ctfontsymbolictraits/traitcondensed.md)
  The font typestyle is condensed.
- [static var traitMonoSpace: CTFontSymbolicTraits](ctfontsymbolictraits/traitmonospace.md)
  The font uses fixed-pitch glyphs if available.
- [static var traitVertical: CTFontSymbolicTraits](ctfontsymbolictraits/traitvertical.md)
  The font uses vertical glyph variants and metrics.
- [static var traitUIOptimized: CTFontSymbolicTraits](ctfontsymbolictraits/traituioptimized.md)
  The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [static var traitColorGlyphs: CTFontSymbolicTraits](ctfontsymbolictraits/traitcolorglyphs.md)
  The font contains color glyphs.
- [static var traitComposite: CTFontSymbolicTraits](ctfontsymbolictraits/traitcomposite.md)
  The font is in Composite Font Reference format.
- [static var traitClassMask: CTFontSymbolicTraits](ctfontsymbolictraits/traitclassmask.md)
  Mask for the font class.
### Deprecated Constants
- [static var italicTrait: CTFontSymbolicTraits](ctfontsymbolictraits/italictrait.md)
  The font typestyle is italic.
- [static var boldTrait: CTFontSymbolicTraits](ctfontsymbolictraits/boldtrait.md)
  The font typestyle is boldface.
- [static var expandedTrait: CTFontSymbolicTraits](ctfontsymbolictraits/expandedtrait.md)
  The font typestyle is expanded.
- [static var condensedTrait: CTFontSymbolicTraits](ctfontsymbolictraits/condensedtrait.md)
  The font typestyle is condensed.
- [static var monoSpaceTrait: CTFontSymbolicTraits](ctfontsymbolictraits/monospacetrait.md)
  The font uses fixed-pitch glyphs if available.
- [static var verticalTrait: CTFontSymbolicTraits](ctfontsymbolictraits/verticaltrait.md)
  The font uses vertical glyph variants and metrics.
- [static var uiOptimizedTrait: CTFontSymbolicTraits](ctfontsymbolictraits/uioptimizedtrait.md)
  The font synthesizes appropriate attributes for user interface rendering, such as control titles, if necessary.
- [static var colorGlyphsTrait: CTFontSymbolicTraits](ctfontsymbolictraits/colorglyphstrait.md)
  The font contains color glyphs.
- [static var compositeTrait: CTFontSymbolicTraits](ctfontsymbolictraits/compositetrait.md)
  The font is in Composite Font Reference format.
- [static var classMaskTrait: CTFontSymbolicTraits](ctfontsymbolictraits/classmasktrait.md)
  Mask for the font class.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Font Traits](font-traits.md)
  The keys for accessing font traits from a font descriptor.
- [Font Class Mask Shift Constants](font-class-mask-shift-constants.md)
  These constants represent the font class mask shift.
- [struct CTFontStylisticClass](ctfontstylisticclass.md)
  The stylistic class values of the font.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontsymbolictraits)*