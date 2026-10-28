# localizedUppercase

**Framework**: Foundation  
**Kind**: property  
**Role**: Instance Property

Returns a version of the string with all letters converted to uppercase, taking into account the current locale.

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
var localizedUppercase: String { get }
```

```objc
@property (copy, readonly) NSString * localizedUppercaseString;
```

## Discussion

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals. See [`lowercased`](./lowercased.md) for an example.

## See Also

### Changing Case
- [var lowercased: String](./lowercased.md)
  A lowercase representation of the string.
- [var localizedLowercase: String](./localizedlowercase.md)
  Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
- [func lowercased(with: Locale?) -> String](./lowercased%28with%29.md)
  Returns a version of the string with all letters converted to lowercase, taking into account the specified locale.
- [var uppercased: String](./uppercased.md)
  An uppercase representation of the string.
- [func uppercased(with: Locale?) -> String](./uppercased%28with%29.md)
  Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [var capitalized: String](./capitalized.md)
  A capitalized representation of the string.
- [var localizedCapitalized: String](./localizedcapitalized.md)
  Returns a capitalized representation of the receiver using the current locale.
- [func capitalized(with: Locale?) -> String](./capitalized%28with%29.md)
  Returns a capitalized representation of the receiver using the specified locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/localizeduppercase)*