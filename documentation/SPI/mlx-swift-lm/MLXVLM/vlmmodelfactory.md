---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmmodelfactory"
framework: "mlx-swift-lm/MLXVLM"
---

# VLMModelFactory

**Framework**: mlx-swift-lm/MLXVLM  
**Kind**: class  
**Role**: Class

Factory for creating new LLMs.

## Declaration

```swift
final class VLMModelFactory
```

## Overview

Callers can use the `shared` instance or create a new instance if custom configuration is required.

```swift
let modelContainer = try await VLMModelFactory.shared.loadContainer(
    configuration: VLMRegistry.paligemma3bMix4488bit)
```

## Topics

### Initializers
- [init(typeRegistry: ModelTypeRegistry<LanguageModel>, processorRegistry: ProcessorTypeRegistry, modelRegistry: AbstractModelRegistry, conventionsRegistry: ChatConventionsRegistry, processorLoadingRegistry: VLMProcessorLoadingRegistry)](./vlmmodelfactory/init%28typeregistry,processorregistry,modelregistry,conventionsregistry,processorloadingregistry%29.md)
### Instance Properties
- [let conventionsRegistry: ChatConventionsRegistry](./vlmmodelfactory/conventionsregistry.md)
  resolvers for chat conventions that are keyed on model id rather than declared by the model itself, e.g. DeepSeek-R1
- [let modelRegistry: AbstractModelRegistry](./vlmmodelfactory/modelregistry.md)
  registry of model id to configuration, e.g. `mlx-community/paligemma-3b-mix-448-8bit`
- [let processorLoadingRegistry: VLMProcessorLoadingRegistry](./vlmmodelfactory/processorloadingregistry.md)
  resolvers for processor metadata that is absent or incorrect in a checkpoint
- [let processorRegistry: ProcessorTypeRegistry](./vlmmodelfactory/processorregistry.md)
  registry of input processor type, e.g. configuration value `PaliGemmaProcessor` -> configuration and init methods
- [let typeRegistry: ModelTypeRegistry<LanguageModel>](./vlmmodelfactory/typeregistry.md)
  registry of model type, e.g. configuration value `paligemma` -> configuration and init methods
### Instance Methods
- [func loraMetadata(configurationData: Data) async throws -> LoRAModelMetadata?](./vlmmodelfactory/lorametadata%28configurationdata%29.md)
  Returns the model’s LoRA metadata without loading checkpoint weights or a processor.
### Type Aliases
- [VLMModelFactory.ContainerType](./vlmmodelfactory/containertype.md)
- [VLMModelFactory.ContextType](./vlmmodelfactory/contexttype.md)
### Type Properties
- [static let shared: VLMModelFactory](./vlmmodelfactory/shared.md)
  Shared instance with default behavior.
### Default Implementations
- [GenericModelFactory Implementations](./vlmmodelfactory/genericmodelfactory-implementations.md)

## Relationships

### Conforms To
- MLXLMCommon.GenericModelFactory
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxvlm/vlmmodelfactory)*