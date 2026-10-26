---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddingmodel"
framework: "mlx-swift-lm/MLXEmbedders"
---

# EmbeddingModel

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: protocol  
**Role**: Protocol

## Declaration

```swift
protocol EmbeddingModel : BaseLanguageModel
```

## Topics

### Instance Properties
- [var maxPositionEmbeddings: Int?](./embeddingmodel/maxpositionembeddings.md)
  The maximum number of position embeddings supported by this model, or `nil` if the model uses a position encoding (e.g. RoPE) that handles arbitrary lengths.
- [var poolingStrategy: Pooling.Strategy?](./embeddingmodel/poolingstrategy.md)
- [var vocabularySize: Int](./embeddingmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput](./embeddingmodel/callasfunction%28_,positionids,tokentypeids,attentionmask%29.md)

## Relationships

### Inherits From
- MLXLMCommon.BaseLanguageModel
### Conforming Types
- [BertModel](./bertmodel.md)
- [BertRerankerModel](./bertrerankermodel.md)
- [BertSequenceClassificationRerankerModel](./bertsequenceclassificationrerankermodel.md)
- [DistilBertModel](./distilbertmodel.md)
- [EmbeddingGemma](./embeddinggemma.md)
- [EmbeddingGemma2](./mlxlmcommon/embeddinggemma2.md)
- [LFM2BidirectionalModel](./lfm2bidirectionalmodel.md)
- [NomicBertModel](./nomicbertmodel.md)
- [Qwen3Model](./qwen3model.md)


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddingmodel)*