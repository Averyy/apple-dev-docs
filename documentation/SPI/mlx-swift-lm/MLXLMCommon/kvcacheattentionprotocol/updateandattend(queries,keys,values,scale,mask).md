---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheattentionprotocol/updateandattend(queries:keys:values:scale:mask:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# updateAndAttend(queries:keys:values:scale:mask:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Update the cache with new K/V tensors and compute attention without first returning a fully materialized cache tensor pair.

## Declaration

```swift
func updateAndAttend(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode) -> MLXArray
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheattentionprotocol/updateandattend(queries:keys:values:scale:mask:))*