# LanguageModelCapabilities.Capability

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

A capability that a given language model may or may not have.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct Capability
```

## Topics

### Accessing model capabilities
- [static var guidedGeneration: LanguageModelCapabilities.Capability](./capability/guidedgeneration.md)
  The capability to ensure model output conforms to a given generation schema.
- [static var reasoning: LanguageModelCapabilities.Capability](./capability/reasoning.md)
  The capability to reason, structurally separately from producing a response.
- [static var toolCalling: LanguageModelCapabilities.Capability](./capability/toolcalling.md)
  The capability to call tools to gather information or trigger side effects.
- [static var vision: LanguageModelCapabilities.Capability](./capability/vision.md)
  The capability to accept image inputs in prompts.

## Relationships

### Conforms To
- [Equatable](../../Swift/equatable.md)
- [Hashable](../../Swift/hashable.md)
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Creating an instance
- [init([LanguageModelCapabilities.Capability])](./init%28_%29.md)
  Creates a capabilities instance from a list of supported capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelcapabilities/capability)*