---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rope"
framework: "mlx-swift/MLXNN"
---

# RoPE

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Implements the rotary positional encoding.

## Declaration

```swift
final class RoPE
```

## Overview

The traditional implementation rotates consecutive pairs of elements in the feature dimension while the default implementation rotates pairs with stride half the feature dimensions for efficiency.

For more details see *RoFormer: Enhanced Transformer with Rotary Position Embedding* ([https://arxiv.org/abs/2104.09864](https://arxiv.org/abs/2104.09864))

### See Also

- [Positional Encoding](./positional-encoding.md)

## Topics

### Initializers
- [init(dimensions: Int, traditional: Bool, base: Float, scale: Float)](./rope/init%28dimensions,traditional,base,scale%29.md)
  Initialize [`RoPE`](./rope.md).
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./rope/callasfunction%28_%29.md)
  Evaluate with `offset` of `0`.
- [func callAsFunction(MLXArray, offset: MLXArray) -> MLXArray](./rope/callasfunction%28_,offset%29-1d45j.md)
  Evaluate with array offset for batched inference with different positions per sequence.
- [func callAsFunction(MLXArray, offset: Int) -> MLXArray](./rope/callasfunction%28_,offset%29-2ab0h.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforms To
- [ArrayOffsetLayer](./arrayoffsetlayer.md)
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- [OffsetLayer](./offsetlayer.md)
- Swift.CustomStringConvertible
- [UnaryLayer](./unarylayer.md)

## See Also

### Unary Layers
- [class AvgPool1d](./avgpool1d.md)
  Applies 1-dimensional average pooling.
- [class AvgPool2d](./avgpool2d.md)
  Applies 2-dimensional average pooling.
- [class Conv1d](./conv1d.md)
  Applies a 1-dimensional convolution over the multi-channel input sequence.
- [class Conv2d](./conv2d.md)
  Applies a 2-dimensional convolution over the multi-channel input image.
- [class Dropout](./dropout.md)
  Randomly zero a portion of the elements during training.
- [class Dropout2d](./dropout2d.md)
  Apply 2D channel-wise dropout during training.
- [class Dropout3d](./dropout3d.md)
  Apply 3D channel-wise dropout during training.
- [class Embedding](./embedding.md)
  Implements a simple lookup table that maps each input integer to a high-dimensional vector.
- [class Identity](./identity.md)
  A placeholder identity operator that is argument-insensitive.
- [class Linear](./linear.md)
  Applies an affine transformation to the input.
- [class MaxPool1d](./maxpool1d.md)
  Applies 1-dimensional max pooling.
- [class MaxPool2d](./maxpool2d.md)
  Applies 2-dimensional max pooling.
- [class QuantizedLinear](./quantizedlinear.md)
  Applies an affine transformation to the input using a quantized weight matrix.
- [class RMSNorm](./rmsnorm.md)
  Applies Root Mean Square normalization [1] to the inputs.
- [class Sequential](./sequential.md)
  A layer that calls the passed [`UnaryLayer`](./unarylayer.md) in order.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/rope)*