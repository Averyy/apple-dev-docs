# String.LocalizationValue.Placeholder

**Framework**: Swift  
**Kind**: enum

An enumeration of types that can appear as a placeholder in a string interpolation.

**Availability**:
- iOS 16.0+
- iPadOS 16.0+
- Mac Catalyst 16.0+
- macOS 13.0+
- tvOS 16.0+
- visionOS 1.0+
- watchOS 9.0+

## Declaration

```swift
enum Placeholder
```

#### Overview

Foundation uses this type when you create a string with the `\(placeholder: type)` syntax and supply an array of replacement values in a `String.LocalizationOptions`. Placeholders work with [`String`](string.md) initializers that take an `options:` parameter:

- [`init(localized:options:table:bundle:locale:comment:)`](string/init(localized:options:table:bundle:locale:comment:).md)
- [`init(localized:options:)`](string/init(localized:options:).md)
- [`init(localized:defaultValue:options:table:bundle:locale:comment:)`](string/init(localized:defaultvalue:options:table:bundle:locale:comment:).md)

You only use this type directly when specifying one of its enumeration cases in the placeholder syntax, like `\(placeholder: .int)`.

## Topics

### Placeholder types
- [String.LocalizationValue.Placeholder.int](string/localizationvalue/placeholder/int.md)
  The signed integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.uint](string/localizationvalue/placeholder/uint.md)
  The unsigned integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.float](string/localizationvalue/placeholder/float.md)
  The single-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.double](string/localizationvalue/placeholder/double.md)
  The double-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.object](string/localizationvalue/placeholder/object.md)
  The object type, as used for replacement values with the localized string placeholder syntax.

## Relationships

### Conforms To
- [Decodable](decodable.md)
- [Encodable](encodable.md)
- [Equatable](equatable.md)
- [Hashable](hashable.md)
- [Sendable](sendable.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/localizationvalue/placeholder)*