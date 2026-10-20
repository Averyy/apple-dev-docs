# prepareTranslation()

**Framework**: Translation  
**Kind**: method  
**Role**: Instance Method

Asks for permission to download translation languages without doing any translations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
func prepareTranslation() async throws
```

#### Discussion

If you know ahead of time which languages the person needs to translate, you can prompt them to download those languages in advance by calling this method.

When you call this method, the framework asks the person for permission to download the [`sourceLanguage`](./sourcelanguage.md) and [`targetLanguage`](./targetlanguage.md). If the languages are already installed or in the middle of downloading, the function returns without prompting them.

If you call this function when the `sourceLanguage` is `nil`, it throws [`unableToIdentifyLanguage`](../translationerror/unabletoidentifylanguage.md) error, since there’s no sample text to identify which source language to use for translation.

## See Also

### Preparing for translation
- [TranslationSession.Configuration](./configuration.md)
  A type containing the information to use when performing a translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/preparetranslation())*