---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/batchpositionedkvcache"
framework: "mlx-swift-lm/MLXLMCommon"
---

# BatchPositionedKVCache

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: protocol  
**Role**: Protocol

Protocol for KV caches that expose per-sequence RoPE offsets.

## Declaration

```swift
protocol BatchPositionedKVCache : KVCache
```

## Overview

This is a forward-compatible hook for batched caches. Current scalar-cache code paths continue using `KVCache.offset`.

## Topics

### Instance Properties
- [var batchOffset: MLXArray](./batchpositionedkvcache/batchoffset.md)
  Per-sequence RoPE offsets with shape `[B]`.

## Relationships

### Inherits From
- [KVCache](./kvcache.md)
- MLX.Evaluatable


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/batchpositionedkvcache)*