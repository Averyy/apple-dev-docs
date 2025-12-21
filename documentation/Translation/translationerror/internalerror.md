# internalError

**Framework**: Translation  
**Kind**: property

An error occurred internal to the translation engine.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
static let internalError: TranslationError
```

## See Also

- [static let nothingToTranslate: TranslationError](translationerror/nothingtotranslate.md)
  No content to translate.
- [static let unableToIdentifyLanguage: TranslationError](translationerror/unabletoidentifylanguage.md)
  The framework can’t identify the source language automatically.
- [static let alreadyCancelled: TranslationError](translationerror/alreadycancelled.md)
  An error describing a translation session that you’ve cancelled before, which prevents the session from producing additional results.
- [static let notInstalled: TranslationError](translationerror/notinstalled.md)
  The device doesn’t have the necessary languages downloaded to perform a translation and the session can’t request the person to download them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/internalerror)*