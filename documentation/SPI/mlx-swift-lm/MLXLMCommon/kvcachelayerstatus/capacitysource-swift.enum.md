---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachelayerstatus/capacitysource-swift.enum"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheLayerStatus.CapacitySource

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Where an attention layer’s resident-token bound originated.

## Declaration

```swift
enum CapacitySource
```

## Topics

### Enumeration Cases
- [KVCacheLayerStatus.CapacitySource.implementationDefined](./capacitysource-swift.enum/implementationdefined.md)
  A model-specific cache implementation defines the bound.
- [KVCacheLayerStatus.CapacitySource.modelDefined](./capacitysource-swift.enum/modeldefined.md)
  The model architecture defines the bound, such as sliding-window attention.
- [KVCacheLayerStatus.CapacitySource.requested](./capacitysource-swift.enum/requested.md)
  The caller requested the bound through generation parameters.
- [KVCacheLayerStatus.CapacitySource.unbounded](./capacitysource-swift.enum/unbounded.md)
  The attention cache grows without an explicit resident-token bound.
### Default Implementations
- [Equatable Implementations](./capacitysource-swift.enum/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcachelayerstatus/capacitysource-swift.enum)*