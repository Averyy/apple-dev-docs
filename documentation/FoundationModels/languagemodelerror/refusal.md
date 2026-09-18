# LanguageModelError.Refusal

**Framework**: Foundation Models  
**Kind**: struct

Information about a model refusal.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Refusal
```

#### Overview

Refusal failures indicate that the model chose not to respond to a prompt.

## Topics

### Creating an error instance
- [init(explanation: String, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/refusal/init(explanation:debugdescription:metadata:).md)
  Creates information describing a model refusal.
### Inspecting refusal errors
- [var metadata: [String : any Sendable]](languagemodelerror/refusal/metadata.md)
  Additional information about the failure, keyed by name.
- [var debugDescription: String](languagemodelerror/refusal/debugdescription.md)
  A debug description to help developers diagnose issues during development.
### Getting a refusal explanation
- [var explanation: LanguageModelSession.Response<String>](languagemodelerror/refusal/explanation.md)
  The model’s explanation for why it refused to generate a response.
- [var explanationStream: LanguageModelSession.ResponseStream<String>](languagemodelerror/refusal/explanationstream.md)
  The model’s explanation for why it refused to generate a response, delivered as it streams.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case refusal(LanguageModelError.Refusal)](languagemodelerror/refusal(_:).md)
  The model refused to answer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/refusal)*