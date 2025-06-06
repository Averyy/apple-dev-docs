# CTFontStylisticClass

**Framework**: Core Text  
**Kind**: struct

The stylistic class values of the font.

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
struct CTFontStylisticClass
```

#### Overview

`CTFontStylisticClass` identifies certain stylistic qualities of the font. These values correspond closely to the font class values in the OpenType OS/2 table. The class values are bundled in the upper four bits of the [`CTFontSymbolicTraits`](ctfontsymbolictraits.md) and can be obtained via [`classMaskTrait`](ctfontsymbolictraits/classmasktrait.md).

## Topics

### Initializers
- [init(rawValue: UInt32)](ctfontstylisticclass/init(rawvalue:).md)
  Creates a stylistic class structure with the specified raw value.
### Stylistic Classes
- [static var classOldStyleSerifs: CTFontStylisticClass](ctfontstylisticclass/classoldstyleserifs.md)
  A font style based on the Latin printing style of the 15th to 17th century.
- [static var classTransitionalSerifs: CTFontStylisticClass](ctfontstylisticclass/classtransitionalserifs.md)
  A font style based on the Latin printing style of the 18th to 19th century.
- [static var classModernSerifs: CTFontStylisticClass](ctfontstylisticclass/classmodernserifs.md)
  A font style based on the Latin printing style of the 20th century.
- [static var classClarendonSerifs: CTFontStylisticClass](ctfontstylisticclass/classclarendonserifs.md)
  A font style variation of the Oldstyle Serifs and the Transitional Serifs.
- [static var classSlabSerifs: CTFontStylisticClass](ctfontstylisticclass/classslabserifs.md)
  A font style characterized by serifs with a square transition between the strokes and the serifs (no brackets).
- [static var classFreeformSerifs: CTFontStylisticClass](ctfontstylisticclass/classfreeformserifs.md)
  A font style that includes serifs but expresses a design freedom that doesn’t generally fit within the other serif design classifications.
- [static var classSansSerif: CTFontStylisticClass](ctfontstylisticclass/classsansserif.md)
  A font style that includes most basic letter forms (excluding Scripts and Ornamentals) that do not have serifs on the strokes.
- [static var classOrnamentals: CTFontStylisticClass](ctfontstylisticclass/classornamentals.md)
  A font style that includes highly decorated or stylized character shapes such as those typically used in headlines.
- [static var classScripts: CTFontStylisticClass](ctfontstylisticclass/classscripts.md)
  A font style among those typefaces designed to simulate handwriting.
- [static var classSymbolic: CTFontStylisticClass](ctfontstylisticclass/classsymbolic.md)
  A generally design-independent font style.
### Deprecated Constants
- [static var oldStyleSerifsClass: CTFontStylisticClass](ctfontstylisticclass/oldstyleserifsclass.md)
  The font’s style is based on the Latin printing style of the 15th to 17th century.
- [static var transitionalSerifsClass: CTFontStylisticClass](ctfontstylisticclass/transitionalserifsclass.md)
  The font’s style is based on the Latin printing style of the 18th to 19th century.
- [static var modernSerifsClass: CTFontStylisticClass](ctfontstylisticclass/modernserifsclass.md)
  The font’s style is based on the Latin printing style of the 20th century.
- [static var clarendonSerifsClass: CTFontStylisticClass](ctfontstylisticclass/clarendonserifsclass.md)
  The font’s style is a variation of the Oldstyle Serifs and the Transitional Serifs.
- [static var slabSerifsClass: CTFontStylisticClass](ctfontstylisticclass/slabserifsclass.md)
  The font’s style is characterized by serifs with a square transition between the strokes and the serifs (no brackets).
- [static var freeformSerifsClass: CTFontStylisticClass](ctfontstylisticclass/freeformserifsclass.md)
  The font’s style includes serifs but expresses a design freedom that doesn’t generally fit within the other serif design classifications.
- [static var sansSerifClass: CTFontStylisticClass](ctfontstylisticclass/sansserifclass.md)
  The font’s style includes most basic letter forms (excluding Scripts and Ornamentals) that do not have serifs on the strokes.
- [static var ornamentalsClass: CTFontStylisticClass](ctfontstylisticclass/ornamentalsclass.md)
  The font’s style includes highly decorated or stylized character shapes such as those typically used in headlines.
- [static var scriptsClass: CTFontStylisticClass](ctfontstylisticclass/scriptsclass.md)
  The font’s style is among those typefaces designed to simulate handwriting.
- [static var symbolicClass: CTFontStylisticClass](ctfontstylisticclass/symbolicclass.md)
  The font’s style is generally design independent.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [ExpressibleByArrayLiteral](../Swift/ExpressibleByArrayLiteral.md)
- [OptionSet](../Swift/OptionSet.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SetAlgebra](../Swift/SetAlgebra.md)

## See Also

- [Font Traits](font-traits.md)
  The keys for accessing font traits from a font descriptor.
- [Font Class Mask Shift Constants](font-class-mask-shift-constants.md)
  These constants represent the font class mask shift.
- [struct CTFontSymbolicTraits](ctfontsymbolictraits.md)
  The symbolic representation of stylistic font attributes.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctfontstylisticclass)*