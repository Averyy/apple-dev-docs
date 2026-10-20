# unableToIdentifyLanguage

**Framework**: Translation  
**Kind**: property  
**Role**: Type Property

The framework can’t identify the source language automatically.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
static let unableToIdentifyLanguage: TranslationError
```

#### Discussion

The framework throws this error when you call [`prepareTranslation()`](../translationsession/preparetranslation%28%29.md) without specifying the source language, or when using [`status(for:to:)`](../languageavailability/status%28for,to%29.md) and it can’t automatically identify the source language of the sample text you pass in.

> **Note**: For best results in automatic language detection, pass in a sample string of at least 20 characters in length.

## See Also

### Handling general errors
- [static let nothingToTranslate: TranslationError](./nothingtotranslate.md)
  No content to translate.
- [static let internalError: TranslationError](./internalerror.md)
  An error occurred internal to the translation engine.
- [static let alreadyCancelled: TranslationError](./alreadycancelled.md)
  An error describing a translation session that you’ve cancelled before, which prevents the session from producing additional results.
- [static let notInstalled: TranslationError](./notinstalled.md)
  The device doesn’t have the necessary languages downloaded to perform a translation and the session can’t request the person to download them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/unabletoidentifylanguage)*