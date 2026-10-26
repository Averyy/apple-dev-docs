---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qloralinear"
framework: "mlx-swift-lm/MLXLMCommon"
---

# QLoRALinear

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Implementation of LoRA `QuantizedLinear` replacement layer.

## Declaration

```swift
class QLoRALinear
```

#### Overview

See [`LoRALinear`](./loralinear.md) (equivalent class for `Linear` layers) for more information.

## Topics

### Initializers
- [init(Int, Int, rank: Int, bias: Bool, scale: Float, dropout: Float, linear: QuantizedLinear)](./qloralinear/init%28_,_,rank,bias,scale,dropout,linear%29.md)
- [init(Int, Int, rank: Int, bias: Bool, scale: Float, linear: QuantizedLinear)](./qloralinear/init%28_,_,rank,bias,scale,linear%29.md)
### Instance Properties
- [var loraEnabled: Bool](./qloralinear/loraenabled.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./qloralinear/callasfunction%28_%29.md)
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./qloralinear/freeze%28recursive,keys,strict%29.md)
  Freeze all parameters except the lora parameters
- [func fused() -> Module](./qloralinear/fused%28%29.md)
  Convert back into a fused `QuantizedLinear` layer.
### Type Methods
- [static func from(linear: QuantizedLinear, rank: Int, scale: Float, dropout: Float) -> LoRALayer](./qloralinear/from%28linear,rank,scale,dropout%29.md)
  Convert a `QuantizedLinear` layer into a new `Linear` layer that implements the `LoRA` adapter.
### Default Implementations
- [LoRALayer Implementations](./qloralinear/loralayer-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/qloralinear)*