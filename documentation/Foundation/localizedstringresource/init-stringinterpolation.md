# init(stringInterpolation:)

**Framework**: Foundation  
**Kind**: init

Creates a localized string resource from the given string interpolation.

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
init(stringInterpolation: String.LocalizationValue.StringInterpolation)
```

#### Discussion

To create a localized string key from a string interpolation, use the `\()` string interpolation syntax. Swift matches the parameter types in the expression to one of the `appendInterpolation` methods in `LocalizedStringResource/StringInterpolation`.

This initializer uses the default values from `LocalizedStringResource/init(_:table:locale:bundle:comment:)` for the `table`, `locale`, `bundle`, and `comment`.

## Parameters

- `stringInterpolation`: The key to use when looking up a localized value, created from a string interpolation.

## See Also

- [init(stringLiteral: String)](localizedstringresource/init(stringliteral:).md)
  Creates a localized string resource from the specified string literal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource/init(stringinterpolation:))*