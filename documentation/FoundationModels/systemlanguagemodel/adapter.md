# SystemLanguageModel.Adapter

**Framework**: Foundation Models  
**Kind**: struct

Specializes the system language model for custom use cases.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)

## Declaration

```swift
struct Adapter
```

#### Overview

Use the base system model for most prompt engineering, guided generation, and tools. If you need to specialize the model, train a custom `Adapter` to alter the system model weights and optimize it for your custom task. Use custom adapters only if you’re comfortable training foundation models in Python.

> **Note**: You need to re-train an adapter for every new version of the base system model that Apple releases. Adapters consume a large amount of storage space and isn’t recommended for most apps.

For more on custom adapters, see [`adapter training toolkit`](https://developer.apple.comhttps://developer.apple.com/apple-intelligence/foundation-models-adapter/).

## Topics

### Creating an adapter
- [init(fileURL: URL) throws](systemlanguagemodel/adapter/init(fileurl:).md)
  Creates an adapter from the file URL.
- [init(name: String) throws](systemlanguagemodel/adapter/init(name:).md)
  Creates an adapter downloaded from the background assets framework.
### Getting the metadata
- [let creatorDefinedMetadata: [String : Any]](systemlanguagemodel/adapter/creatordefinedmetadata.md)
  Values read from the creator defined field of the adapter’s metadata.
### Removing obsolete adapters
- [static func removeObsoleteAdapters()](systemlanguagemodel/adapter/removeobsoleteadapters.md)
  Remove all obsolete adapters that are no longer compatible with current system models.
### Checking compatibility
- [static func compatibleAdapterIdentifiers(name: String) -> [String]](systemlanguagemodel/adapter/compatibleadapteridentifiers(name:).md)
  Get all compatible adapter identifiers compatible with current system models.
- [static func isCompatible(AssetPack) -> Bool](systemlanguagemodel/adapter/iscompatible(_:).md)
  Returns true when an asset pack is an Foundation Models Adapter and compatible with current system base model.
### Getting the asset error
- [SystemLanguageModel.Adapter.AssetError](systemlanguagemodel/adapter/asseterror.md)

## See Also

- [convenience init(adapter: SystemLanguageModel.Adapter)](systemlanguagemodel/init(adapter:).md)
  Creates the base version of the model with an adapter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/foundationmodels/systemlanguagemodel/adapter)*