# UIFontDescriptor.FeatureKey

**Framework**: UIKit  
**Kind**: struct

Keys for retrieving feature settings.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- tvOS ?+
- visionOS ?+
- watchOS 4.0+

## Declaration

```swift
struct FeatureKey
```

#### Overview

Use these keys when retrieving information from one of the dictionaries associated with the [`featureSettings`](uifontdescriptor/attributename/featuresettings.md) key.

## Topics

### Keys
- [static let type: UIFontDescriptor.FeatureKey](uifontdescriptor/featurekey/type.md)
  A key for identifying the font feature type.
- [static let selector: UIFontDescriptor.FeatureKey](uifontdescriptor/featurekey/selector.md)
  A key for identifying the font feature selector.
### Initializers
- [init(String)](uifontdescriptor/featurekey/init(_:).md)
  Creates a font feature key.
- [init(rawValue: String)](uifontdescriptor/featurekey/init(rawvalue:).md)
  Creates a font feature key with the specified raw value.
### Deprecated
- [static let featureIdentifier: UIFontDescriptor.FeatureKey](uifontdescriptor/featurekey/featureidentifier.md)
  A key for identifying a font feature type.
- [static let typeIdentifier: UIFontDescriptor.FeatureKey](uifontdescriptor/featurekey/typeidentifier.md)
  A key for identifying the font feature selector.

## Relationships

### Conforms To
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

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
- [UIFontDescriptor.TraitKey](uifontdescriptor/traitkey.md)
  Keys for retrieving the font descriptor’s trait information.
- [UIFont.Weight](uifont/weight.md)
  Constants that represent standard typeface styles.
- [UIFont.Width](uifont/width.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/uikit/uifontdescriptor/featurekey)*