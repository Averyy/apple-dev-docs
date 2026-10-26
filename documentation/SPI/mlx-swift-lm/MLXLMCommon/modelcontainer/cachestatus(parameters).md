---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/cachestatus(parameters:)"
framework: "mlx-swift-lm/MLXLMCommon"
---

# cacheStatus(parameters:)

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: method  
**Role**: Instance Method

Authoritative planned cache status for the given generation parameters.

## Declaration

```swift
func cacheStatus(parameters: GenerateParameters? = nil) async throws -> KVCacheStatus
```

## Mentions

- [KV Cache Quantization](../kv-cache-quantization.md)

#### Discussion

Reports topology, capacity provenance, and strategy compatibility without requiring application code to allocate or cast concrete [`KVCache`](../kvcache.md) types.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelcontainer/cachestatus(parameters:))*