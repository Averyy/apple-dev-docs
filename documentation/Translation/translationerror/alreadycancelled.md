# alreadyCancelled

**Framework**: Translation  
**Kind**: property

An error describing a translation session that you’ve cancelled before, which prevents the session from producing additional results.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)

## Declaration

```swift
static let alreadyCancelled: TranslationError
```

#### Discussion

A [`TranslationSession`](translationsession.md) instance throws this error when you call one of its translate methods after calling its [`cancel()`](translationsession/cancel().md) method.

## See Also

- [static let nothingToTranslate: TranslationError](translationerror/nothingtotranslate.md)
  No content to translate.
- [static let unableToIdentifyLanguage: TranslationError](translationerror/unabletoidentifylanguage.md)
  The framework can’t identify the source language automatically.
- [static let internalError: TranslationError](translationerror/internalerror.md)
  An error occurred internal to the translation engine.
- [static let notInstalled: TranslationError](translationerror/notinstalled.md)
  The device doesn’t have the necessary languages downloaded to perform a translation and the session can’t request the person to download them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/alreadycancelled)*