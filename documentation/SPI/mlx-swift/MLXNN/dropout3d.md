---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/dropout3d"
framework: "mlx-swift/MLXNN"
---

# Dropout3d

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Apply 3D channel-wise dropout during training.

## Declaration

```swift
class Dropout3d
```

#### Overview

Randomly zero out entire channels independently with probability `p`. This layer expects the channels to be last, i.e., the input shape should be `NDHWC` or `DHWC` where: `N` is the batch dimension, `D` is the depth, `H` is the input image height, `W` is the input image width, and `C` is the number of input channels.

The remaining channels are scaled by `1 / (1-p)` to maintain the expected value of each element. Unlike traditional dropout, which zeros individual entries, this layer zeros entire channels. This is often beneficial for convolutional layers processing 3D data, like in medical imaging or video processing.

##### See Also

- [`Dropout`](./dropout.md)
- [`Dropout2d`](./dropout2d.md)

## Topics

### Initializers
- [init(p: Float)](./dropout3d/init%28p%29.md)
### Instance Properties
- [let p1: Float](./dropout3d/p1.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./dropout3d/callasfunction%28_%29.md)

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
- [class Dropout](./dropout.md)
  Randomly zero a portion of the elements during training.
- [class Dropout2d](./dropout2d.md)
  Apply 2D channel-wise dropout during training.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/dropout3d)*