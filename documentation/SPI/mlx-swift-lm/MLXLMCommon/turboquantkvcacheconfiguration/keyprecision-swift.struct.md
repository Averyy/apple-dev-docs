---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcacheconfiguration/keyprecision-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# TurboQuantKVCacheConfiguration.KeyPrecision

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Opaque key encoding precision. Additional encodings can be introduced without adding public enum cases that clients must exhaustively handle.

## Declaration

```swift
struct KeyPrecision
```

## Topics

### Type Properties
- [static let affineEightBit: TurboQuantKVCacheConfiguration.KeyPrecision](./keyprecision-swift.struct/affineeightbit.md)
  Affine 8-bit keys with TurboQuant-compressed values.
- [static let fourBit: TurboQuantKVCacheConfiguration.KeyPrecision](./keyprecision-swift.struct/fourbit.md)
- [static let fp16: TurboQuantKVCacheConfiguration.KeyPrecision](./keyprecision-swift.struct/fp16.md)
  Keep keys in FP16; only values are compressed.
- [static let threeBit: TurboQuantKVCacheConfiguration.KeyPrecision](./keyprecision-swift.struct/threebit.md)
- [static let twoBit: TurboQuantKVCacheConfiguration.KeyPrecision](./keyprecision-swift.struct/twobit.md)
  TurboQuant-compressed keys.
### Default Implementations
- [Equatable Implementations](./keyprecision-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/turboquantkvcacheconfiguration/keyprecision-swift.struct)*