---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/dynamicntkalpharope"
framework: "mlx-swift-lm/MLXLMCommon"
---

# DynamicNTKAlphaRoPE

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

RoPE whose base is rescaled once by `alpha^(dim/(dim-2))` (Hunyuan’s static NTK scaling).

## Declaration

```swift
class DynamicNTKAlphaRoPE
```

## Topics

### Initializers
- [init(dimensions: Int, base: Float, scalingAlpha: Float, traditional: Bool)](./dynamicntkalpharope/init%28dimensions,base,scalingalpha,traditional%29.md)
### Instance Methods
- [func callAsFunction(MLXArray, offset: MLXArray) -> MLXArray](./dynamicntkalpharope/callasfunction%28_,offset%29-46ch.md)
- [func callAsFunction(MLXArray, offset: Int) -> MLXArray](./dynamicntkalpharope/callasfunction%28_,offset%29-4mv9o.md)

## Relationships

### Inherits From
- MLXNN.Module
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXNN.ArrayOffsetLayer
- MLXNN.OffsetLayer
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/dynamicntkalpharope)*