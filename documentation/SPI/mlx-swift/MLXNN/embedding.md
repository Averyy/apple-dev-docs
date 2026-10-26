---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/embedding"
framework: "mlx-swift/MLXNN"
---

# Embedding

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Implements a simple lookup table that maps each input integer to a high-dimensional vector.

## Declaration

```swift
class Embedding
```

#### Overview

Typically used to embed discrete tokens for processing by neural networks.

## Topics

### Initializers
- [init(embeddingCount: Int, dimensions: Int)](./embedding/init%28embeddingcount,dimensions%29.md)
  Implements a simple lookup table that maps each input integer to a high-dimensional vector.
- [init(weight: MLXArray)](./embedding/init%28weight%29.md)
  Initializer meant for subclasses to provide weight directly.
### Instance Properties
- [var shape: (Int, Int)](./embedding/shape.md)
- [let weight: MLXArray](./embedding/weight.md)
### Instance Methods
- [func asLinear(MLXArray) -> MLXArray](./embedding/aslinear%28_%29.md)
  Call the embedding layer as a linear layer.
- [func callAsFunction(MLXArray) -> MLXArray](./embedding/callasfunction%28_%29.md)
- [func describeExtra(Int) -> String](./embedding/describeextra%28_%29.md)
  Describe the shape of the `weight`.
- [func toQuantized(groupSize: Int, bits: Int, mode: QuantizationMode) -> Module](./embedding/toquantized%28groupsize,bits,mode%29.md)
  Return the module as a quantized representation
### Default Implementations
- [Quantizable Implementations](./embedding/quantizable-implementations.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Inherited By
- [QuantizedEmbedding](./quantizedembedding.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- [Quantizable](./quantizable.md)
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/embedding)*