# characterDirection(forLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

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

```objc
+ (NSLocaleLanguageDirection) characterDirectionForLanguage:(NSString *) isoLangCode;
```

#### Return Value

Returns the direction in which characters appear within a line in the specified language. See [`NSLocale.LanguageDirection`](./languagedirection.md) for possible values. If the appropriate direction can’t be determined [`NSLocale.LanguageDirection.unknown`](./languagedirection/unknown.md) is returned.

## Parameters

- `isoLangCode`: The ISO language code.

## See Also

### Getting Line and Character Direction for a Language
- [class func lineDirection(forLanguage: String) -> NSLocale.LanguageDirection](./linedirection%28forlanguage%29.md)
  Returns the direction of the sequence of lines for the specified ISO language code.
- [NSLocale.LanguageDirection](./languagedirection.md)
  The directions that a language may take across a page of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/nslocale/characterdirection(forlanguage:))*