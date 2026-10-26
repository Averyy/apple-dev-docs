---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachelayerstatus"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheLayerStatus

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Effective state of one leaf in a model’s cache topology.

## Declaration

```swift
struct KVCacheLayerStatus
```

#### Overview

This is shared by the high-level [`KVCacheStatus`](./kvcachestatus.md) API and the lower-level [`KVCacheRuntimeReport`](./kvcacheruntimereport.md) compatibility view.

## Topics

### Instance Properties
- [let capacitySource: CapacitySource?](./kvcachelayerstatus/capacitysource-swift.property.md)
  `nil` for recurrent or other non-attention state.
- [let kind: CacheLayerKind](./kvcachelayerstatus/kind.md)
- [let memoryBytes: Int](./kvcachelayerstatus/memorybytes.md)
  Bytes allocated for this layer’s arrays, including space reserved for tokens not yet written.
- [let path: [Int]](./kvcachelayerstatus/path.md)
  Stable path through top-level and composite cache entries.
- [let reason: Reason?](./kvcachelayerstatus/reason-swift.property.md)
- [let resolvedStrategy: KVCacheStrategyIdentifier?](./kvcachelayerstatus/resolvedstrategy.md)
- [let state: State](./kvcachelayerstatus/state-swift.property.md)
### Enumerations
- [KVCacheLayerStatus.CapacitySource](./kvcachelayerstatus/capacitysource-swift.enum.md)
  Where an attention layer’s resident-token bound originated.
- [KVCacheLayerStatus.Reason](./kvcachelayerstatus/reason-swift.enum.md)
- [KVCacheLayerStatus.State](./kvcachelayerstatus/state-swift.enum.md)
### Default Implementations
- [Equatable Implementations](./kvcachelayerstatus/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachelayerstatus)*