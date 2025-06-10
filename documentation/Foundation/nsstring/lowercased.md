# lowercased

**Framework**: Foundation  
**Kind**: property

A lowercase representation of the string.

**Availability**:
- iOS 2.0+
- iPadOS 2.0+
- Mac Catalyst 13.0+
- macOS 10.0+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
var lowercased: String { get }
```

#### Discussion

This property performs the canonical (non-localized) mapping. It is suitable for programming operations that require stable results not depending on the current locale.

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals. That is, the result of this statement:

```objc
lcString = [myString lowercaseString];
```

…might not be equal to this statement:

```objc
lcString = [[myString uppercaseString] lowercaseString];
```

For example, the uppercase form of “ß” in German is “SS”, so converting “Straße” to uppercase, then lowercase, produces this sequence of strings:

- “Straße”
- “STRASSE”
- “strasse”

> ❗ **Important**:  When working with text that’s presented to the user, use [`localizedLowercase`](nsstring/localizedlowercase.md) or [`lowercased(with:)`](nsstring/lowercased(with:).md) instead.

## See Also

- [var localizedLowercase: String](nsstring/localizedlowercase.md)
  Returns a version of the string with all letters converted to lowercase, taking into account the current locale.
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

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/lowercased)*