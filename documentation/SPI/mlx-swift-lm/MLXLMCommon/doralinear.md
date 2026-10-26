---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/doralinear"
framework: "mlx-swift-lm/MLXLMCommon"
---

# DoRALinear

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Implementation of DoRA `Linear` replacement layer.

## Declaration

```swift
class DoRALinear
```

#### Overview

This layer implements DoRA (Weight-Decomposed Low-Rank Adaptation) for `Linear` layers.

[`QDoRALinear`](./qdoralinear.md) is the equivalent class for `QuantizedLinear`.

## Topics

### Initializers
- [init(linear: Linear, rank: Int, scale: Float)](./doralinear/init%28linear,rank,scale%29.md)
- [init(linear: Linear, rank: Int, scale: Float, dropout: Float)](./doralinear/init%28linear,rank,scale,dropout%29.md)
### Instance Properties
- [var loraEnabled: Bool](./doralinear/loraenabled.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./doralinear/callasfunction%28_%29.md)
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./doralinear/freeze%28recursive,keys,strict%29.md)
- [func fused() -> Module](./doralinear/fused%28%29.md)
### Type Methods
- [static func from(linear: Linear, rank: Int, scale: Float, dropout: Float) -> LoRALayer](./doralinear/from%28linear,rank,scale,dropout%29.md)
### Default Implementations
- [LoRALayer Implementations](./doralinear/loralayer-implementations.md)

## Relationships

### Inherits From
- MLXNN.Linear
### Conforms To
- [LoRALayer](./loralayer.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXNN.Quantizable
- MLXNN.UnaryLayer
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/doralinear)*