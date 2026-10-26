---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/dropout"
framework: "mlx-swift/MLXNN"
---

# Dropout

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Randomly zero a portion of the elements during training.

## Declaration

```swift
class Dropout
```

#### Overview

The remaining elements are multiplied with `1 / (1-p)` where `p` is the probability of zeroing an element. This is done so the expected value of a given element will remain the same.

##### See Also

- [`Dropout2d`](./dropout2d.md)
- [`Dropout3d`](./dropout3d.md)

## Topics

### Initializers
- [init(p: Float)](./dropout/init%28p%29.md)
### Instance Properties
- [let p1: Float](./dropout/p1.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./dropout/callasfunction%28_%29.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
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
- [class RoPE](./rope.md)
  Implements the rotary positional encoding.
- [class RMSNorm](./rmsnorm.md)
  Applies Root Mean Square normalization [1] to the inputs.
- [class Sequential](./sequential.md)
  A layer that calls the passed [`UnaryLayer`](./unarylayer.md) in order.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/dropout)*