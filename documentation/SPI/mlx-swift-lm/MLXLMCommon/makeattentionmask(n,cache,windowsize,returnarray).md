---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makeattentionmask(n:cache:windowsize:returnarray:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# makeAttentionMask(n:cache:windowSize:returnArray:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Create an attention mask matching mlx-lm’s create_attention_mask helper.

## Declaration

```swift
func makeAttentionMask(n: Int, cache: KVCache?, windowSize: Int? = nil, returnArray: Bool = false) -> MLXFast.ScaledDotProductAttentionMaskMode
```

## Discussion

This returns `.causal` when a symbolic mask is sufficient, avoiding materializing a full mask array.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/makeattentionmask(n:cache:windowsize:returnarray:))*