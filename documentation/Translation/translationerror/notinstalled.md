# notInstalled

**Framework**: Translation  
**Kind**: property

The device doesn’t have the necessary languages downloaded to perform a translation and the session can’t request the person to download them.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+

## Declaration

```swift
static let notInstalled: TranslationError
```

#### Discussion

This error is thrown if [`canRequestDownloads`](TranslationSession/canRequestDownloads.md) is false and either the languages are supported but the person hasn’t approved them or if the person has approved them but the languages haven’t finished downloading.

## See Also

- [static let nothingToTranslate: TranslationError](translationerror/nothingtotranslate.md)
  No content to translate.
- [static let unableToIdentifyLanguage: TranslationError](translationerror/unabletoidentifylanguage.md)
  The framework can’t identify the source language automatically.
- [static let internalError: TranslationError](translationerror/internalerror.md)
  An error occurred internal to the translation engine.
- [static let alreadyCancelled: TranslationError](translationerror/alreadycancelled.md)
  An error describing a translation session that you’ve cancelled before, which prevents the session from producing additional results.


---

*[View on Apple Developer](https://developer.apple.com/documentation/translation/translationerror/notinstalled)*