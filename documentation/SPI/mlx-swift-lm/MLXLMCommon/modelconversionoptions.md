---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionoptions"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionOptions

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: struct  
**Role**: Structure

Options controlling model conversion.

## Declaration

```swift
struct ModelConversionOptions
```

## Topics

### Initializers
- [init(bits: Int?, groupSize: Int?, mode: QuantizationMode, calibration: ModelConversionQuantizationCalibration, maxShardSize: Int64, overwriteExistingOutput: Bool, quantizationPredicate: ModelConversionQuantizationPredicate?)](./modelconversionoptions/init%28bits,groupsize,mode,calibration,maxshardsize,overwriteexistingoutput,quantizationpredicate%29.md)
### Instance Properties
- [var bits: Int?](./modelconversionoptions/bits.md)
- [var calibration: ModelConversionQuantizationCalibration](./modelconversionoptions/calibration.md)
- [var groupSize: Int?](./modelconversionoptions/groupsize.md)
- [var maxShardSize: Int64](./modelconversionoptions/maxshardsize.md)
  Maximum safetensors shard size in bytes.
- [var mode: QuantizationMode](./modelconversionoptions/mode.md)
- [var overwriteExistingOutput: Bool](./modelconversionoptions/overwriteexistingoutput.md)
  Remove and recreate the output directory if it already exists.
- [var quantization: ModelConversionQuantization](./modelconversionoptions/quantization.md)
  Default quantization settings.
- [var quantizationPredicate: ModelConversionQuantizationPredicate?](./modelconversionoptions/quantizationpredicate.md)
  Optional per-layer quantization customization.

## Relationships

### Conforms To
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionoptions)*