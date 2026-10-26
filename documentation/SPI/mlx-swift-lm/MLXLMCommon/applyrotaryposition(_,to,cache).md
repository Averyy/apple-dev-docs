---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/applyrotaryposition(_:to:cache:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# applyRotaryPosition(_:to:cache:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Apply rotary position embeddings, using the cache offset when available.

> **Deprecated**: use applyRotaryPosition(_:to:offset:) instead

## Declaration

```swift
func applyRotaryPosition<R>(_ rope: R, to x: MLXArray, cache: KVCache?) -> MLXArray where R : ArrayOffsetLayer, R : OffsetLayer
```

#### Return Value

The input with rotary positional encoding applied.

## Parameters

- `rope`: A RoPE layer conforming to both `OffsetLayer` and `ArrayOffsetLayer`.
- `x`: The input tensor to apply RoPE to.
- `cache`: The KV cache (determines scalar or per-sequence offset), or `nil` for offset 0.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/applyrotaryposition(_:to:cache:))*