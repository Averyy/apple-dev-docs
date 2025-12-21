# SystemLanguageModel.Adapter

**Framework**: Foundation Models  
**Kind**: struct

Specializes the system language model for custom use cases.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- visionOS 26.0+

## Declaration

```swift
struct Adapter
```

## Mentions

- [Loading and using a custom adapter with Foundation Models](loading-and-using-a-custom-adapter-with-foundation-models.md)

#### Overview

Use the base system model for most prompt engineering, guided generation, and tools. If you need to specialize the model, train a custom `Adapter` to alter the system model weights and optimize it for your custom task. Use custom adapters only if you’re comfortable training foundation models in Python.

> ❗ **Important**: Be sure to re-train the adapter for every new version of the base system model that Apple releases. Adapters consume a large amount of storage space and isn’t recommended for most apps.

For more on custom adapters, see [`Get started with Foundation Models adapter training`](https://developer.apple.comhttps://developer.apple.com/apple-intelligence/foundation-models-adapter/).

## Topics

### Creating an adapter
- [Loading and using a custom adapter with Foundation Models](loading-and-using-a-custom-adapter-with-foundation-models.md)
  Specialize the behavior of the system language model by using a custom adapter you train.
- [com.apple.developer.foundation-model-adapter](../BundleResources/Entitlements/com.apple.developer.foundation-model-adapter.md)
  A Boolean value that indicates whether the app can enable custom adapters for the Foundation Models framework.
- [init(fileURL: URL) throws](systemlanguagemodel/adapter/init(fileurl:).md)
  Creates an adapter from the file URL.
- [init(name: String) throws](systemlanguagemodel/adapter/init(name:).md)
  Creates an adapter downloaded from the background assets framework.
### Prepare the adapter
- [func compile() async throws](systemlanguagemodel/adapter/compile.md)
  Prepares an adapter before being used with a [`LanguageModelSession`](languagemodelsession.md). You should call this if your adapter has a draft model.
### Getting the metadata
- [var creatorDefinedMetadata: [String : Any]](systemlanguagemodel/adapter/creatordefinedmetadata.md)
  Values read from the creator defined field of the adapter’s metadata.
### Removing obsolete adapters
- [static func removeObsoleteAdapters() throws](systemlanguagemodel/adapter/removeobsoleteadapters.md)
  Remove all obsolete adapters that are no longer compatible with current system models.
### Checking compatibility
- [static func compatibleAdapterIdentifiers(name: String) -> [String]](systemlanguagemodel/adapter/compatibleadapteridentifiers(name:).md)
  Get all compatible adapter identifiers compatible with current system models.
- [static func isCompatible(AssetPack) -> Bool](systemlanguagemodel/adapter/iscompatible(_:).md)
  Returns a Boolean value that indicates whether an asset pack is an on-device foundation model adapter and is compatible with the system base model version on the runtime device.
### Getting the asset error
- [SystemLanguageModel.Adapter.AssetError](systemlanguagemodel/adapter/asseterror.md)

## See Also

- [Loading and using a custom adapter with Foundation Models](loading-and-using-a-custom-adapter-with-foundation-models.md)
  Specialize the behavior of the system language model by using a custom adapter you train.
- [com.apple.developer.foundation-model-adapter](../BundleResources/Entitlements/com.apple.developer.foundation-model-adapter.md)
  A Boolean value that indicates whether the app can enable custom adapters for the Foundation Models framework.
- [convenience init(adapter: SystemLanguageModel.Adapter, guardrails: SystemLanguageModel.Guardrails)](systemlanguagemodel/init(adapter:guardrails:).md)
  Creates the base version of the model with an adapter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter)*