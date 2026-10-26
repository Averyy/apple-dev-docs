---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/auxiliarykvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# AuxiliaryKVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

A cache entry that holds no attention state, such as a record of the tokens processed so far.

## Declaration

```swift
protocol AuxiliaryKVCache : KVCache
```

#### Overview

Cache policy skips these entries: capacity and compression settings, offset alignment checks, and [`KVCacheStatus`](./kvcachestatus.md) layers ignore them. Generation still trims, copies, and saves them with the other entries, so an auxiliary cache must be trimmable to keep pace, and it needs a [`serializedClassName`](./kvcache/serializedclassname.md) to be saved to a prompt cache file.

Staged speculative rounds (MTP) write through an auxiliary entry and trim it back to the accepted positions, so it must stay trimmable after the round’s width.

## Relationships

### Inherits From
- [KVCache](./kvcache.md)
- MLX.Evaluatable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/auxiliarykvcache)*