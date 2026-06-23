# LanguageModelError.Refusal

**Framework**: Foundation Models  
**Kind**: struct

Information about a model refusal.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Refusal
```

#### Overview

Refusal failures indicate that the model chose not to respond to a prompt.

## Topics

### Creating an error instance
- [init(explanation: String, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/refusal/init(explanation:debugdescription:metadata:).md)
### Inspecting refusal errors
- [var metadata: [String : any Sendable]](languagemodelerror/refusal/metadata.md)
- [var debugDescription: String](languagemodelerror/refusal/debugdescription.md)
### Getting a refusal explanation
- [var explanation: LanguageModelSession.Response<String>](languagemodelerror/refusal/explanation.md)
- [var explanationStream: LanguageModelSession.ResponseStream<String>](languagemodelerror/refusal/explanationstream.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case refusal(LanguageModelError.Refusal)](languagemodelerror/refusal(_:).md)
  The model refused to answer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/refusal)*