---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatingkvcache/toquantized(groupsize:bits:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# toQuantized(groupSize:bits:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Convert to a quantized cache.

## Declaration

```swift
func toQuantized(groupSize: Int = 64, bits: Int = 4) throws -> QuantizedKVCache
```

#### Discussion

Rotating-cache quantization needs a representation that preserves temporal ordering and rotation metadata. Until that representation exists, callers can recover by retaining the full-precision rotating cache.

> **Throws**: Always, because rotating-cache quantization is not implemented.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatingkvcache/toquantized(groupsize:bits:))*