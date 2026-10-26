---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baseconfiguration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# BaseConfiguration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

The fundamental configuration for any MLX-based model.

## Declaration

```swift
struct BaseConfiguration
```

#### Overview

`BaseConfiguration` provides the metadata necessary to identify the model architecture (`modelType`) and describes the quantization parameters used to compress the model’s weights. It is designed to be decoded directly from a model repository’s `config.json`.

Typically used the [`GenericModelFactory`](./genericmodelfactory.md) implementations during load.

## Topics

### Structures
- [BaseConfiguration.PerLayerQuantization](./baseconfiguration/perlayerquantization-swift.struct.md)
  A container for per-layer [`BaseConfiguration.Quantization`](./baseconfiguration/quantization-swift.struct.md) settings.
- [BaseConfiguration.Quantization](./baseconfiguration/quantization-swift.struct.md)
  Configuration parameters for weight quantization.
### Initializers
- [init(from: any Decoder) throws](./baseconfiguration/init%28from%29.md)
### Instance Properties
- [var effectiveEOSTokenIds: Set<Int>](./baseconfiguration/effectiveeostokenids.md)
  EOS token IDs declared at either the model root or in `text_config`.
- [var eosTokenIds: IntOrIntArray?](./baseconfiguration/eostokenids.md)
  EOS token IDs from config.json. Can be a single Int or an array of Ints.
- [let modelType: String](./baseconfiguration/modeltype.md)
  The architecture identifier (e.g., “bert”, “roberta”, “xlm-roberta”).
- [var perLayerQuantization: PerLayerQuantization?](./baseconfiguration/perlayerquantization-swift.property.md)
  The per-layer quantization settings, including the default fallback.
- [var quantization: Quantization?](./baseconfiguration/quantization-swift.property.md)
  The default quantization settings.
### Enumerations
- [BaseConfiguration.QuantizationOption](./baseconfiguration/quantizationoption.md)
  handling instructions for [`BaseConfiguration.PerLayerQuantization`](./baseconfiguration/perlayerquantization-swift.struct.md)
### Default Implementations
- [Encodable Implementations](./baseconfiguration/encodable-implementations.md)

## Relationships

### Conforms To
- Swift.Decodable
- Swift.Encodable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baseconfiguration)*