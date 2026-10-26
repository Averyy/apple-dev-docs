---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionquantization"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionQuantization

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Quantization settings for one conversion pass or layer.

## Declaration

```swift
struct ModelConversionQuantization
```

## Topics

### Initializers
- [init(bits: Int?, groupSize: Int?, mode: QuantizationMode, calibration: ModelConversionQuantizationCalibration)](./modelconversionquantization/init%28bits,groupsize,mode,calibration%29.md)
### Instance Properties
- [var bits: Int?](./modelconversionquantization/bits.md)
  Quantization bit depth.
- [var calibration: ModelConversionQuantizationCalibration](./modelconversionquantization/calibration.md)
  How the quantization grid is derived. Defaults to [`ModelConversionQuantizationCalibration.standard`](./modelconversionquantizationcalibration/standard.md).
- [var groupSize: Int?](./modelconversionquantization/groupsize.md)
  Quantization group size.
- [var mode: QuantizationMode](./modelconversionquantization/mode.md)
  Quantization mode.
### Default Implementations
- [Equatable Implementations](./modelconversionquantization/equatable-implementations.md)

## Relationships

### Conforms To
- Swift.Equatable
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionquantization)*