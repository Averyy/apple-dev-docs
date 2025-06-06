# prepareTranslation()

**Framework**: Translation  
**Kind**: method

Asks the user for permission to download translation languages without doing any translations.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
func prepareTranslation() async throws
```

#### Discussion

If you know ahead of time which languages the user needs to translate, you can prompt them to download those languages in advance by calling this method.

When you call this method the framework asks the user for permission to download the [`sourceLanguage`](translationsession/sourcelanguage.md) and [`targetLanguage`](translationsession/targetlanguage.md). If the languages are already installed or are in the middle of downloading, the function returns without prompting the user.

If you call this function when the `sourceLanguage` is `nil`, it throws [`unableToIdentifyLanguage`](translationerror/unabletoidentifylanguage.md) since there’s no sample text to identify which source language to use for translation.

## See Also

- [TranslationSession.Configuration](translationsession/configuration.md)
  A type containing the information to use when performing a translation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationsession/preparetranslation())*