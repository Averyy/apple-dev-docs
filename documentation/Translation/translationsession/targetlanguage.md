# targetLanguage

**Framework**: Translation  
**Kind**: property  
**Role**: Instance Property

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

## Discussion

If this value is set to `nil`, the session chooses an optimal language to translate into based on the `sourceLanguage` and the person’s [`preferredLanguages`](../../Foundation/locale/preferredlanguages.md).

> **Note**: This value doesn’t update after translation. To see what target language the session uses for a particular translation, check the response [`targetLanguage`](./response/targetlanguage.md).

## See Also

### Getting the language configuration
- [let sourceLanguage: Locale.Language?](./sourcelanguage.md)
  The input language to translate from.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/targetlanguage)*