---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/maybeturboquantizekvcache(cache:keybits:valuebits:quantizedkvstart:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# maybeTurboQuantizeKVCache(cache:keyBits:valueBits:quantizedKVStart:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: func  
**Role**: Function

Convert eligible `KVCacheSimple` layers to `TurboQuantKVCache` once their offset passes `quantizedKVStart`, transferring the accumulated KV state. Mamba / wrapper caches are left untouched. `RotatingKVCache` layers (Gemma-style sliding-window) are also left untouched – see `logRotatingKVCacheSkipOnce` – since they are already memory-bounded by their window size and their rotating storage layout does not fit the sequential-append compression path. Called from `maybeQuantizeKVCache` when `kvScheme` names a TurboQuant scheme.

## Declaration

```swift
@discardableResult
func maybeTurboQuantizeKVCache(cache: inout [KVCache], keyBits: Int, valueBits: Int, quantizedKVStart: Int) -> Bool
```


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/maybeturboquantizekvcache(cache:keybits:valuebits:quantizedkvstart:))*