# LanguageModelCapabilities.Capability

**Framework**: Foundation Models  
**Kind**: struct

A capability that a given language model may or may not have.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct Capability
```

## Topics

### Accessing model capabilities
- [static var guidedGeneration: LanguageModelCapabilities.Capability](languagemodelcapabilities/capability/guidedgeneration.md)
  The capability to ensure model output conforms to a given generation schema.
- [static var reasoning: LanguageModelCapabilities.Capability](languagemodelcapabilities/capability/reasoning.md)
  The capability to reason, structurally separately from producing a response.
- [static var toolCalling: LanguageModelCapabilities.Capability](languagemodelcapabilities/capability/toolcalling.md)
  The capability to call tools to gather information or trigger side effects.
- [static var vision: LanguageModelCapabilities.Capability](languagemodelcapabilities/capability/vision.md)
  The capability to accept image inputs in prompts.

## Relationships

### Conforms To
- [Equatable](../swift/equatable.md)
- [Hashable](../swift/hashable.md)
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [init([LanguageModelCapabilities.Capability])](languagemodelcapabilities/init(_:).md)
  Creates a capabilities instance from a list of supported capabilities.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelcapabilities/capability)*