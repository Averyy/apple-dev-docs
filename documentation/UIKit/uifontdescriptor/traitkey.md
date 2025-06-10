# UIFontDescriptor.TraitKey

**Framework**: UIKit  
**Kind**: struct

Keys for retrieving the font descriptor’s trait information.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 4.0+

## Declaration

```swift
struct TraitKey
```

#### Overview

Use these keys to fetch values from the dictionary associated with the [`traits`](uifontdescriptor/attributename/traits.md) key.

## Topics

### Font traits
- [static let slant: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/slant.md)
  The relative slant angle of the font.
- [static let symbolic: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/symbolic.md)
  The symbolic font traits.
- [static let weight: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/weight.md)
  The numerical value that corresponds to a font face.
- [static let width: UIFontDescriptor.TraitKey](uifontdescriptor/traitkey/width.md)
  The inter-glyph spacing of the font.
### Initializer
- [init(rawValue: String)](uifontdescriptor/traitkey/init(rawvalue:).md)
  Creates a font trait key with the specified raw value.

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
- [UIFontDescriptor.SystemDesign](uifontdescriptor/systemdesign.md)
  Constants that describe the system-defined typeface designs.
- [UIFontDescriptor.SymbolicTraits](uifontdescriptor/symbolictraits-swift.struct.md)
  Constants that describe the stylistic aspects of a font.
- [UIFontDescriptor.Class](uifontdescriptor/class.md)
  Constants that classify certain stylistic qualities of the font.
- [UIFontDescriptor.AttributeName](uifontdescriptor/attributename.md)
  Constants that describe font attributes.
- [UIFontDescriptor.FeatureKey](uifontdescriptor/featurekey.md)
  Keys for retrieving feature settings.
- [UIFont.Weight](uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](uifont/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/traitkey)*