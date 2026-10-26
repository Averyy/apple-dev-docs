---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/createattentionmask(h:cache:windowsize:returnarray:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# createAttentionMask(h:cache:windowSize:returnArray:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Create an attention mask with explicit window size parameter.

## Declaration

```swift
func createAttentionMask(h: MLXArray, cache: KVCache?, windowSize: Int? = nil, returnArray: Bool = false) -> MLXFast.ScaledDotProductAttentionMaskMode
```

#### Return Value

Attention mask mode for scaled dot product attention

## Parameters

- `h`: The input array (used to determine sequence length)
- `cache`: Optional single KV cache
- `windowSize`: Optional sliding window size (if provided, creates windowed attention)
- `returnArray`: Force return of array mask instead of symbolic “causal”


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/createattentionmask(h:cache:windowsize:returnarray:))*