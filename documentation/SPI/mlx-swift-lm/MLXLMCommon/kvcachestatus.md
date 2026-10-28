---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachestatus"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheStatus

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Authoritative planned or realized state of a model’s KV / recurrent cache.

## Declaration

```swift
struct KVCacheStatus
```

## Overview

Obtain this through [`cacheStatus(parameters:)`](./languagemodel/cachestatus%28parameters%29.md), [`cacheStatus(parameters:)`](./modelcontainer/cachestatus%28parameters%29.md), or [`cacheStatus()`](./chatsession/cachestatus%28%29.md). The same value describes topology, capacity, strategy application, and model-wide progress for both legacy and typed configuration entry points.

## Topics

### Initializers
- [init(cache: [KVCache], configuration: KVCacheConfiguration?, phase: Phase, processedTokenCount: Int?)](./kvcachestatus/init%28cache,configuration,phase,processedtokencount%29.md)
  Inspect a raw cache array using a typed request.
### Instance Properties
- [var attentionMaxSizes: [Int?]](./kvcachestatus/attentionmaxsizes.md)
  Per-leaf attention token bounds (`nil` for unbounded or non-attention state).
- [let capacityAppliedLayerCount: Int](./kvcachestatus/capacityappliedlayercount.md)
- [let capacityDisposition: CapacityDisposition](./kvcachestatus/capacitydisposition-swift.property.md)
- [let capacityUnappliedLayerCount: Int](./kvcachestatus/capacityunappliedlayercount.md)
- [var compressedLayerCount: Int](./kvcachestatus/compressedlayercount.md)
- [var isHybrid: Bool](./kvcachestatus/ishybrid.md)
  `true` when the topology contains both attention and recurrent state.
- [let layers: [KVCacheLayerStatus]](./kvcachestatus/layers.md)
  Flattened leaf layers. [`path`](./kvcachelayerstatus/path.md) preserves composite topology.
- [var memoryBytes: Int](./kvcachestatus/memorybytes.md)
  Bytes allocated across all layers.
- [var pendingLayerCount: Int](./kvcachestatus/pendinglayercount.md)
- [let phase: Phase](./kvcachestatus/phase-swift.property.md)
- [let processedTokenCount: Int?](./kvcachestatus/processedtokencount.md)
  Authoritative model-wide position for realized session storage.
- [let requestSource: RequestSource?](./kvcachestatus/requestsource-swift.property.md)
- [let requestedConfiguration: KVCacheConfiguration?](./kvcachestatus/requestedconfiguration.md)
  `nil` when no capacity or compression behavior was requested.
- [var requestedStrategy: KVCacheStrategyIdentifier?](./kvcachestatus/requestedstrategy.md)
- [var skippedLayerCount: Int](./kvcachestatus/skippedlayercount.md)
### Enumerations
- [KVCacheStatus.CapacityDisposition](./kvcachestatus/capacitydisposition-swift.enum.md)
  Relationship between requested capacity and the attention layers to which that request applies.
- [KVCacheStatus.Phase](./kvcachestatus/phase-swift.enum.md)
- [KVCacheStatus.RequestSource](./kvcachestatus/requestsource-swift.enum.md)
### Default Implementations
- [Equatable Implementations](./kvcachestatus/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachestatus)*