---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/variancenormalizedkvcacheconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# VarianceNormalizedKVCacheConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Variance-normalized (KVarN-inspired) cache compression settings.

## Declaration

```swift
struct VarianceNormalizedKVCacheConfiguration
```

#### Overview

Completed tiles are rotated, dual-axis variance-normalized, and quantized asymmetrically (keys and values may use different bit widths). The intended use case is memory-constrained long-context decoding rather than latency- sensitive generation.

> ⚠️ **Warning**: This strategy is experimental. Models must route attention through `attentionWithCacheUpdate`; direct `KVCache.update` call sites use a full-cache materialization fallback that is not suitable for long-context decode.

## Topics

### Initializers
- [init(keyBits: Int, valueBits: Int, tileSize: Int, sinkhornIterations: Int, compressionStart: Int) throws](./variancenormalizedkvcacheconfiguration/init%28keybits,valuebits,tilesize,sinkhorniterations,compressionstart%29.md)
### Instance Properties
- [let compressionStart: Int](./variancenormalizedkvcacheconfiguration/compressionstart.md)
- [let keyBits: Int](./variancenormalizedkvcacheconfiguration/keybits.md)
- [let sinkhornIterations: Int](./variancenormalizedkvcacheconfiguration/sinkhorniterations.md)
- [let tileSize: Int](./variancenormalizedkvcacheconfiguration/tilesize.md)
- [let valueBits: Int](./variancenormalizedkvcacheconfiguration/valuebits.md)
### Type Properties
- [static let balanced: VarianceNormalizedKVCacheConfiguration](./variancenormalizedkvcacheconfiguration/balanced.md)
  4-bit keys and values for higher fidelity at still-reduced memory.
- [static let memoryFirst: VarianceNormalizedKVCacheConfiguration](./variancenormalizedkvcacheconfiguration/memoryfirst.md)
  4-bit keys and 2-bit values with 128-token tiles; the paper-inspired default.
### Default Implementations
- [Equatable Implementations](./variancenormalizedkvcacheconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/variancenormalizedkvcacheconfiguration)*