---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baseconfiguration/quantizationoption"
framework: "mlx-swift-lm/MLXLMCommon"
---

# BaseConfiguration.QuantizationOption

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

handling instructions for [`BaseConfiguration.PerLayerQuantization`](./perlayerquantization-swift.struct.md)

## Declaration

```swift
enum QuantizationOption
```

## Topics

### Enumeration Cases
- [BaseConfiguration.QuantizationOption.quantize(_:)](./quantizationoption/quantize%28_%29.md)
  Quantize this layer using the provided parameters.
- [BaseConfiguration.QuantizationOption.skip](./quantizationoption/skip.md)
  Do not quantize this specific layer (keep it in high precision).

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/baseconfiguration/quantizationoption)*