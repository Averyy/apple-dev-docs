---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/compressedattention(queries:keys:values:scale:mask:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# compressedAttention(queries:keys:values:scale:mask:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Compressed-domain attention via Metal kernels.

## Declaration

```swift
func compressedAttention(queries: MLXArray, keys newKeys: MLXArray, values newValues: MLXArray, scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode = .none) -> MLXArray
```

## Discussion

On first call: compresses raw prefill cache in one batch. Then: encode 1 new token → fused attention kernel → inverse rotation.

For L=1 (decode): uses TurboFlashAttention, a single Metal dispatch that fuses Q×K scoring + online softmax + Attn×V aggregation. No intermediate score or weight arrays are materialized. This reduces 3 dispatches (score + softmax + value) to 1.

For L>1 (prefill chunks): falls back to separate score → softmax → value kernels since causal masking across multiple query positions requires the full score matrix.

In rawKeyMode: uses standard matmul for Q*K scoring (raw FP16 keys, no rotation), then compressed-domain Metal kernel for Attn*V (TurboQuant compressed values). TurboFlash is NOT used, it assumes both K and V are packed.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache/compressedattention(queries:keys:values:scale:mask:))*