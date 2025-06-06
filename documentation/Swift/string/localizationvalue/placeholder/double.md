# String.LocalizationValue.Placeholder.double

**Framework**: Swift  
**Kind**: case

The double-precision floating-point type, as used for replacement values with the localized string placeholder syntax.

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
case double
```

#### Discussion

To insert a `double` into a placeholder, use the syntax `\(placeholder: .double)`.

The various `String(localized:)` initializers apply a locale-appropriate `FormatStyle` to the numeric value, based on the `locale:` parameter or the `LocalizedStringResource`.

## See Also

- [String.LocalizationValue.Placeholder.int](string/localizationvalue/placeholder/int.md)
  The signed integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.uint](string/localizationvalue/placeholder/uint.md)
  The unsigned integer type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.float](string/localizationvalue/placeholder/float.md)
  The single-precision floating-point type, as used for replacement values with the localized string placeholder syntax.
- [String.LocalizationValue.Placeholder.object](string/localizationvalue/placeholder/object.md)
  The object type, as used for replacement values with the localized string placeholder syntax.


---

*[View on Apple Developer](https://developer.apple.com/documentation/swift/string/localizationvalue/placeholder/double)*