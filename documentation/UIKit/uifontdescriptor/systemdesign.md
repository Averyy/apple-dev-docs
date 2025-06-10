# UIFontDescriptor.SystemDesign

**Framework**: UIKit  
**Kind**: struct

Constants that describe the system-defined typeface designs.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 5.2+

## Declaration

```swift
struct SystemDesign
```

#### Overview

Use these constants to specify a system-provided typeface design, such as:

- SF Pro in iOS or SF Compact in watchOS ([`default`](uifontdescriptor/systemdesign/default.md))
- SF Pro Rounded in iOS or SF Compact Rounded in watchOS ([`rounded`](uifontdescriptor/systemdesign/rounded.md))
- SF Mono ([`monospaced`](uifontdescriptor/systemdesign/monospaced.md))
- New York ([`serif`](uifontdescriptor/systemdesign/serif.md))

## Topics

### Typeface designs
- [static let `default`: UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign/default.md)
  The default typeface for an app’s user interface.
- [static let rounded: UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign/rounded.md)
  The rounded variant of the default typeface.
- [static let monospaced: UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign/monospaced.md)
  The monospace variant of the default typeface.
- [static let serif: UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign/serif.md)
  The serif variant of the default typeface.
### Initializers
- [init(rawValue: String)](uifontdescriptor/systemdesign/init(rawvalue:).md)
  Creates a typeface design constant with the specified raw value.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [UIFont.TextStyle](uifont/textstyle.md)
  Constants that describe the preferred styles for fonts.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [UIFontDescriptor.Class](uifontdescriptor/class.md)
  Constants that classify certain stylistic qualities of the font.
- [UIFontDescriptor.AttributeName](uifontdescriptor/attributename.md)
  Constants that describe font attributes.
- [UIFontDescriptor.FeatureKey](uifontdescriptor/featurekey.md)
  Keys for retrieving feature settings.
- [UIFontDescriptor.TraitKey](uifontdescriptor/traitkey.md)
  Keys for retrieving the font descriptor’s trait information.
- [UIFont.Weight](uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](uifont/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/systemdesign)*