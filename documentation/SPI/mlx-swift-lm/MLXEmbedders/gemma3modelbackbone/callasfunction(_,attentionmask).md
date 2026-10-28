---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/gemma3modelbackbone/callasfunction(_:attentionmask:)"
framework: "mlx-swift-lm/MLXEmbedders"
---

# callAsFunction(_:attentionMask:)

**Framework**: mlx-swift-lm/MLXEmbedders  
**Kind**: method  
**Role**: Instance Method

Processes input tokens through the model backbone.

## Declaration

```swift
func callAsFunction(_ inputs: MLXArray, attentionMask: MLXArray? = nil) -> MLXArray
```

## Return Value

Final hidden states of shape `[Batch, Length, HiddenSize]`.

## Parameters

- `inputs`: Array of token IDs of shape `[Batch, Length]`.
- `attentionMask`: Optional padding mask of shape `[Batch, Length]`, nonzero for real tokens. Used only when `useBidirectionalAttention` is `true`.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxembedders/gemma3modelbackbone/callasfunction(_:attentionmask:))*