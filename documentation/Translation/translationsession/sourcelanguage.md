# sourceLanguage

**Framework**: Translation  
**Kind**: property

The input language to translate from.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
final let sourceLanguage: Locale.Language?
```

#### Discussion

If this value is set to `nil`, the session tries to identify the source language automatically. If it can’t identify the language, it prompts the person to choose the source language to use for the translation.

> **Note**: This value doesn’t update after translation. To see what source language the session uses for a particular translation, check the response [`sourceLanguage`](translationsession/response/sourcelanguage.md).

## See Also

- [let targetLanguage: Locale.Language?](translationsession/targetlanguage.md)
  The output language to translate into.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/sourcelanguage)*