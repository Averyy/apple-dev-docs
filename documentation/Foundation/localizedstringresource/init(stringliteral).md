# init(stringLiteral:)

**Framework**: Foundation  
**Kind**: init  
**Role**: Initializer

Creates a localized string resource from the specified string literal.

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
init(stringLiteral value: String)
```

#### Discussion

This initializer uses the default values from `LocalizedStringResource/init(_:table:locale:bundle:comment:)` for the `table`, `locale`, `bundle`, and `comment`.

## Parameters

- `value`: The key to use when looking up a localized value.

## See Also

### Creating a localized string resource from literal values
- [init(stringInterpolation: String.LocalizationValue.StringInterpolation)](./init%28stringinterpolation%29.md)
  Creates a localized string resource from the given string interpolation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/localizedstringresource/init(stringliteral:))*