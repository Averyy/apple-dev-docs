---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/kvscheme"
framework: "mlx-swift-lm/MLXLMCommon"
---

# kvScheme

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: property  
**Role**: Instance Property

KV cache compression scheme. Overrides kvBits when set.

## Declaration

```swift
var kvScheme: String?
```

#### Discussion

Built-in affine: “affine4”, “affine8” (equivalent to kvBits 4/8).

TurboQuant schemes (`turbo<K>v<V>`, keys × values). Start light, verify quality on your model, then ratchet V:

- “turbo0v4”  FP16 K + 4-bit V, the safest start
- “turbo0v3”/“turbo0v2”  FP16 K, more aggressive V
- “turbo8v4”  8-bit affine K + 4-bit V, conservative asymmetric
- “turbo8v3”  recommended default (near-lossless K, compressed V)
- “turbo8v2”  aggressive V (boundary-layer protection auto-engages)
- “turbo4”/“turbo4v2”/“turbo3”/“turbo2”  turbo-quantized keys: maximum compression; K sensitivity varies by model family, so validate on your model (asym is the recommended starting point).

Variance-normalized (KVarN-inspired) schemes for memory-bound long context:

- “varn” / “varn4v2”  4-bit K + 2-bit V, 128-token tiles
- “varn4” / “varn4v4”  4-bit K/V
- “varn2” / “varn2v2”  2-bit K/V
- “varn4v2t32” / “varn4v2t64”  explicit tile size variants

Unrecognized schemes are rejected when generation starts. Prefer [`kvCache`](./kvcache.md) for compile-time-safe configuration.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/generateparameters/kvscheme)*