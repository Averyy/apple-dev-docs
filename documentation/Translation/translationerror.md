# TranslationError

**Framework**: Translation  
**Kind**: struct

Error codes describing why the framework can’t perform a translation.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- Mac Catalyst 26.0+ (Beta)
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
### Handling unsupported errors
- [static let unsupportedSourceLanguage: TranslationError](translationerror/unsupportedsourcelanguage.md)
  The framework doesn’t support the specified or detected source language.
- [static let unsupportedTargetLanguage: TranslationError](translationerror/unsupportedtargetlanguage.md)
  The framework doesn’t support the specified or chosen target language.
- [static let unsupportedLanguagePairing: TranslationError](translationerror/unsupportedlanguagepairing.md)
  The framework doesn’t support the the specified source and target language pairing.
### Operators
- [static func ~= (TranslationError, any Error) -> Bool](translationerror/~=(_:_:).md)
  You can use `switch` and `case` to check for a given value of `TranslationError` if you want to handle each error case separately.
### Instance Properties
- [var errorDescription: String?](translationerror/errordescription.md)
  A localized message describing what error occurred.
- [var failureReason: String?](translationerror/failurereason.md)
  A localized message describing the reason for the failure.
### Type Properties
- [static let alreadyCancelled: TranslationError](translationerror/alreadycancelled.md)
  The session was already cancelled, so can’t produce more results.
- [static let notInstalled: TranslationError](translationerror/notinstalled.md)
  The device doesn’t have the necessary languages downloaded to perform a translation, and this session can’t request the user download them. This error can be thrown if the languages are supported but not approved, or if they’re approved but not finished downloading yet.
### Default Implementations
- [Error Implementations](translationerror/error-implementations.md)
- [LocalizedError Implementations](translationerror/localizederror-implementations.md)

## Relationships

### Conforms To
- [Error](../Swift/Error.md)
- [LocalizedError](../Foundation/LocalizedError.md)
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror)*