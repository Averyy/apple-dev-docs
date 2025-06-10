# localizedLowercase

**Framework**: Foundation  
**Kind**: property

Returns a version of the string with all letters converted to lowercase, taking into account the current locale.

**Availability**:
- iOS 9.0+
- iPadOS 9.0+
- Mac Catalyst 13.1+
- macOS 10.11+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var localizedLowercase: String { get }
```

#### Discussion

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals. See [`lowercased`](nsstring/lowercased.md) for an example.

## See Also

- [var lowercased: String](nsstring/lowercased.md)
  A lowercase representation of the string.
- [func lowercased(with: Locale?) -> String](nsstring/lowercased(with:).md)
  Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [var uppercased: String](nsstring/uppercased.md)
  An uppercase representation of the string.
- [var localizedUppercase: String](nsstring/localizeduppercase.md)
  Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [func uppercased(with: Locale?) -> String](nsstring/uppercased(with:).md)
  Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [var capitalized: String](nsstring/capitalized.md)
  A capitalized representation of the string.
- [var localizedCapitalized: String](nsstring/localizedcapitalized.md)
  Returns a capitalized representation of the receiver using the current locale.
- [func capitalized(with: Locale?) -> String](nsstring/capitalized(with:).md)
  Returns a capitalized representation of the receiver using the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/localizedlowercase)*