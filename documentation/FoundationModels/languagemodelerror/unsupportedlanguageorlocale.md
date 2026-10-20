# LanguageModelError.UnsupportedLanguageOrLocale

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

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
- [init(languageCode: Locale.LanguageCode, debugDescription: String, metadata: [String : any Sendable])](./unsupportedlanguageorlocale/init%28languagecode,debugdescription,metadata%29.md)
  Creates information describing a language or locale the model doesn’t support.
### Inspecting unsupported language or locale errors
- [var metadata: [String : any Sendable]](./unsupportedlanguageorlocale/metadata.md)
  Additional information about the failure, keyed by name.
- [var languageCode: Locale.LanguageCode](./unsupportedlanguageorlocale/languagecode.md)
  The language code that the model doesn’t support.
- [var debugDescription: String](./unsupportedlanguageorlocale/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Language unsupported error
- [case unsupportedLanguageOrLocale(LanguageModelError.UnsupportedLanguageOrLocale)](./unsupportedlanguageorlocale%28_%29.md)
  The model was prompted to respond in a language that it does not support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedlanguageorlocale)*