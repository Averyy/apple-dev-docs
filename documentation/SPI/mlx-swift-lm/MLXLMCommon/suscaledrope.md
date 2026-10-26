---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/suscaledrope"
framework: "mlx-swift-lm/MLXLMCommon"
---

# SuScaledRoPE

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Su Scaled Rotary Position Embedding.

## Declaration

```swift
class SuScaledRoPE
```

## Topics

### Initializers
- [init(dimensions: Int, base: Float, maxPositionEmbeddings: Int, originalMaxPositionEmbeddings: Int, shortFactor: [Float], longFactor: [Float], shortMScale: Float?, longMScale: Float?)](./suscaledrope/init%28dimensions,base,maxpositionembeddings,originalmaxpositionembeddings,shortfactor,longfactor,shortmscale,longmscale%29.md)
### Instance Methods
- [func callAsFunction(MLXArray, offset: Int) -> MLXArray](./suscaledrope/callasfunction%28_,offset%29-1cmxe.md)
- [func callAsFunction(MLXArray, offset: MLXArray) -> MLXArray](./suscaledrope/callasfunction%28_,offset%29-20j2m.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/suscaledrope)*