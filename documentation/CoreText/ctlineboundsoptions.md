# CTLineBoundsOptions

**Framework**: Core Text  
**Kind**: struct

Options for getting the bounds of a line of text.

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
struct CTLineBoundsOptions
```

#### Overview

Passing `0` (no options) returns the typographic bounds, including typographic leading and shifts.

## Topics

### Line Bounds Options
- [static var excludeTypographicLeading: CTLineBoundsOptions](ctlineboundsoptions/excludetypographicleading.md)
  An option to exclude typographic leading.
- [static var excludeTypographicShifts: CTLineBoundsOptions](ctlineboundsoptions/excludetypographicshifts.md)
  An option to ignore cross-stream shifts due to positioning, such as kerning or baseline alignment.
- [static var includeLanguageExtents: CTLineBoundsOptions](ctlineboundsoptions/includelanguageextents.md)
  An option to include additional space based on common glyph sequences for various languages.
- [static var useGlyphPathBounds: CTLineBoundsOptions](ctlineboundsoptions/useglyphpathbounds.md)
  An option to use glyph path bounds rather than the default typographic bounds.
- [static var useHangingPunctuation: CTLineBoundsOptions](ctlineboundsoptions/usehangingpunctuation.md)
  An option to enable hanging punctuation.
- [static var useOpticalBounds: CTLineBoundsOptions](ctlineboundsoptions/useopticalbounds.md)
  An option to use optical bounds.
### Initializers
- [init(rawValue: CFOptionFlags)](ctlineboundsoptions/init(rawvalue:).md)
  Creates a line bound options enumeration with the specified raw value.

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

- [enum CTFontDescriptorMatchingState](ctfontdescriptormatchingstate.md)
  Constants that track the progress of font descriptor matching.
- [enum CTFontManagerAutoActivationSetting](ctfontmanagerautoactivationsetting.md)
  Sets the auto-activation for the specified bundle identifier.
- [enum CTFontManagerError](ctfontmanagererror.md)
  Errors that prevent unregistration of fonts for a specified font file URL.
- [enum CTFontManagerScope](ctfontmanagerscope.md)
  Constants that define the scope for font registration.
- [enum CTRubyAlignment](ctrubyalignment.md)
  Constants that specify how to align the ruby text and the base text relative to each other when they have different lengths.
- [enum CTRubyOverhang](ctrubyoverhang.md)
  Constants that specify whether, and on which side, ruby text can overhang adjacent text if it’s wider than the base text.
- [enum CTRubyPosition](ctrubyposition.md)
  Constants that specify the position of the ruby text relative to to the base text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/coretext/ctlineboundsoptions)*