# LanguageModelError.UnsupportedTranscriptContent

**Framework**: Foundation Models  
**Kind**: struct

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
- [init(unsupportedContent: [Transcript.Entry], debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/unsupportedtranscriptcontent/init(unsupportedcontent:debugdescription:metadata:).md)
  Creates information describing transcript content the model can’t process.
### Inspecting unsupported transcript content errors
- [var metadata: [String : any Sendable]](languagemodelerror/unsupportedtranscriptcontent/metadata.md)
  Additional information about the failure, keyed by name.
- [var unsupportedContent: [Transcript.Entry]](languagemodelerror/unsupportedtranscriptcontent/unsupportedcontent.md)
  The transcript entries that the model can’t process.
- [var debugDescription: String](languagemodelerror/unsupportedtranscriptcontent/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case unsupportedTranscriptContent(LanguageModelError.UnsupportedTranscriptContent)](languagemodelerror/unsupportedtranscriptcontent(_:).md)
  The prompt contains content that the model cannot process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedtranscriptcontent)*