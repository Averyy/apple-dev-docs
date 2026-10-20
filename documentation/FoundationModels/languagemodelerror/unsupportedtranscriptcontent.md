# LanguageModelError.UnsupportedTranscriptContent

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Information about unsupported prompt content.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct UnsupportedTranscriptContent
```

## Topics

### Creating an error instance
- [init(unsupportedContent: [Transcript.Entry], debugDescription: String, metadata: [String : any Sendable])](./unsupportedtranscriptcontent/init%28unsupportedcontent,debugdescription,metadata%29.md)
  Creates information describing transcript content the model can’t process.
### Inspecting unsupported transcript content errors
- [var metadata: [String : any Sendable]](./unsupportedtranscriptcontent/metadata.md)
  Additional information about the failure, keyed by name.
- [var unsupportedContent: [Transcript.Entry]](./unsupportedtranscriptcontent/unsupportedcontent.md)
  The transcript entries that the model can’t process.
- [var debugDescription: String](./unsupportedtranscriptcontent/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Transcript content unsupported error
- [case unsupportedTranscriptContent(LanguageModelError.UnsupportedTranscriptContent)](./unsupportedtranscriptcontent%28_%29.md)
  The prompt contains content that the model cannot process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedtranscriptcontent)*