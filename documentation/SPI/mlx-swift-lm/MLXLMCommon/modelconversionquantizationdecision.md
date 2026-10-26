---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionquantizationdecision"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionQuantizationDecision

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Per-layer quantization decision.

## Declaration

```swift
enum ModelConversionQuantizationDecision
```

## Topics

### Enumeration Cases
- [ModelConversionQuantizationDecision.quantize(_:)](./modelconversionquantizationdecision/quantize%28_%29.md)
  Quantize this layer, using the global conversion settings when the associated value is nil.
- [ModelConversionQuantizationDecision.skip](./modelconversionquantizationdecision/skip.md)
  Do not quantize this layer.
### Default Implementations
- [Equatable Implementations](./modelconversionquantizationdecision/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionquantizationdecision)*