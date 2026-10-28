# LanguageModelError.unsupportedCapability(_:)

**Framework**: Foundation Models  
**Kind**: case  
**Role**: Case

The model being used doesn’t support a particular feature.

**Availability**:
- iOS 27.0+
- iPadOS 27.0+
- Mac Catalyst 27.0+
- macOS 27.0+
- visionOS 27.0+
- watchOS 27.0+

## Declaration

```swift
case unsupportedCapability(LanguageModelError.UnsupportedCapability)
```

## Discussion

This failure can happen if you use capabilities like guided generation or tool calling with a model that does not support them.

## See Also

### Capability unsupported error
- [LanguageModelError.UnsupportedCapability](./unsupportedcapability.md)
  Information about an unsupported capability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/languagemodelerror/unsupportedcapability(_:))*