# LanguageModelCapabilities

**Framework**: Foundation Models  
**Kind**: struct

A set of capabilities that a language model provides.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct LanguageModelCapabilities
```

#### Overview

Use this to declare what your model can do, like tool calling and guided generation:

```swift
struct MyLanguageModel: LanguageModel {
    var capabilities: LanguageModelCapabilities {
        LanguageModelCapabilities([
            .toolCalling,
            .guidedGeneration,
            .reasoning
        ])
    }
}
```

Inspect [`capabilities`](languagemodel/capabilities.md) ahead of time to detect what the model supports before performing the request:

```swift
// Before prompting the model with a generable type, check whether it
// supports guided generation.
if selectedModel.capabilities.contains(.guidedGeneration) {
    let response = try await session.respond(to: "...", generating: MySchema.self)
}
```

When a model doesn’t support a capability, the framework can refuse to dispatch incompatible requests to the executor and throw an [`LanguageModelError.unsupportedCapability(_:)`](languagemodelerror/unsupportedcapability(_:).md) error instead.

## Topics

### Creating an instance
- [init([LanguageModelCapabilities.Capability])](languagemodelcapabilities/init(_:).md)
  Creates a capabilities instance from a list of supported capabilities.
- [LanguageModelCapabilities.Capability](languagemodelcapabilities/capability.md)
  A capability that a given language model may or may not have.
### Inspecting model capabilities
- [func contains(LanguageModelCapabilities.Capability) -> Bool](languagemodelcapabilities/contains(_:).md)
  Returns a Boolean value that indicates whether the specified capability is supported.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [Running a Core AI model in a Foundation Models session](running-a-core-ai-model-in-a-foundation-models-session.md)
  Send requests on device to an open source model you export with Core AI to get a consistent API experience.
- [Optimizing key-value caching in language model sessions](optimizing-key-value-caching-in-language-model-sessions.md)
  Prevent repeated token processing by preserving the cached state across turns.
- [protocol LanguageModel](languagemodel.md)
  A protocol that you use to interface with a model.
- [protocol LanguageModelExecutor](languagemodelexecutor.md)
  A protocol that defines the interface for responding to session requests.
- [struct LanguageModelExecutorGenerationChannel](languagemodelexecutorgenerationchannel.md)
  A type you use to send model output deltas and updates to the framework.
- [struct LanguageModelExecutorGenerationRequest](languagemodelexecutorgenerationrequest.md)
  A type that contains the details for a generation request.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelcapabilities)*