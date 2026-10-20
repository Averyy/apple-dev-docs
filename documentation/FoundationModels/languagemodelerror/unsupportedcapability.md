# LanguageModelError.UnsupportedCapability

**Framework**: Foundation Models  
**Kind**: struct  
**Role**: Structure

Information about an unsupported capability.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
struct UnsupportedCapability
```

## Topics

### Creating an error instance
- [init(capability: LanguageModelCapabilities.Capability, debugDescription: String, metadata: [String : any Sendable])](./unsupportedcapability/init%28capability,debugdescription,metadata%29.md)
  Creates information describing a capability the model doesn’t support.
### Inspecting unsupported capability errors
- [var metadata: [String : any Sendable]](./unsupportedcapability/metadata.md)
  Additional information about the failure, keyed by name.
- [var capability: LanguageModelCapabilities.Capability](./unsupportedcapability/capability.md)
  The capability that the model doesn’t support.
- [var debugDescription: String](./unsupportedcapability/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../../Swift/sendable.md)
- [SendableMetatype](../../Swift/sendablemetatype.md)

## See Also

### Capability unsupported error
- [case unsupportedCapability(LanguageModelError.UnsupportedCapability)](./unsupportedcapability%28_%29.md)
  The model being used doesn’t support a particular feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedcapability)*