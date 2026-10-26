---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/qwen3model/callasfunction(_:positionids:tokentypeids:attentionmask:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# callAsFunction(_:positionIds:tokenTypeIds:attentionMask:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Forward pass to generate embeddings.

## Declaration

```swift
func callAsFunction(_ inputIds: MLXArray, positionIds: MLXArray? = nil, tokenTypeIds: MLXArray? = nil, attentionMask: MLXArray? = nil) -> EmbeddingModelOutput
```

#### Return Value

An `EmbeddingModelOutput` containing the final hidden states.

## Parameters

- `inputIds`: Tensor of token indices.
- `positionIds`: Optional indices for positional information.
- `tokenTypeIds`: Optional indices for segment-based tasks.
- `attentionMask`: Optional `[Batch, Length]` key-padding mask (nonzero = attend). Honored, not decorative: without it a padded batch lets real tokens attend to padding keys whenever padding precedes them (left padding, the Hugging Face default for this model family).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/qwen3model/callasfunction(_:positionids:tokentypeids:attentionmask:))*