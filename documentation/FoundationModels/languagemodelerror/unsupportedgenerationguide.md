# LanguageModelError.UnsupportedGenerationGuide

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Information about an unsupported generation guide.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct UnsupportedGenerationGuide
```

## Topics

### Creating an error instance
- [init(schemaName: String?, debugDescription: String, metadata: [String : any Sendable])](./unsupportedgenerationguide/init%28schemaname,debugdescription,metadata%29.md)
  Creates information describing a generation guide the model doesn’t support.
### Inspecting unsupported generation guide errors
- [var metadata: [String : any Sendable]](./unsupportedgenerationguide/metadata.md)
  Additional information about the failure, keyed by name.
- [var schemaName: String?](./unsupportedgenerationguide/schemaname.md)
  The name of the schema whose generation guide isn’t supported, if any.
- [var debugDescription: String](./unsupportedgenerationguide/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Generation guide unsupported error
- [case unsupportedGenerationGuide(LanguageModelError.UnsupportedGenerationGuide)](./unsupportedgenerationguide%28_%29.md)
  An unsupported generation guide was used.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedgenerationguide)*