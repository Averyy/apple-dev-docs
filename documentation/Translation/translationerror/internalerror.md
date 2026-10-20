# internalError

**Framework**: Translation  
**Kind**: property  
**Role**: Type Property

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

### Handling general errors
- [static let nothingToTranslate: TranslationError](./nothingtotranslate.md)
  No content to translate.
- [static let unableToIdentifyLanguage: TranslationError](./unabletoidentifylanguage.md)
  The framework can’t identify the source language automatically.
- [static let alreadyCancelled: TranslationError](./alreadycancelled.md)
  An error describing a translation session that you’ve cancelled before, which prevents the session from producing additional results.
- [static let notInstalled: TranslationError](./notinstalled.md)
  The device doesn’t have the necessary languages downloaded to perform a translation and the session can’t request the person to download them.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/internalerror)*