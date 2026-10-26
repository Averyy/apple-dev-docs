---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/cachestatus()"
framework: "mlx-swift-lm/MLXLMCommon"
---

# cacheStatus()

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Unified KV / recurrent-cache status for this session.

## Declaration

```swift
func cacheStatus() async throws -> KVCacheStatus
```

## Mentions

- [KV Cache Quantization](../kv-cache-quantization.md)

#### Discussion

If the session owns a realized cache, this reports its actual request, topology, strategy state, and progress. Otherwise it reports the cache planned by the current [`generateParameters`](./generateparameters.md).


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/chatsession/cachestatus())*