---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertrerankermodel"
framework: "mlx-swift-lm/MLXEmbedders"
---

# BertRerankerModel

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

BERT/RoBERTa-style sequence-classification model used by encoder reranker checkpoints.

## Declaration

```swift
class BertRerankerModel
```

## Topics

### Initializers
- [init(BertConfiguration)](./bertrerankermodel/init%28_%29.md)
### Instance Properties
- [var maxPositionEmbeddings: Int?](./bertrerankermodel/maxpositionembeddings.md)
- [var vocabularySize: Int](./bertrerankermodel/vocabularysize.md)
  The total count of tokens in the model’s vocabulary.
### Instance Methods
- [func callAsFunction(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput](./bertrerankermodel/callasfunction%28_,positionids,tokentypeids,attentionmask%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./bertrerankermodel/sanitize%28weights%29.md)
  Maps external weight names (e.g., from Hugging Face) to this class’s internal structure.
- [func score(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> MLXArray](./bertrerankermodel/score%28_,positionids,tokentypeids,attentionmask%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./bertrerankermodel/baselanguagemodel-implementations.md)
- [EmbeddingModel Implementations](./bertrerankermodel/embeddingmodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertrerankermodel)*