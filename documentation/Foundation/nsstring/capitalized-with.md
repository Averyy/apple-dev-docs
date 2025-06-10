# capitalized(with:)

**Framework**: Foundation  
**Kind**: method

Returns a capitalized representation of the receiver using the specified locale.

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
func capitalized(with locale: Locale?) -> String
```

#### Return Value

A string with the first character from each word in the receiver changed to its corresponding uppercase value, and all remaining characters set to their corresponding lowercase values.

#### Discussion

A capitalized string is a string with the first character in each word changed to its corresponding uppercase value, and all remaining characters set to their corresponding lowercase values. A “word” is any sequence of characters delimited by spaces, tabs, or line terminators (listed under [`getLineStart(_:end:contentsEnd:for:)`](nsstring/getlinestart(_:end:contentsend:for:).md)). Some common word delimiting punctuation isn’t considered, so this property may not generally produce the desired results for multiword strings.

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals. See [`lowercased`](nsstring/lowercased.md) for an example.

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
- [func uppercased(with: Locale?) -> String](nsstring/uppercased(with:).md)
  Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [var capitalized: String](nsstring/capitalized.md)
  A capitalized representation of the string.
- [var localizedCapitalized: String](nsstring/localizedcapitalized.md)
  Returns a capitalized representation of the receiver using the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/capitalized(with:))*