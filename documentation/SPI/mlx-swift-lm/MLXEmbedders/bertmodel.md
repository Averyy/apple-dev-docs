---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertmodel"
framework: "mlx-swift-lm/MLXEmbedders"
---

# BertModel

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

The complete BERT model implementation.

## Declaration

```swift
class BertModel
```

#### Overview

`BertModel` coordinates the flow of data from raw input tokens to high-level contextual representations. It can be configured in two modes:

1. **Feature Extraction (Default)**: Produces sequence-level hidden states and a pooled sentence embedding (useful for similarity or classification).
2. **Language Modeling**: Attaches an `LMHead` to predict masked tokens.

## Topics

### Initializers
- [init(BertConfiguration, lmHead: Bool)](./bertmodel/init%28_,lmhead%29.md)
  Initializes a BERT model.
### Instance Properties
- [var maxPositionEmbeddings: Int?](./bertmodel/maxpositionembeddings.md)
- [var vocabularySize: Int](./bertmodel/vocabularysize.md)
  The total count of tokens in the model’s vocabulary.
### Instance Methods
- [func callAsFunction(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput](./bertmodel/callasfunction%28_,positionids,tokentypeids,attentionmask%29.md)
  Primary inference entry point.
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./bertmodel/sanitize%28weights%29.md)
  Maps external weight names (e.g., from Hugging Face) to this class’s internal structure.
### Default Implementations
- [BaseLanguageModel Implementations](./bertmodel/baselanguagemodel-implementations.md)
- [EmbeddingModel Implementations](./bertmodel/embeddingmodel-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Inherited By
- [DistilBertModel](./distilbertmodel.md)
### Conforms To
- [EmbeddingModel](./embeddingmodel.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertmodel)*