---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/createattentionmask(h:cache:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# createAttentionMask(h:cache:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Create an attention mask using the parameters from the KVCache.

## Declaration

```swift
func createAttentionMask(h: MLXArray, cache: [KVCache]?) -> MLXArray?
```

## Discussion

The mask is sized by the cache, so it spans the keys the cache still presents: an evicting cache drops rows the absolute offset would include.

See also `MultiHeadAttention.createAdditiveCausalMask(_:dtype:)` – same idea but doesn’t honor the cache offset.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/createattentionmask(h:cache:))*