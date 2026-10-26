---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedswitchlinear"
framework: "mlx-swift-lm/MLXLMCommon"
---

# QuantizedSwitchLinear

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class QuantizedSwitchLinear
```

## Topics

### Initializers
- [init(SwitchLinear, groupSize: Int, bits: Int, mode: QuantizationMode)](./quantizedswitchlinear/init%28_,groupsize,bits,mode%29.md)
### Instance Properties
- [let bits: Int](./quantizedswitchlinear/bits.md)
- [let groupSize: Int](./quantizedswitchlinear/groupsize.md)
- [let mode: QuantizationMode](./quantizedswitchlinear/mode.md)
### Instance Methods
- [func callAsFunction(MLXArray, MLXArray, sortedIndices: Bool) -> MLXArray](./quantizedswitchlinear/callasfunction%28_,_,sortedindices%29.md)

## Relationships

### Inherits From
- [SwitchLinear](./switchlinear.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXNN.Quantizable
- MLXNN.Quantized
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/quantizedswitchlinear)*