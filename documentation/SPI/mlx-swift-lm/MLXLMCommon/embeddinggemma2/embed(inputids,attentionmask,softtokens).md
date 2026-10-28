---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2/embed(inputids:attentionmask:softtokens:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# embed(inputIds:attentionMask:softTokens:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

## Declaration

```swift
func embed(inputIds: MLXArray, attentionMask: MLXArray?, softTokens: MLXArray? = nil) -> MLXArray
```

## Return Value

`[B, embeddingDim]` unit-length float32 embeddings.

## Parameters

- `inputIds`: `[B, L]` tokens.
- `attentionMask`: `[B, L]`, `1` for real tokens. Attention and pooling ignore padding.
- `softTokens`: `[soft tokens, hidden]` features of every image, video and audio placeholder in `inputIds`, in sequence order; single row only.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/embeddinggemma2/embed(inputids:attentionmask:softtokens:))*