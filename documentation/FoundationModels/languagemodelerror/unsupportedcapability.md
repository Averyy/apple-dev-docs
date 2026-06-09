# LanguageModelError.UnsupportedCapability

**Framework**: Foundation Models  
**Kind**: struct

Information about an unsupported capability.

**Availability**:
- iOS 27.0+ (Beta)
- iPadOS 27.0+ (Beta)
- Mac Catalyst 27.0+ (Beta)
- macOS 27.0+ (Beta)
- visionOS 27.0+ (Beta)
- watchOS 27.0+ (Beta)

## Declaration

```swift
struct UnsupportedCapability
```

## Topics

### Creating an error instance
- [init(capability: LanguageModelCapabilities.Capability, debugDescription: String, metadata: [String : any Sendable])](languagemodelerror/unsupportedcapability/init(capability:debugdescription:metadata:).md)
### Inspecting unsupported capability errors
- [var metadata: [String : any Sendable]](languagemodelerror/unsupportedcapability/metadata.md)
- [var capability: LanguageModelCapabilities.Capability](languagemodelerror/unsupportedcapability/capability.md)
- [var debugDescription: String](languagemodelerror/unsupportedcapability/debugdescription.md)

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)
- [SendableMetatype](../Swift/SendableMetatype.md)

## See Also

- [case unsupportedCapability(LanguageModelError.UnsupportedCapability)](languagemodelerror/unsupportedcapability(_:).md)
  The model being used doesn’t support a particular feature.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedcapability)*