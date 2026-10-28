# alreadyCancelled

**Framework**: Translation  
**Kind**: property  
**Role**: Type Property

An error describing a translation session that you’ve cancelled before, which prevents the session from producing additional results.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
static let alreadyCancelled: TranslationError
```

## Discussion

A [`TranslationSession`](../translationsession.md) instance throws this error when you call one of its translate methods after calling its [`cancel()`](../translationsession/cancel%28%29.md) method.

## See Also

### Handling general errors
- [static let nothingToTranslate: TranslationError](./nothingtotranslate.md)
  No content to translate.
- [static let unableToIdentifyLanguage: TranslationError](./unabletoidentifylanguage.md)
  The framework can’t identify the source language automatically.
- [static let internalError: TranslationError](./internalerror.md)
  An error occurred internal to the translation engine.
- [static let notInstalled: TranslationError](./notinstalled.md)
  The device doesn’t have the necessary languages downloaded to perform a translation and the session can’t request the person to download them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/alreadycancelled)*