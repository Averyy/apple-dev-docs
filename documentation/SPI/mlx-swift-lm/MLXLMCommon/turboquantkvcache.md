---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TurboQuantKVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

KV cache using TurboQuant compression with two-phase architecture:

## Declaration

```swift
class TurboQuantKVCache
```

## Overview

**Phase 1, Prefill** (L>1): Store raw K/V like KVCacheSimple. Zero overhead. **Transition**: On first decode call, compress entire raw cache in one batch. **Phase 2, Decode** (L=1): Encode 1 new token. Metal kernel scores against all compressed tokens. Zero dequantization.

Both keys and values: Algorithm 1 (MSE at b bits, no QJL)

## Topics

### Initializers
- [init(bits: Int, keyBits: Int?, valueBits: Int?, seed: UInt64, keyGroupSize: Int)](./turboquantkvcache/init%28bits,keybits,valuebits,seed,keygroupsize%29.md)
### Instance Properties
- [let affineKeyMode: Bool](./turboquantkvcache/affinekeymode.md)
  Affine-K mode: keys stored as 8-bit affine-quantized (upstream QuantizedKVCache layout, groupSize 64) while values are TurboQuant compressed. The efficient K per the asymmetric-kv paper: near-lossless like FP16 keys at half the bytes. Enabled when keyBits == 8.
- [let bits: Int](./turboquantkvcache/bits.md)
- [var isCompressed: Bool](./turboquantkvcache/iscompressed.md)
  Whether we’ve transitioned from raw → compressed
- [var isTrimmable: Bool](./turboquantkvcache/istrimmable.md)
- [let keyBits: Int](./turboquantkvcache/keybits.md)
- [var keyGroupSize: Int](./turboquantkvcache/keygroupsize.md)
  Affine-K quantization group size. Defaults to 64, but callers that already know the head dimension (e.g. `maybeTurboQuantizeKVCache`) can pass a value pre-resolved via `resolvedKVQuantizationGroupSize` so kernels and quantization agree. Resolved (and possibly adjusted) against the actual head dimension the first time an affine-K encode runs, see `resolveAffineKeyGroupSize(headDim:)`.
- [var memoryBytes: Int](./turboquantkvcache/memorybytes.md)
  Actual memory footprint: compressed storage (packed indices + norms) for K and V, plus any raw FP16 buffers if still in prefill phase or rawKeyMode. Does NOT include codec overhead (rotation matrices, codebooks) which is shared across layers. In rawKeyMode: rawKeys is always present (FP16 keys), no keyPackedMSE/keyNorms.
- [var metaState: [String]](./turboquantkvcache/metastate.md)
- [let rawKeyMode: Bool](./turboquantkvcache/rawkeymode.md)
  Raw-K mode: keys stay at FP16 (uncompressed) while only values are TurboQuant compressed. This is the single biggest quality finding from TurboQuant+, K precision dominates quality via softmax amplification, V compression is nearly free (linear averaging). Enabled when keyBits == 0.
- [var state: [MLXArray]](./turboquantkvcache/state.md)
- [let valueBits: Int](./turboquantkvcache/valuebits.md)
### Instance Methods
- [func compressedAttention(queries: MLXArray, keys: MLXArray, values: MLXArray, scale: Float, mask: MLXFast.ScaledDotProductAttentionMaskMode) -> MLXArray](./turboquantkvcache/compressedattention%28queries,keys,values,scale,mask%29.md)
  Compressed-domain attention via Metal kernels.
- [func copy() -> any KVCache](./turboquantkvcache/copy%28%29.md)
- [func innerState() -> [MLXArray]](./turboquantkvcache/innerstate%28%29.md)
- [func trim(Int) -> Int](./turboquantkvcache/trim%28_%29.md)
- [func update(keys: MLXArray, values: MLXArray) -> (MLXArray, MLXArray)](./turboquantkvcache/update%28keys,values%29.md)
  Prefill update: store raw K/V, return raw. Zero encoding overhead. Uses KVCacheSimple-style allocation with concatenated growth.
### Type Properties
- [class var serializedClassName: String?](./turboquantkvcache/serializedclassname.md)
### Type Methods
- [class func restore(state: [MLXArray], metaState: [String]) throws -> any KVCache](./turboquantkvcache/restore%28state,metastate%29.md)

## Relationships

### Inherits From
- [BaseKVCache](./basekvcache.md)
### Conforms To
- [KVCache](./kvcache.md)
- MLX.Evaluatable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcache)*