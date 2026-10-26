---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertsequenceclassificationrerankermodel"
framework: "mlx-swift-lm/MLXEmbedders"
---

# BertSequenceClassificationRerankerModel

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

BERT sequence-classification model used by reranker checkpoints with pooled-output heads.

## Declaration

```swift
class BertSequenceClassificationRerankerModel
```

## Topics

### Initializers
- [init(BertConfiguration)](./bertsequenceclassificationrerankermodel/init%28_%29.md)
### Instance Properties
- [var maxPositionEmbeddings: Int?](./bertsequenceclassificationrerankermodel/maxpositionembeddings.md)
- [var vocabularySize: Int](./bertsequenceclassificationrerankermodel/vocabularysize.md)
  The total count of tokens in the model’s vocabulary.
### Instance Methods
- [func callAsFunction(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput](./bertsequenceclassificationrerankermodel/callasfunction%28_,positionids,tokentypeids,attentionmask%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./bertsequenceclassificationrerankermodel/sanitize%28weights%29.md)
- [func score(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> MLXArray](./bertsequenceclassificationrerankermodel/score%28_,positionids,tokentypeids,attentionmask%29.md)
### Default Implementations
- [BaseLanguageModel Implementations](./bertsequenceclassificationrerankermodel/baselanguagemodel-implementations.md)
- [EmbeddingModel Implementations](./bertsequenceclassificationrerankermodel/embeddingmodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertsequenceclassificationrerankermodel)*