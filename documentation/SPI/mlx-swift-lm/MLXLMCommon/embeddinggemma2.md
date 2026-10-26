---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2"
framework: "mlx-swift-lm/MLXLMCommon"
---

# EmbeddingGemma2

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

EmbeddingGemma 2: a bidirectional text encoder with per-layer embeddings that maps text and the soft tokens of images, video frames and audio into one normalized [`embeddingDim`](./embeddinggemma2configuration/embeddingdim.md) space. Load checkpoints with `loadWeights`. Vision and audio load independently on first use by default; keep the checkpoint files readable until then.

## Declaration

```swift
final class EmbeddingGemma2
```

## Topics

### Initializers
- [init(EmbeddingGemma2Configuration)](./embeddinggemma2/init%28_%29.md)
### Instance Properties
- [let config: EmbeddingGemma2Configuration](./embeddinggemma2/config.md)
- [var excludedCheckpointNamespaces: [String]](./embeddinggemma2/excludedcheckpointnamespaces.md)
- [var modelComponents: [ModelComponent : [CheckpointComponent]]](./embeddinggemma2/modelcomponents.md)
- [var onDemandComponents: [AnyOnDemandComponent]](./embeddinggemma2/ondemandcomponents.md)
### Instance Methods
- [func audioFeatures(MLXArray) throws -> MLXArray?](./embeddinggemma2/audiofeatures%28_%29.md)
- [func embed(inputIds: MLXArray, attentionMask: MLXArray?, softTokens: MLXArray?) -> MLXArray](./embeddinggemma2/embed%28inputids,attentionmask,softtokens%29.md)
- [func imageFeatures(MLXArray) throws -> MLXArray?](./embeddinggemma2/imagefeatures%28_%29.md)
- [func prepareCheckpoint(ModelCheckpoint) throws -> ModelCheckpoint](./embeddinggemma2/preparecheckpoint%28_%29.md)
- [func sanitize(weights: [String : MLXArray]) throws -> [String : MLXArray]](./embeddinggemma2/sanitize%28weights%29.md)
  Keeps the text model and the encoders this configuration loads. PyTorch checkpoints store convolution kernels channels-first; they move to the channels-last layout of MLX.
### Default Implementations
- [BaseLanguageModel Implementations](./embeddinggemma2/baselanguagemodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- [BaseLanguageModel](./baselanguagemodel.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- [ModelComponentsProviding](./modelcomponentsproviding.md)
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2)*