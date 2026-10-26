---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/applyrotaryposition(_:to:offset:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# applyRotaryPosition(_:to:offset:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Apply rotary position embeddings, using the cache offset when available.

## Declaration

```swift
func applyRotaryPosition<R>(_ rope: R, to x: MLXArray, offset: RoPEOffset?) -> MLXArray where R : ArrayOffsetLayer, R : OffsetLayer
```

#### Return Value

The input with rotary positional encoding applied.

#### Discussion

This function enables models to use a single call site instead of repeating conditional offset handling:

```swift
let offset = cache?.ropeOffset
queries = applyRotaryPosition(rope, to: queries, offset: offset)
keys = applyRotaryPosition(rope, to: keys, offset: offset)
```

## Parameters

- `rope`: A RoPE layer conforming to both `OffsetLayer` and `ArrayOffsetLayer`.
- `x`: The input tensor to apply RoPE to.
- `offset`: The offset into the rotary positional encoding.  0 if nil.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/applyrotaryposition(_:to:offset:))*