# uppercased(with:)

**Framework**: Foundation  
**Kind**: method

Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.

**Availability**:
- iOS 6.0+
- iPadOS 6.0+
- Mac Catalyst 13.1+
- macOS 10.8+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
func uppercased(with locale: Locale?) -> String
```

#### Return Value

An uppercase string using the `locale`.

## Parameters

- `locale`: The locale. For strings presented to users, pass the current locale ([   ]). To use the system locale, pass  .

## See Also

- [var lowercased: String](nsstring/lowercased.md)
  A lowercase representation of the string.
- [var localizedLowercase: String](nsstring/localizedlowercase.md)
  Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
- [func lowercased(with: Locale?) -> String](nsstring/lowercased(with:).md)
  Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [var uppercased: String](nsstring/uppercased.md)
  An uppercase representation of the string.
- [var localizedUppercase: String](nsstring/localizeduppercase.md)
  Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [var capitalized: String](nsstring/capitalized.md)
  A capitalized representation of the string.
- [var localizedCapitalized: String](nsstring/localizedcapitalized.md)
  Returns a capitalized representation of the receiver using the current locale.
- [func capitalized(with: Locale?) -> String](nsstring/capitalized(with:).md)
  Returns a capitalized representation of the receiver using the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/uppercased(with:))*