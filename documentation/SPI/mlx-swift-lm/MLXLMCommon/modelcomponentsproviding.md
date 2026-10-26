---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcomponentsproviding"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelComponentsProviding

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A model with components that can load separately or not at all.

## Declaration

```swift
protocol ModelComponentsProviding : BaseLanguageModel
```

## Mentions

- [Model Compatibility](./model-compatibility.md)

#### Overview

Before the loader reads the checkpoint, it removes the modules of each component that does not load now, and it does not read their tensors. The module tree does not change after the load. An on-demand component loads later through the same [`prepareCheckpoint(_:)`](./baselanguagemodel/preparecheckpoint%28_%29.md), quantization and validation as the model.

## Topics

### Instance Properties
- [var modelComponents: [ModelComponent : [CheckpointComponent]]](./modelcomponentsproviding/modelcomponents.md)
  The checkpoint components that make up each model component.
- [var onDemandComponents: [AnyOnDemandComponent]](./modelcomponentsproviding/ondemandcomponents.md)
  Components that load the first time an input needs them. The default is empty.

## Relationships

### Inherits From
- [BaseLanguageModel](./baselanguagemodel.md)
### Conforming Types
- [EmbeddingGemma2](./embeddinggemma2.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcomponentsproviding)*