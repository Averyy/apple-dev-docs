# characterDirection(forLanguage:)

**Framework**: Foundation  
**Kind**: method

Returns the direction of the sequence of characters in a line for the specified ISO language code.

**Availability**:
- iOS 4.0+
- iPadOS 4.0+
- Mac Catalyst 13.1+
- macOS 10.6+
- tvOS 9.0+
- visionOS 1.0+
- watchOS 2.0+

## Declaration

```swift
class func characterDirection(forLanguage isoLangCode: String) -> NSLocale.LanguageDirection
```

#### Return Value

Returns the direction in which characters appear within a line in the specified language. See [`NSLocale.LanguageDirection`](nslocale/languagedirection.md) for possible values. If the appropriate direction can’t be determined [`NSLocale.LanguageDirection.unknown`](nslocale/languagedirection/unknown.md) is returned.

## Parameters

- `isoLangCode`: The ISO language code.

## See Also

- [class func lineDirection(forLanguage: String) -> NSLocale.LanguageDirection](nslocale/linedirection(forlanguage:).md)
  Returns the direction of the sequence of lines for the specified ISO language code.
- [NSLocale.LanguageDirection](nslocale/languagedirection.md)
  The directions that a language may take across a page of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/characterdirection(forlanguage:))*