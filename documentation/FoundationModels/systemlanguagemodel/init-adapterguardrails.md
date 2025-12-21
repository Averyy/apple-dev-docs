# init(adapter:guardrails:)

**Framework**: Foundation Models  
**Kind**: init

Creates the base version of the model with an adapter.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
convenience init(adapter: SystemLanguageModel.Adapter, guardrails: SystemLanguageModel.Guardrails = .default)
```

## See Also

- [Loading and using a custom adapter with Foundation Models](loading-and-using-a-custom-adapter-with-foundation-models.md)
  Specialize the behavior of the system language model by using a custom adapter you train.
- [com.apple.developer.foundation-model-adapter](../BundleResources/Entitlements/com.apple.developer.foundation-model-adapter.md)
  A Boolean value that indicates whether the app can enable custom adapters for the Foundation Models framework.
- [SystemLanguageModel.Adapter](systemlanguagemodel/adapter.md)
  Specializes the system language model for custom use cases.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/init(adapter:guardrails:))*