---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionquantizationcalibration"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionQuantizationCalibration

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

How the quantization grid is derived from the source weights.

## Declaration

```swift
enum ModelConversionQuantizationCalibration
```

#### Overview

This selects a *derivation*, not a storage format: every calibration produces ordinary quantized layers that load and run without any decode-side support.

## Topics

### Enumeration Cases
- [ModelConversionQuantizationCalibration.q4Zero](./modelconversionquantizationcalibration/q4zero.md)
  Reproduce the `Q4_0` grid: symmetric, 32-element groups, scaled by the signed element of largest magnitude.
- [ModelConversionQuantizationCalibration.standard](./modelconversionquantizationcalibration/standard.md)
  Derive the grid from the weights, as MLX does by default.
### Default Implementations
- [Equatable Implementations](./modelconversionquantizationcalibration/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Hashable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionquantizationcalibration)*