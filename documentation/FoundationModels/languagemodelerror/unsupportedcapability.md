# LanguageModelError.UnsupportedCapability

**Framework**: Foundation Models  
**Kind**: struct

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
- [init(capability: LanguageModelCapabilities.Capability, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/unsupportedcapability/init(capability:debugdescription:metadata:).md)
  Creates information describing a capability the model doesn’t support.
### Inspecting unsupported capability errors
- [var metadata: [String : any Sendable]](languagemodelerror/unsupportedcapability/metadata.md)
  Additional information about the failure, keyed by name.
- [var capability: LanguageModelCapabilities.Capability](languagemodelerror/unsupportedcapability/capability.md)
  The capability that the model doesn’t support.
- [var debugDescription: String](languagemodelerror/unsupportedcapability/debugdescription.md)
  A debug description to help developers diagnose issues during development.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)
- [SendableMetatype](../swift/sendablemetatype.md)

## See Also

- [case unsupportedCapability(LanguageModelError.UnsupportedCapability)](languagemodelerror/unsupportedcapability(_:).md)
  The model being used doesn’t support a particular feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedcapability)*