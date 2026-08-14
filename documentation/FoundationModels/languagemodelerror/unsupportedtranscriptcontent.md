# LanguageModelError.UnsupportedTranscriptContent

**Framework**: Foundation Models  
**Kind**: struct

Information about unsupported prompt content.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct UnsupportedTranscriptContent
```

## Topics

### Creating an error instance
- [init(unsupportedContent: [Transcript.Entry], debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/unsupportedtranscriptcontent/init(unsupportedcontent:debugdescription:metadata:).md)
### Inspecting unsupported transcript content errors
- [var metadata: [String : any Sendable]](languagemodelerror/unsupportedtranscriptcontent/metadata.md)
- [var unsupportedContent: [Transcript.Entry]](languagemodelerror/unsupportedtranscriptcontent/unsupportedcontent.md)
- [var debugDescription: String](languagemodelerror/unsupportedtranscriptcontent/debugdescription.md)

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case unsupportedTranscriptContent(LanguageModelError.UnsupportedTranscriptContent)](languagemodelerror/unsupportedtranscriptcontent(_:).md)
  The prompt contains content that the model cannot process.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedtranscriptcontent)*