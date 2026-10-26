---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel"
framework: "mlx-swift-lm/MLXLMCommon"
---

# BaseLanguageModel

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Abstract form of a model that processes language.

## Declaration

```swift
protocol BaseLanguageModel : Module
```

## Topics

### Instance Properties
- [var excludedCheckpointNamespaces: [String]](./baselanguagemodel/excludedcheckpointnamespaces.md)
  Serialized namespaces whose tensors this model never loads, such as the target model in a checkpoint that a drafter shares with it. The loader does not read them.
### Instance Methods
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./baselanguagemodel/preparecheckpoint%28_%29.md)
  Normalize tensor names, values, and layer settings before loading the checkpoint. The default implementation calls [`sanitize(weights:metadata:)`](./baselanguagemodel/sanitize%28weights,metadata%29.md).
- [func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]](./baselanguagemodel/sanitize%28weights%29.md)
  Optionally preprocess the weights and modify / remove values as needed. Errors propagate to the checkpoint loader.
- [func sanitize(weights: [String : MLXArray], metadata: [String : String]) throws -> [String : MLXArray]](./baselanguagemodel/sanitize%28weights,metadata%29.md)
  Optionally preprocess the weights with access to safetensor metadata.

## Relationships

### Inherits From
- MLXNN.Module
### Inherited By
- [LanguageModel](./languagemodel.md)
- [MTPDrafterModel](./mtpdraftermodel.md)
- [ModelComponentsProviding](./modelcomponentsproviding.md)
- [StatefulMTPDrafterModel](./statefulmtpdraftermodel.md)
### Conforming Types
- [EmbeddingGemma2](./embeddinggemma2.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baselanguagemodel)*