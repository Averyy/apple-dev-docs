---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loralinear"
framework: "mlx-swift-lm/MLXLMCommon"
---

# LoRALinear

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Implementation of LoRA `Linear` replacement layer.

## Declaration

```swift
class LoRALinear
```

#### Overview

This layer implements the LoRA capabilities for `Linear` layers, specifically:

- converting `Linear` or `QuantizedLinear` layers to [`LoRALinear`](./loralinear.md) / [`QLoRALinear`](./qloralinear.md)
- converting [`LoRALinear`](./loralinear.md) back to `Linear` or `QuantizedLinear` via [`fused()`](./loralinear/fused%28%29.md)
- implementing the LoRA evaluation
- applying optional dropout to the LoRA branch during training

[`QLoRALinear`](./qloralinear.md) is the equivalent class for `QuantizedLinear`.

This is not typically used directly – `LoRATrain.convert(model:layers:)` is used to add the adapter layers to a given model.

##### See Also

- [LoRA: Low-Rank Adaptation of Large Language Models](https://arxiv.org/abs/2106.09685)
- [QLoRA: Efficient Finetuning of Quantized LLMs](https://arxiv.org/abs/2305.14314)
- [`QLoRALinear`](./qloralinear.md)

## Topics

### Initializers
- [init(Int, Int, rank: Int, bias: Bool, scale: Float, dropout: Float, linear: Linear)](./loralinear/init%28_,_,rank,bias,scale,dropout,linear%29.md)
- [init(Int, Int, rank: Int, bias: Bool, scale: Float, linear: Linear)](./loralinear/init%28_,_,rank,bias,scale,linear%29.md)
### Instance Properties
- [var loraEnabled: Bool](./loralinear/loraenabled.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./loralinear/callasfunction%28_%29.md)
- [func freeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./loralinear/freeze%28recursive,keys,strict%29.md)
  Freeze all parameters except the lora parameters
- [func fused() -> Module](./loralinear/fused%28%29.md)
  Convert back into a fused `Linear` layer.
### Type Methods
- [static func from(linear: Linear, rank: Int, scale: Float, dropout: Float) -> LoRALayer](./loralinear/from%28linear,rank,scale,dropout%29.md)
  Convert a `Linear` or `QuantizedLinear` layer into a new `Linear` layer that implements the `LoRA` adapter.
### Default Implementations
- [LoRALayer Implementations](./loralinear/loralayer-implementations.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/loralinear)*