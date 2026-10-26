---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelfactory"
framework: "mlx-swift-lm/MLXEmbedders"
---

# EmbedderModelFactory

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

Factory for creating new Embedder models.

## Declaration

```swift
final class EmbedderModelFactory
```

#### Overview

Callers can use the `shared` instance or create a new instance if custom configuration is required.

```swift
let downloader: any Downloader
let tokenizerLoader: any TokenizerLoader
let modelId = "mlx-community/gemma-3-1b-it-qat-4bit"
let modelContainer = try await EmbedderModelFactory.shared.loadContainer(
    from: downloader, using: tokenizerLoader, configuration: .init(id: modelId),
    progressHandler: logProgress(modelId)
)
```

## Topics

### Initializers
- [init(typeRegistry: ModelTypeRegistry<EmbeddingModel>, modelRegistry: AbstractModelRegistry)](./embeddermodelfactory/init%28typeregistry,modelregistry%29.md)
### Instance Properties
- [let modelRegistry: AbstractModelRegistry](./embeddermodelfactory/modelregistry.md)
  registry of model id to configuration, e.g. `sentence-transformers/all-MiniLM-L6-v2`
- [let typeRegistry: ModelTypeRegistry<EmbeddingModel>](./embeddermodelfactory/typeregistry.md)
  registry of model type, e.g. configuration value `gemma3` -> configuration and init methods
### Type Aliases
- [EmbedderModelFactory.ContainerType](./embeddermodelfactory/containertype.md)
- [EmbedderModelFactory.ContextType](./embeddermodelfactory/contexttype.md)
### Type Properties
- [static let shared: EmbedderModelFactory](./embeddermodelfactory/shared.md)
  Shared instance with default behavior.
### Default Implementations
- [GenericModelFactory Implementations](./embeddermodelfactory/genericmodelfactory-implementations.md)

## Relationships

### Conforms To
- MLXLMCommon.GenericModelFactory
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddermodelfactory)*