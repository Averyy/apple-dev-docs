---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcacheconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TurboQuantKVCacheConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

TurboQuant cache compression settings.

## Declaration

```swift
struct TurboQuantKVCacheConfiguration
```

## Topics

### Structures
- [TurboQuantKVCacheConfiguration.KeyPrecision](./turboquantkvcacheconfiguration/keyprecision-swift.struct.md)
  Opaque key encoding precision. Additional encodings can be introduced without adding public enum cases that clients must exhaustively handle.
- [TurboQuantKVCacheConfiguration.ValuePrecision](./turboquantkvcacheconfiguration/valueprecision-swift.struct.md)
  Opaque value encoding precision.
### Initializers
- [init(keyPrecision: KeyPrecision, valuePrecision: ValuePrecision, compressionStart: Int) throws](./turboquantkvcacheconfiguration/init%28keyprecision,valueprecision,compressionstart%29.md)
### Instance Properties
- [let compressionStart: Int](./turboquantkvcacheconfiguration/compressionstart.md)
- [let keyPrecision: KeyPrecision](./turboquantkvcacheconfiguration/keyprecision-swift.property.md)
- [let valuePrecision: ValuePrecision](./turboquantkvcacheconfiguration/valueprecision-swift.property.md)
### Type Properties
- [static let balanced: TurboQuantKVCacheConfiguration](./turboquantkvcacheconfiguration/balanced.md)
  Affine 8-bit keys and 3-bit values; the recommended general preset.
- [static let memoryFirst: TurboQuantKVCacheConfiguration](./turboquantkvcacheconfiguration/memoryfirst.md)
  Affine 8-bit keys and 2-bit values for memory-bound long contexts.
- [static let qualityFirst: TurboQuantKVCacheConfiguration](./turboquantkvcacheconfiguration/qualityfirst.md)
  FP16 keys and 4-bit values; the conservative quality-first preset.
### Default Implementations
- [Equatable Implementations](./turboquantkvcacheconfiguration/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcacheconfiguration)*