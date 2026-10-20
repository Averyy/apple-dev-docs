# lineDirection(forLanguage:)

**Framework**: Foundation  
**Kind**: method  
**Role**: Type Method

Returns the line direction for a specified language code.

**Availability**:
- iOS 8.0+ - Deprecated in 16.0
- iPadOS 8.0+ - Deprecated in 16.0
- Mac Catalyst 8.0+ - Deprecated in 16.0
- macOS 10.10+ - Deprecated in 13.0
- tvOS 9.0+ - Deprecated in 16.0
- visionOS 1.0+
- watchOS 2.0+ - Deprecated in 9.0

> **Deprecated**: Use `Locale.Language(identifier:).lineLayoutDirection`

## Declaration

```swift
static func lineDirection(forLanguage isoLangCode: String) -> Locale.LanguageDirection
```

## See Also

### Getting line and character direction for a language
- [static func characterDirection(forLanguage: String) -> Locale.LanguageDirection](./characterdirection%28forlanguage%29.md)
  Returns the character direction for a specified language code.
- [typealias LanguageDirection](./languagedirection.md)
  An alias for the standard set of language directions.
- [NSLocale.LanguageDirection](../nslocale/languagedirection.md)
  The directions that a language may take across a page of text.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundation/locale/linedirection(forlanguage:))*