---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddinggemma/callasfunction(_:positionids:tokentypeids:attentionmask:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# callAsFunction(_:positionIds:tokenTypeIds:attentionMask:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Generates embeddings for the given inputs.

## Declaration

```swift
func callAsFunction(_ inputs: MLXArray, positionIds: MLXArray?, tokenTypeIds: MLXArray?, attentionMask: MLXArray?) -> EmbeddingModelOutput
```

#### Return Value

An `EmbeddingModelOutput` containing the full hidden states and the pooled sentence embedding.

## Parameters

- `inputs`: Input token indices of shape `[Batch, Length]`.
- `positionIds`: Optional indices for positional information.
- `tokenTypeIds`: Optional indices for segment/type information.
- `attentionMask`: Optional mask for padding tokens, `[Batch, Length]` or `[Length]`, nonzero for real tokens. Pooling always uses it; attention uses it to hide padded keys when `useBidirectionalAttention` is `true`. Padded batches require `attentionMask`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/embeddinggemma/callasfunction(_:positionids:tokentypeids:attentionmask:))*