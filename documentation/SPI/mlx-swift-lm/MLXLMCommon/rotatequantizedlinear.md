---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatequantizedlinear"
framework: "mlx-swift-lm/MLXLMCommon"
---

# RotateQuantizedLinear

**Framework**: mlx-swift-lm/MLXLMCommon  
**Kind**: class  
**Role**: Class

Pairwise Givens rotation + quantized matmul.

## Declaration

```swift
class RotateQuantizedLinear
```

## Overview

Subclasses `QuantizedLinear` so it can replace `Linear` in `@ModuleInfo` slots via `update(modules:)`. Only overrides `callAsFunction` to insert the rotation step before the standard quantized matmul.

Rotation is applied to activations at runtime via a Metal kernel, preserving the quantization-friendly properties of the original weights.

## Topics

### Initializers
- [init(inputDims: Int, outputDims: Int, hasBias: Bool, groupSize: Int, bits: Int, krot: Int)](./rotatequantizedlinear/init%28inputdims,outputdims,hasbias,groupsize,bits,krot%29.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./rotatequantizedlinear/callasfunction%28_%29.md)
  Forward pass: applies pairwise Givens rotation then quantized matmul.
- [func prepareDerivedRotationState() -> [MLXArray]](./rotatequantizedlinear/preparederivedrotationstate%28%29.md)
  See `RotationStatePreparing` — loader-owned, results batched into a single load-time `eval` with every other rotation module’s.

## Relationships

### Inherits From
- MLXNN.QuantizedLinear
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- MLXNN.Quantizable
- MLXNN.Quantized
- MLXNN.UnaryLayer
- Swift.CustomStringConvertible


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift-lm/main/documentation/mlxlmcommon/rotatequantizedlinear)*