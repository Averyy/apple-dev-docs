---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration/strategy-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# KVCacheConfiguration.Strategy

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Opaque cache strategy. New strategies can be added without introducing public enum cases that clients must exhaustively switch over.

## Declaration

```swift
struct Strategy
```

## Topics

### Instance Properties
- [var identifier: KVCacheStrategyIdentifier](./strategy-swift.struct/identifier.md)
  Stable algorithm identity for diagnostics and persistence adapters.
### Type Properties
- [static let fullPrecision: KVCacheConfiguration.Strategy](./strategy-swift.struct/fullprecision.md)
### Type Methods
- [static func affine(AffineKVCacheConfiguration) -> Strategy](./strategy-swift.struct/affine%28_%29.md)
- [static func turboQuant(TurboQuantKVCacheConfiguration) -> Strategy](./strategy-swift.struct/turboquant%28_%29.md)
- [static func varianceNormalized(VarianceNormalizedKVCacheConfiguration) -> Strategy](./strategy-swift.struct/variancenormalized%28_%29.md)
### Default Implementations
- [Equatable Implementations](./strategy-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/kvcacheconfiguration/strategy-swift.struct)*