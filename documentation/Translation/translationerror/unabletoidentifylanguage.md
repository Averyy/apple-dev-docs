# unableToIdentifyLanguage

**Framework**: Translation  
**Kind**: property

The framework can’t identify the source language automatically.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
static let unableToIdentifyLanguage: TranslationError
```

#### Discussion

This error is thrown when you call [`prepareTranslation()`](translationsession/preparetranslation().md) without specifying the source language, or when using [`status(for:to:)`](languageavailability/status(for:to:).md) and the system can’t automatically identify the source language of the sample text you pass in.

> **Note**: For best results in automatic language detection, pass in a sample string of at least 20 characters in length.

For best results in automatic language detection, pass in a sample string of at least 20 characters in length.

## See Also

- [static let nothingToTranslate: TranslationError](translationerror/nothingtotranslate.md)
  No content to translate.
- [static let internalError: TranslationError](translationerror/internalerror.md)
  An error occurred internal to the translation engine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/unabletoidentifylanguage)*