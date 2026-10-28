---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertmodel/callasfunction(_:positionids:tokentypeids:attentionmask:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# callAsFunction(_:positionIds:tokenTypeIds:attentionMask:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Primary inference entry point.

## Declaration

```swift
func callAsFunction(_ inputs: MLXArray, positionIds: MLXArray? = nil, tokenTypeIds: MLXArray? = nil, attentionMask: MLXArray? = nil) -> EmbeddingModelOutput
```

## Return Value

An `EmbeddingModelOutput` containing hidden states and/or pooled vectors.

## Parameters

- `inputs`: Token IDs [Batch, SeqLen].
- `positionIds`: Optional indices for positions.
- `tokenTypeIds`: Optional segment IDs (0 or 1).
- `attentionMask`: Binary mask (1 for active, 0 for padding).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/bertmodel/callasfunction(_:positionids:tokentypeids:attentionmask:))*