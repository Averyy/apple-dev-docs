# TranslationError

**Framework**: Translation  
**Kind**: struct

Error codes describing why the framework can’t perform a translation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+
- macOS 15.0+

## Declaration

```swift
struct TranslationError
```

## Topics

### Handling general errors
- [static let nothingToTranslate: TranslationError](translationerror/nothingtotranslate.md)
  No content to translate.
- [static let unableToIdentifyLanguage: TranslationError](translationerror/unabletoidentifylanguage.md)
  The framework can’t identify the source language automatically.
- [static let internalError: TranslationError](translationerror/internalerror.md)
  An error occurred internal to the translation engine.
- [static let alreadyCancelled: TranslationError](translationerror/alreadycancelled.md)
  An error describing a translation session that you’ve cancelled before, which prevents the session from producing additional results.
- [static let notInstalled: TranslationError](translationerror/notinstalled.md)
  The device doesn’t have the necessary languages downloaded to perform a translation and the session can’t request the person to download them.
### Handling unsupported errors
- [static let unsupportedSourceLanguage: TranslationError](translationerror/unsupportedsourcelanguage.md)
  The framework doesn’t support the specified or detected source language.
- [static let unsupportedTargetLanguage: TranslationError](translationerror/unsupportedtargetlanguage.md)
  The framework doesn’t support the specified or chosen target language.
- [static let unsupportedLanguagePairing: TranslationError](translationerror/unsupportedlanguagepairing.md)
  The framework doesn’t support the specified source and target language pairing.
### Describing errors
- [var errorDescription: String?](translationerror/errordescription.md)
  A localized message describing the error.
- [var failureReason: String?](translationerror/failurereason.md)
  A localized message describing the reason for the failure.
### Comparing errors
- [static func ~= (TranslationError, any Error) -> Bool](translationerror/~=(_:_:).md)
  This operator allows you to check for a given value of a translation error and handle each error case.

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror)*