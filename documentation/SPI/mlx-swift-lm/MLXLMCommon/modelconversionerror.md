---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionerror"
framework: "mlx-swift-lm/MLXLMCommon"
---

# ModelConversionError

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: enum  
**Role**: Enumeration

Errors thrown by model conversion helpers.

## Declaration

```swift
enum ModelConversionError
```

## Topics

### Enumeration Cases
- [case incompatibleCalibration(ModelConversionQuantizationCalibration, ModelConversionQuantization)](./modelconversionerror/incompatiblecalibration%28_,_%29.md)
- [ModelConversionError.invalidShardSize(_:)](./modelconversionerror/invalidshardsize%28_%29.md)
- [ModelConversionError.noSafetensorsFiles(_:)](./modelconversionerror/nosafetensorsfiles%28_%29.md)
- [ModelConversionError.outputDirectoryExists(_:)](./modelconversionerror/outputdirectoryexists%28_%29.md)
- [ModelConversionError.outputDirectoryMatchesSource(_:)](./modelconversionerror/outputdirectorymatchessource%28_%29.md)
- [ModelConversionError.sourceAlreadyQuantized(_:)](./modelconversionerror/sourcealreadyquantized%28_%29.md)
- [ModelConversionError.unsupportedPyTorchWeights(_:)](./modelconversionerror/unsupportedpytorchweights%28_%29.md)
### Instance Properties
- [var errorDescription: String?](./modelconversionerror/errordescription.md)
### Default Implementations
- [Equatable Implementations](./modelconversionerror/equatable-implementations.md)
- [Error Implementations](./modelconversionerror/error-implementations.md)
- [LocalizedError Implementations](./modelconversionerror/localizederror-implementations.md)

## Relationships

### Conforms To
- Foundation.LocalizedError
- Swift.Equatable
- Swift.Error
- Swift.Sendable
- Swift.SendableMetatype


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/modelconversionerror)*