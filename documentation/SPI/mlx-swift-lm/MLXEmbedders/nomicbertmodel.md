---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/nomicbertmodel"
framework: "mlx-swift-lm/MLXEmbedders"
---

# NomicBertModel

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

The main entry point for the Nomic BERT model.

## Declaration

```swift
class NomicBertModel
```

## Overview

This class serves as the container for the entire architecture. It connects the embeddings, the encoder stack, and the optional output heads (Pooler or LM Head). It also handles weight key sanitization to ensure compatibility with checkpoints trained in other frameworks (e.g., PyTorch / Hugging Face).

## Topics

### Initializers
- [init(NomicBertConfiguration, pooler: Bool, lmHead: Bool)](./nomicbertmodel/init%28_,pooler,lmhead%29.md)
  Initializes the Nomic BERT model.
### Instance Properties
- [var maxPositionEmbeddings: Int?](./nomicbertmodel/maxpositionembeddings.md)
- [var vocabularySize: Int](./nomicbertmodel/vocabularysize.md)
  The size of the vocabulary.
### Instance Methods
- [func callAsFunction(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput](./nomicbertmodel/callasfunction%28_,positionids,tokentypeids,attentionmask%29.md)
  Performs the full forward pass of the model.
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./nomicbertmodel/sanitize%28weights%29.md)
  Remaps weight keys from external formats (e.g., Hugging Face) to this model’s internal structure.
### Default Implementations
- [BaseLanguageModel Implementations](./nomicbertmodel/baselanguagemodel-implementations.md)
- [EmbeddingModel Implementations](./nomicbertmodel/embeddingmodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/nomicbertmodel)*