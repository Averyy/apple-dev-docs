# LanguageModelError.UnsupportedLanguageOrLocale

**Framework**: Foundation Models  
**Kind**: struct

Information about an unsupported language or locale.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct UnsupportedLanguageOrLocale
```

## Topics

### Creating an error instance
- [init(languageCode: Locale.LanguageCode, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/unsupportedlanguageorlocale/init(languagecode:debugdescription:metadata:).md)
### Inspecting unsupported language or locale errors
- [var metadata: [String : any Sendable]](languagemodelerror/unsupportedlanguageorlocale/metadata.md)
- [var languageCode: Locale.LanguageCode](languagemodelerror/unsupportedlanguageorlocale/languagecode.md)
- [var debugDescription: String](languagemodelerror/unsupportedlanguageorlocale/debugdescription.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case unsupportedLanguageOrLocale(LanguageModelError.UnsupportedLanguageOrLocale)](languagemodelerror/unsupportedlanguageorlocale(_:).md)
  The model was prompted to respond in a language that it does not support.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedlanguageorlocale)*