---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/pooling/callasfunction(_:mask:normalize:applylayernorm:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# callAsFunction(_:mask:normalize:applyLayerNorm:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Processes the input hidden states according to the configured strategy.

## Declaration

```swift
func callAsFunction(_ inputs: EmbeddingModelOutput, mask: MLXArray? = nil, normalize: Bool = false, applyLayerNorm: Bool = false) -> MLXArray
```

#### Return Value

An `MLXArray` representing the pooled embedding.

## Parameters

- `inputs`: The `EmbeddingModelOutput` containing hidden states and/or pooled output.
- `mask`: An optional `MLXArray` mask (usually 1 for tokens, 0 for padding).
- `normalize`: If `true`, L2 normalizes the resulting vector.
- `applyLayerNorm`: If `true`, applies Layer Normalization before truncation/normalization.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/pooling/callasfunction(_:mask:normalize:applylayernorm:))*