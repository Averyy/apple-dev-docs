---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A complete request for key-value cache storage during generation.

## Declaration

```swift
struct KVCacheConfiguration
```

## Mentions

- [KV Cache Quantization](./kv-cache-quantization.md)

#### Overview

This keeps cache capacity, compression, and compatibility semantics in one value so every generation path forwards the same configuration.

## Topics

### Structures
- [KVCacheConfiguration.Capacity](./kvcacheconfiguration/capacity-swift.struct.md)
  Attention window for caches whose capacity is caller-configurable.
- [KVCacheConfiguration.Rewind](./kvcacheconfiguration/rewind-swift.struct.md)
  Extra historical rows retained by rotating caches for exact prefix rewinds.
- [KVCacheConfiguration.Strategy](./kvcacheconfiguration/strategy-swift.struct.md)
  Opaque cache strategy. New strategies can be added without introducing public enum cases that clients must exhaustively switch over.
### Initializers
- [init(capacity: Capacity?, strategy: Strategy, compatibility: CompatibilityPolicy, rewind: Rewind?)](./kvcacheconfiguration/init%28capacity,strategy,compatibility,rewind%29.md)
### Instance Properties
- [var capacity: Capacity?](./kvcacheconfiguration/capacity-swift.property.md)
- [var compatibility: CompatibilityPolicy](./kvcacheconfiguration/compatibility.md)
- [var rewind: Rewind?](./kvcacheconfiguration/rewind-swift.property.md)
- [var strategy: Strategy](./kvcacheconfiguration/strategy-swift.property.md)
### Enumerations
- [KVCacheConfiguration.CompatibilityPolicy](./kvcacheconfiguration/compatibilitypolicy.md)
  Behavior when only part of a model’s cache topology supports the strategy.
### Default Implementations
- [Equatable Implementations](./kvcacheconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration)*