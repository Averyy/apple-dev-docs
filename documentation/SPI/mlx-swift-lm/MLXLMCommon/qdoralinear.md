---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qdoralinear"
framework: "mlx-swift-lm/MLXLMCommon"
---

# QDoRALinear

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Implementation of DoRA `QuantizedLinear` replacement layer.

## Declaration

```swift
class QDoRALinear
```

#### Overview

See [`DoRALinear`](./doralinear.md) (equivalent class for `Linear` layers) for more information.

##### See Also

- [`DoRALinear`](./doralinear.md)

## Topics

### Initializers
- [init(linear: QuantizedLinear, rank: Int, scale: Float)](./qdoralinear/init%28linear,rank,scale%29.md)
- [init(linear: QuantizedLinear, rank: Int, scale: Float, dropout: Float)](./qdoralinear/init%28linear,rank,scale,dropout%29.md)
### Instance Properties
- [var loraEnabled: Bool](./qdoralinear/loraenabled.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./qdoralinear/callasfunction%28_%29.md)
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./qdoralinear/freeze%28recursive,keys,strict%29.md)
- [func fused() -> Module](./qdoralinear/fused%28%29.md)
### Default Implementations
- [LoRALayer Implementations](./qdoralinear/loralayer-implementations.md)

## Relationships

### Inherits From
- MLXNN.QuantizedLinear
### Conforms To
- [LoRALayer](./loralayer.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXNN.Quantizable
- MLXNN.Quantized
- MLXNN.UnaryLayer
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qdoralinear)*