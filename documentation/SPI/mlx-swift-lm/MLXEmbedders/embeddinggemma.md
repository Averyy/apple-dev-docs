---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddinggemma"
framework: "mlx-swift-lm/MLXEmbedders"
---

# EmbeddingGemma

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

A text embedding model based on Gemma 3.

## Declaration

```swift
class EmbeddingGemma
```

## Overview

This class conforms to `EmbeddingModel` and provides high-quality text embeddings by passing inputs through a `Gemma3ModelBackbone`, followed by mean pooling and a projection head.

## Topics

### Initializers
- [init(Gemma3Configuration)](./embeddinggemma/init%28_%29.md)
  Initializes the embedding model.
### Instance Properties
- [let config: Gemma3Configuration](./embeddinggemma/config.md)
  The model configuration.
- [var vocabularySize: Int](./embeddinggemma/vocabularysize.md)
  The size of the vocabulary.
### Instance Methods
- [func callAsFunction(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput](./embeddinggemma/callasfunction%28_,positionids,tokentypeids,attentionmask%29.md)
  Generates embeddings for the given inputs.
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./embeddinggemma/sanitize%28weights%29.md)
  Preprocesses the weights, handling key remapping and vocabulary truncation.
### Default Implementations
- [BaseLanguageModel Implementations](./embeddinggemma/baselanguagemodel-implementations.md)
- [EmbeddingModel Implementations](./embeddinggemma/embeddingmodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddinggemma)*