---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/lfm2bidirectionalmodel"
framework: "mlx-swift-lm/MLXEmbedders"
---

# LFM2BidirectionalModel

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: class  
**Role**: Class

LFM2.5 bidirectional encoder for retrieval. One class serves both heads, selected by the `"mlx"` block in config.json:

## Declaration

```swift
final class LFM2BidirectionalModel
```

#### Overview

- `embedding`: returns the backbone hidden states `(B, L, hidden)`; callers pool with `.cls` + `normalize` to get a 1024-d sentence vector (cosine similarity).
- `colbert`: applies a per-token Dense projection -> `(B, L, projDim)`; callers pool with `.none` + `normalize` to get per-token multi-vectors (MaxSim).

## Topics

### Initializers
- [init(LFM2BidirectionalConfiguration)](./lfm2bidirectionalmodel/init%28_%29.md)
### Instance Properties
- [let configuration: LFM2BidirectionalConfiguration](./lfm2bidirectionalmodel/configuration.md)
- [var poolingStrategy: Pooling.Strategy?](./lfm2bidirectionalmodel/poolingstrategy.md)
- [var vocabularySize: Int](./lfm2bidirectionalmodel/vocabularysize.md)
### Instance Methods
- [func callAsFunction(MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput](./lfm2bidirectionalmodel/callasfunction%28_,positionids,tokentypeids,attentionmask%29.md)
- [func sanitize(weights: [String : MLXArray]) -> [String : MLXArray]](./lfm2bidirectionalmodel/sanitize%28weights%29.md)
  Weights from `convert.py` are already `model.`-prefixed (and the ColBERT head is the bare key `dense.weight`), so this only applies the depthwise Conv1d transpose guard — `(O, 1, K)` -> `(O, K, 1)` — for robustness against weights re-converted straight from Hugging Face. It must NOT blanket-prepend `model.` (that would corrupt `dense.weight`).
### Default Implementations
- [BaseLanguageModel Implementations](./lfm2bidirectionalmodel/baselanguagemodel-implementations.md)
- [EmbeddingModel Implementations](./lfm2bidirectionalmodel/embeddingmodel-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/lfm2bidirectionalmodel)*