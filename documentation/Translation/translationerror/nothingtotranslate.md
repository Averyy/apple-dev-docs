# nothingToTranslate

**Framework**: Translation  
**Kind**: property

No content to translate.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
- macOS 15.0+

## Declaration

```swift
static let nothingToTranslate: TranslationError
```

## See Also

- [static let unableToIdentifyLanguage: TranslationError](translationerror/unabletoidentifylanguage.md)
  The framework can’t identify the source language automatically.
- [static let internalError: TranslationError](translationerror/internalerror.md)
  An error occurred internal to the translation engine.
- [static let alreadyCancelled: TranslationError](translationerror/alreadycancelled.md)
  An error describing a translation session that you’ve cancelled before, which prevents the session from producing additional results.
- [static let notInstalled: TranslationError](translationerror/notinstalled.md)
  The device doesn’t have the necessary languages downloaded to perform a translation and the session can’t request the person to download them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/nothingtotranslate)*