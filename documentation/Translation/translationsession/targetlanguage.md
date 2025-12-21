# targetLanguage

**Framework**: Translation  
**Kind**: property

The output language to translate into.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
final let targetLanguage: Locale.Language?
```

#### Discussion

If this value is set to `nil`, the session chooses an optimal language to translate into based on the `sourceLanguage` and the person’s [`preferredLanguages`](https://developer.apple.com/documentation/Foundation/Locale/preferredLanguages).

> **Note**: This value doesn’t update after translation. To see what target language the session uses for a particular translation, check the response [`targetLanguage`](translationsession/response/targetlanguage.md).

## See Also

- [let sourceLanguage: Locale.Language?](translationsession/sourcelanguage.md)
  The input language to translate from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/targetlanguage)*