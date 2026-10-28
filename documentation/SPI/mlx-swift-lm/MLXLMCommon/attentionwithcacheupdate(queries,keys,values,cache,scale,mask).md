---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/attentionwithcacheupdate(queries:keys:values:cache:scale:mask:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# attentionWithCacheUpdate(queries:keys:values:cache:scale:mask:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Automatic attention with cache update

## Declaration

```swift
func attentionWithCacheUpdate(queries: MLXArray, keys: MLXArray, values: MLXArray, cache: KVCache?, scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode = .none) -> MLXArray
```

## Return Value

Attention output [B, nHeads, L, D]

## Discussion

This function matches Python’s `scaled_dot_product_attention` in base.py:

- Detects if cache is `QuantizedKVCache` using `isinstance` pattern
- Detects cache-native attention implementations
- Routes to `quantizedScaledDotProductAttention` or `MLXFast.scaledDotProductAttention`
- Handles cache updating automatically
- Transparent to models - they just call this function

**Usage in models:**

```swift
let output = attentionWithCacheUpdate(
    queries: queries,
    keys: keys,
    values: values,
    cache: cache,
    scale: scale,
    mask: mask
)
```

## Parameters

- `queries`: Query tensor [B, nHeads, L, D]
- `keys`: Raw key tensor to be cached [B, nKVHeads, L, D]
- `values`: Raw value tensor to be cached [B, nKVHeads, L, D]
- `cache`: Cache instance (any type)
- `scale`: Attention scale factor
- `mask`: Attention mask


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/attentionwithcacheupdate(queries:keys:values:cache:scale:mask:))*