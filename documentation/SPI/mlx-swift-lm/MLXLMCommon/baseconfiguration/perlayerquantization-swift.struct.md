---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baseconfiguration/perlayerquantization-swift.struct"
framework: "mlx-swift-lm/MLXLMCommon"
---

# BaseConfiguration.PerLayerQuantization

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

A container for per-layer [`BaseConfiguration.Quantization`](./quantization-swift.struct.md) settings.

## Declaration

```swift
struct PerLayerQuantization
```

## Overview

This allows for “Mixed-Precision” or “Heterogeneous” quantization, where sensitive layers (like the embedding head) can be kept at higher precision while the rest of the model is compressed.

## Topics

### Initializers
- [init(quantization: BaseConfiguration.Quantization?, perLayerQuantization: [String : BaseConfiguration.QuantizationOption])](./perlayerquantization-swift.struct/init%28quantization,perlayerquantization%29.md)
### Instance Properties
- [var perLayerQuantization: [String : QuantizationOption]](./perlayerquantization-swift.struct/perlayerquantization.md)
  A dictionary mapping layer paths (e.g., “model.embed_tokens”) to their quantization options.
- [var quantization: Quantization?](./perlayerquantization-swift.struct/quantization.md)
  The default quantization for any layer not explicitly named in `perLayerQuantization`.
### Instance Methods
- [func quantization(layer: String) -> Quantization?](./perlayerquantization-swift.struct/quantization%28layer%29.md)
  Resolves the quantization parameters for a specific layer.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baseconfiguration/perlayerquantization-swift.struct)*