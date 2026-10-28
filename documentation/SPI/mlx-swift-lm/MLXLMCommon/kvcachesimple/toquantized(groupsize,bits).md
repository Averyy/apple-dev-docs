---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachesimple/toquantized(groupsize:bits:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# toQuantized(groupSize:bits:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Convert to a quantized cache for maximum efficiency.

## Declaration

```swift
func toQuantized(groupSize: Int = 64, bits: Int = 4) throws -> QuantizedKVCache
```

## Discussion

Use `updateQuantized()` and `quantizedScaledDotProductAttention()` for zero-overhead operation.

> **Throws**: If neither the requested group size nor another supported group size can represent both the key and value head dimensions.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachesimple/toquantized(groupsize:bits:))*