---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/maybequantizekvcache(cache:kvbits:kvgroupsize:quantizedkvstart:kvscheme:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# maybeQuantizeKVCache(cache:kvBits:kvGroupSize:quantizedKVStart:kvScheme:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Converts regular caches to quantized caches when:

## Declaration

```swift
func maybeQuantizeKVCache(cache: inout [KVCache], kvBits: Int?, kvGroupSize: Int = 64, quantizedKVStart: Int = 0, kvScheme: String? = nil)
```

## Mentions

- [KV Cache Quantization](./kv-cache-quantization.md)

#### Discussion

- kvBits is specified (or kvScheme resolves to a built-in affine scheme)
- The cache is not already quantized
- The cache offset is greater than quantizedKVStart

## Parameters

- `cache`: Array of KV caches to potentially quantize
- `kvBits`: Number of bits for quantization (nil = no quantization)
- `kvGroupSize`: Group size for quantization
- `quantizedKVStart`: Token count threshold to begin quantizing
- `kvScheme`: Scheme selector; overrides kvBits when it names a built-in affine scheme (“affine4”, “affine8”) or a TurboQuant scheme (“turbo4”, “turbo4v2”, …). Unrecognized schemes are left to custom cache implementations and do not quantize here.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/maybequantizekvcache(cache:kvbits:kvgroupsize:quantizedkvstart:kvscheme:))*