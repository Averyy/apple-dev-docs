---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache/makemask(n:windowsize:returnarray:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# makeMask(n:windowSize:returnArray:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method  
**Required**: Yes

Create an attention mask for this cache

## Declaration

```swift
func makeMask(n: Int, windowSize: Int?, returnArray: Bool) -> MLXFast.ScaledDotProductAttentionMaskMode
```

## Return Value

Attention mask mode for scaled dot product attention

## Discussion

This method encapsulates cache-specific mask creation logic. Implementations should handle offset capping, window size logic, and optimization decisions (symbolic vs array masks).

## Parameters

- `n`: The sequence length for the new tokens
- `windowSize`: Optional sliding window size
- `returnArray`: Force return of array mask instead of symbolic


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcache/makemask(n:windowsize:returnarray:))*