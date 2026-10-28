---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sequential"
framework: "mlx-swift/MLXNN"
---

# Sequential

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

A layer that calls the passed [`UnaryLayer`](./unarylayer.md) in order.

## Declaration

```swift
class Sequential
```

## Overview

`Sequential` can be constructed either with an array of layers or using a [`SequentialBuilder`](./sequentialbuilder.md):

```swift
// a nonsensical Sequential layer, but it demonstrates how
// to constructuct something with an interesting structure
let b = Bool.random()
let s = Sequential {
    Tanh()
    if b {
        Tanh()
    } else {
        Sigmoid()
    }
    for _ in 0 ..< 3 {
        Linear(10, 20)
    }
}
```

produces:

```swift
Sequential {
  layers: [
    Tanh,
    Sigmoid,
    Linear(inputDimensions=10, outputDimensions=20, bias=true),
    Linear(inputDimensions=10, outputDimensions=20, bias=true),
    Linear(inputDimensions=10, outputDimensions=20, bias=true)
  ],
}
```

## Topics

### Initializers
- [init(layers: any UnaryLayer...)](./sequential/init%28layers%29-2rde0.md)
- [init(layers: [any UnaryLayer])](./sequential/init%28layers%29-3zdqn.md)
- [init(layers: () -> [any UnaryLayer])](./sequential/init%28layers%29-43yu.md)
  A convenient way to write code that builds a Sequential layer:
### Instance Properties
- [var layers: [any UnaryLayer]](./sequential/layers.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./sequential/callasfunction%28_%29.md)

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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/sequential)*