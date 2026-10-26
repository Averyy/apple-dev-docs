---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/qwen3model"
framework: "mlx-swift-lm/MLXEmbedders"
---

# Qwen3Model

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

The top-level Qwen3 model class providing embedding-level outputs.

## Declaration

```swift
class Qwen3Model
```

#### Overview

This class conforms to `EmbeddingModel`, making it suitable for use as a base for Causal Language Models or as a standalone encoder for generating text embeddings.

## Topics

### Initializers
- [init(Qwen3Configuration)](./qwen3model/init%28_%29.md)
  Initializes the Qwen3 Model.
### Instance Properties
- [let kvHeads: [Int]](./qwen3model/kvheads.md)
  An array specifying the number of KV heads for each layer. Useful for initializing KV caches during inference.
- [let poolingStrategy: Pooling.Strategy?](./qwen3model/poolingstrategy.md)
  Qwen3 embedding models use the final non-padding token as the sentence representation.
- [let vocabularySize: Int](./qwen3model/vocabularysize.md)
  The size of the vocabulary used for tokenization.
### Instance Methods
- [func callAsFunction(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput](./qwen3model/callasfunction%28_,positionids,tokentypeids,attentionmask%29.md)
  Forward pass to generate embeddings.
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./qwen3model/sanitize%28weights%29.md)
  Cleans and remaps external weight keys to match the internal module structure.
### Default Implementations
- [BaseLanguageModel Implementations](./qwen3model/baselanguagemodel-implementations.md)
- [EmbeddingModel Implementations](./qwen3model/embeddingmodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- [EmbeddingModel](./embeddingmodel.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/qwen3model)*