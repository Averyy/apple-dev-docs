---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/distilbertmodel"
framework: "mlx-swift-lm/MLXEmbedders"
---

# DistilBertModel

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

A streamlined version of the BERT model.

## Declaration

```swift
class DistilBertModel
```

#### Overview

DistilBERT is a small, fast, cheap and light Transformer model trained by distilling BERT base. It has less parameters than bert-base-uncased and runs faster while preserving the majority of BERT’s performance.

## Topics

### Instance Methods
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./distilbertmodel/sanitize%28weights%29.md)
  Remaps DistilBERT-specific weight keys to the internal MLX architecture.

## Relationships

### Inherits From
- [BertModel](./bertmodel.md)
### Conforms To
- [EmbeddingModel](./embeddingmodel.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXLMCommon.BaseLanguageModel
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/distilbertmodel)*