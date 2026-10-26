---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baseconfiguration/quantization-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# BaseConfiguration.Quantization

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Configuration parameters for weight quantization.

## Declaration

```swift
struct Quantization
```

#### Overview

MLX uses group-wise quantization to reduce memory footprint. This struct defines how weights are grouped and the precision (bits) used for each group.

## Topics

### Initializers
- [init(from: any Decoder) throws](./quantization-swift.struct/init%28from%29.md)
- [init(groupSize: Int, bits: Int)](./quantization-swift.struct/init%28groupsize,bits%29.md)
  Initializes a new quantization configuration.
### Instance Properties
- [var asTuple: (Int, Int, QuantizationMode)](./quantization-swift.struct/astuple.md)
  Converts the configuration into a tuple format compatible with `MLX.quantize`.
- [let bits: Int](./quantization-swift.struct/bits.md)
  The number of bits per weight.
- [let groupSize: Int](./quantization-swift.struct/groupsize.md)
  The size of the quantization group.
- [var mode: QuantizationMode](./quantization-swift.struct/mode.md)
  The quantization method to use (defaults to `.affine`).
### Default Implementations
- [Encodable Implementations](./quantization-swift.struct/encodable-implementations.md)
- [Equatable Implementations](./quantization-swift.struct/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baseconfiguration/quantization-swift.struct)*