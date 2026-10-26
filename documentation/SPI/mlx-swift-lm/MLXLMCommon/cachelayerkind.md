---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelayerkind"
framework: "mlx-swift-lm/MLXLMCommon"
---

# CacheLayerKind

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

How a single model layer retains state across generation steps.

## Declaration

```swift
enum CacheLayerKind
```

#### Overview

This is the stable, descriptive counterpart to concrete [`KVCache`](./kvcache.md) instances. Obtain it through [`KVCacheStatus`](./kvcachestatus.md) rather than inspecting or casting runtime cache objects.

## Topics

### Enumeration Cases
- [CacheLayerKind.attention(maxSize:)](./cachelayerkind/attention%28maxsize%29.md)
  Standard or implementation-defined attention KV.
- [case composite([CacheLayerKind])](./cachelayerkind/composite%28_%29.md)
  Composite per-layer cache ([`CacheList`](./cachelist.md)), e.g. Mamba + attention.
- [CacheLayerKind.rotatingAttention(maxSize:keep:)](./cachelayerkind/rotatingattention%28maxsize,keep%29.md)
  Sliding / rotating attention window ([`RotatingKVCache`](./rotatingkvcache.md)).
- [CacheLayerKind.stateSpace](./cachelayerkind/statespace.md)
  Fixed-size state-space / Mamba / GDN recurrent state ([`MambaCache`](./mambacache.md)).
### Instance Properties
- [var attentionMaxSize: Int?](./cachelayerkind/attentionmaxsize.md)
  Effective attention token budget, if any.
- [var isAttention: Bool](./cachelayerkind/isattention.md)
  Whether this kind stores attention keys/values that can be size-limited.
- [var isBoundedAttention: Bool](./cachelayerkind/isboundedattention.md)
  Whether this kind is a bounded attention window.
### Default Implementations
- [Equatable Implementations](./cachelayerkind/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/cachelayerkind)*