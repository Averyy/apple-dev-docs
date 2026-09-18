# LanguageModelError.UnsupportedLanguageOrLocale

**Framework**: Foundation Models  
**Kind**: struct

Information about an unsupported language or locale.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct UnsupportedLanguageOrLocale
```

## Topics

### Creating an error instance
- [init(languageCode: Locale.LanguageCode, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/unsupportedlanguageorlocale/init(languagecode:debugdescription:metadata:).md)
  Creates information describing a language or locale the model doesn’t support.
### Inspecting unsupported language or locale errors
- [var metadata: [String : any Sendable]](languagemodelerror/unsupportedlanguageorlocale/metadata.md)
  Additional information about the failure, keyed by name.
- [var languageCode: Locale.LanguageCode](languagemodelerror/unsupportedlanguageorlocale/languagecode.md)
  The language code that the model doesn’t support.
- [var debugDescription: String](languagemodelerror/unsupportedlanguageorlocale/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case unsupportedLanguageOrLocale(LanguageModelError.UnsupportedLanguageOrLocale)](languagemodelerror/unsupportedlanguageorlocale(_:).md)
  The model was prompted to respond in a language that it does not support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedlanguageorlocale)*