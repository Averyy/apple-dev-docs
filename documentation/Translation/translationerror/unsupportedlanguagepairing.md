# unsupportedLanguagePairing

**Framework**: Translation  
**Kind**: property

The framework doesn’t support the the specified source and target language pairing.

**Availability**:
- iOS 18.0+
- iPadOS 18.0+
- macOS 15.0+

## Declaration

```swift
static let unsupportedLanguagePairing: TranslationError
```

#### Discussion

The framework doesn’t support translating from and to the same language. For example you can’t translate from English (US) to English (UK) or from French to French.

## See Also

- [static let unsupportedSourceLanguage: TranslationError](translationerror/unsupportedsourcelanguage.md)
  The framework doesn’t support the specified or detected source language.
- [static let unsupportedTargetLanguage: TranslationError](translationerror/unsupportedtargetlanguage.md)
  The framework doesn’t support the specified or chosen target language.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/unsupportedlanguagepairing)*