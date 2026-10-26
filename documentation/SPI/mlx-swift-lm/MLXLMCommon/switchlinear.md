---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/switchlinear"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SwitchLinear

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

## Declaration

```swift
class SwitchLinear
```

## Topics

### Initializers
- [init(inputDims: Int, outputDims: Int, numExperts: Int, bias: Bool)](./switchlinear/init%28inputdims,outputdims,numexperts,bias%29.md)
- [init(inputDims: Int, outputDims: Int, numExperts: Int, weight: MLXArray, bias: MLXArray?)](./switchlinear/init%28inputdims,outputdims,numexperts,weight,bias%29.md)
  Initializer meant for subclasses to provide weight and bias arrays directly.
### Instance Methods
- [func callAsFunction(MLXArray, MLXArray, sortedIndices: Bool) -> MLXArray](./switchlinear/callasfunction%28_,_,sortedindices%29.md)
- [func toQuantized(groupSize: Int, bits: Int, mode: QuantizationMode) -> Module](./switchlinear/toquantized%28groupsize,bits,mode%29.md)
### Default Implementations
- [Quantizable Implementations](./switchlinear/quantizable-implementations.md)

## Relationships

### Inherits From
- MLXNN.Module
### Inherited By
- [QuantizedSwitchLinear](./quantizedswitchlinear.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXNN.Quantizable
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/switchlinear)*