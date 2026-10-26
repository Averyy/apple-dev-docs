---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelfactoryregistry"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelFactoryRegistry

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Registry of [`ModelFactory`](./modelfactory.md) trampolines.

## Declaration

```swift
final class ModelFactoryRegistry
```

#### Overview

This allows [`loadModel(from:using:id:revision:useLatest:progressHandler:)`](./loadmodel%28from,using,id,revision,uselatest,progresshandler%29.md) to use any [`ModelFactory`](./modelfactory.md) instances available but be defined in the `LLMCommon` layer.  This is not typically used directly – it is called via [`loadModel(from:using:id:revision:useLatest:progressHandler:)`](./loadmodel%28from,using,id,revision,uselatest,progresshandler%29.md):

```swift
let model = try await loadModel(from: downloader, using: tokenizerLoader, id: "mlx-community/Qwen3-4B-4bit")
```

## Topics

### Instance Methods
- [func addTrampoline(() -> (any ModelFactory)?)](./modelfactoryregistry/addtrampoline%28_%29.md)
- [func modelFactories() -> [any ModelFactory]](./modelfactoryregistry/modelfactories%28%29.md)
### Type Properties
- [static let shared: ModelFactoryRegistry](./modelfactoryregistry/shared.md)

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype

## See Also

### Related Documentation
- [func loadModel(from: any Downloader, using: any TokenizerLoader, id: String, revision: String, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ModelContext](./loadmodel%28from,using,id,revision,uselatest,progresshandler%29.md)
  Load a model given a model identifier, downloading via a [`Downloader`](./downloader.md).
- [func loadModel(from: URL, using: any TokenizerLoader) async throws -> sending ModelContext](./loadmodel%28from,using%29.md)
  Load a model from a local directory of configuration and weights.
- [func loadModelContainer(from: any Downloader, using: any TokenizerLoader, id: String, revision: String, useLatest: Bool, progressHandler: @Sendable (Progress) -> Void) async throws -> sending ModelContainer](./loadmodelcontainer%28from,using,id,revision,uselatest,progresshandler%29.md)
  Load a model given a model identifier, downloading via a [`Downloader`](./downloader.md).
- [func loadModelContainer(from: URL, using: any TokenizerLoader) async throws -> sending ModelContainer](./loadmodelcontainer%28from,using%29.md)
  Load a model from a local directory of configuration and weights.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelfactoryregistry)*