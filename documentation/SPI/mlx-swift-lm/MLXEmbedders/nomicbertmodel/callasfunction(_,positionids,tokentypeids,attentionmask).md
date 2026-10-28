---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/nomicbertmodel/callasfunction(_:positionids:tokentypeids:attentionmask:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# callAsFunction(_:positionIds:tokenTypeIds:attentionMask:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Performs the full forward pass of the model.

## Declaration

```swift
func callAsFunction(_ inputs: MLXArray, positionIds: MLXArray? = nil, tokenTypeIds: MLXArray? = nil, attentionMask: MLXArray? = nil) -> EmbeddingModelOutput
```

## Return Value

An `EmbeddingModelOutput` containing hidden states and optionally the pooled output.

## Discussion

This method handles:

1. Input reshaping (ensuring batch dimension exists).
2. Mask transformation (converting binary masks to additive log-masks).
3. Embedding -> Encoder flow.
4. Output formatting (Logic for returning Pooling vs LM Head outputs).

## Parameters

- `inputs`: Input token indices. Shape `[batch, seq_len]`.
- `positionIds`: Optional specific position indices.
- `tokenTypeIds`: Optional segment IDs.
- `attentionMask`: A binary mask (1 for keep, 0 for discard).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/nomicbertmodel/callasfunction(_:positionids:tokentypeids:attentionmask:))*