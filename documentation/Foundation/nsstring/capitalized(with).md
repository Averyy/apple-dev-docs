# capitalized(with:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Instance Method

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

```objc
- (NSString *) capitalizedStringWithLocale:(NSLocale *) locale;
```

## Return Value

A string with the first character from each word in the receiver changed to its corresponding uppercase value, and all remaining characters set to their corresponding lowercase values.

## Discussion

A capitalized string is a string with the first character in each word changed to its corresponding uppercase value, and all remaining characters set to their corresponding lowercase values. A “word” is any sequence of characters delimited by spaces, tabs, or line terminators (listed under [`getLineStart(_:end:contentsEnd:for:)`](./getlinestart%28_,end,contentsend,for%29.md)). Some common word delimiting punctuation isn’t considered, so this property may not generally produce the desired results for multiword strings.

Case transformations aren’t guaranteed to be symmetrical or to produce strings of the same lengths as the originals. See [`lowercased`](./lowercased.md) for an example.

## Parameters

- `locale`: The locale. For strings presented to users, pass the current locale ([[`NSLocale`](../nslocale.md) [`current`](../nslocale/current.md)]). To use the system locale, pass `nil`.

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
- [var localizedUppercase: String](./localizeduppercase.md)
  Returns a version of the string with all letters converted to uppercase, taking into account the current locale.
- [func uppercased(with: Locale?) -> String](./uppercased%28with%29.md)
  Returns a version of the string with all letters converted to uppercase, taking into account the specified locale.
- [var capitalized: String](./capitalized.md)
  A capitalized representation of the string.
- [var localizedCapitalized: String](./localizedcapitalized.md)
  Returns a capitalized representation of the receiver using the current locale.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nsstring/capitalized(with:))*