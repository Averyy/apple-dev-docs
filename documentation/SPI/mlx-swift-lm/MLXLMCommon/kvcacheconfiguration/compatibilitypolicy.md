---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration/compatibilitypolicy"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheConfiguration.CompatibilityPolicy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Behavior when only part of a model’s cache topology supports the strategy.

## Declaration

```swift
enum CompatibilityPolicy
```

## Topics

### Enumeration Cases
- [KVCacheConfiguration.CompatibilityPolicy.allowPartial](./compatibilitypolicy/allowpartial.md)
  Apply the strategy where supported and retain other layers unchanged.
- [KVCacheConfiguration.CompatibilityPolicy.requireAllLayers](./compatibilitypolicy/requirealllayers.md)
  Reject the request unless every attention layer can use it.
- [KVCacheConfiguration.CompatibilityPolicy.requireAtLeastOneLayer](./compatibilitypolicy/requireatleastonelayer.md)
  Reject the request unless at least one attention layer can use it.
### Default Implementations
- [Equatable Implementations](./compatibilitypolicy/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration/compatibilitypolicy)*