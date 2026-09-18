# LanguageModelError.ContextSizeExceeded

**Framework**: Foundation Models  
**Kind**: struct

Information about exceeding the context window size.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct ContextSizeExceeded
```

## Topics

### Creating an error instance
- [init(contextSize: Int, tokenCount: Int, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/contextsizeexceeded/init(contextsize:tokencount:debugdescription:metadata:).md)
  Creates information describing a transcript that exceeded the model’s context size.
### Inspecting context size errors
- [var metadata: [String : any Sendable]](languagemodelerror/contextsizeexceeded/metadata.md)
  Additional information about the failure, keyed by name.
- [var tokenCount: Int](languagemodelerror/contextsizeexceeded/tokencount.md)
  The number of tokens in the transcript that exceeded the model’s context size.
- [var contextSize: Int](languagemodelerror/contextsizeexceeded/contextsize.md)
  The model’s maximum context size, in tokens.
- [var debugDescription: String](languagemodelerror/contextsizeexceeded/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case contextSizeExceeded(LanguageModelError.ContextSizeExceeded)](languagemodelerror/contextsizeexceeded(_:).md)
  The session’s transcript exceeded the model’s context size.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/contextsizeexceeded)*