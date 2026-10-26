---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/conv2d"
framework: "mlx-swift/MLXNN"
---

# Conv2d

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies a 2-dimensional convolution over the multi-channel input image.

## Declaration

```swift
class Conv2d
```

##### See Also

- [`Conv1d`](./conv1d.md)
- [`Conv3d`](./conv3d.md)
- [`init(inputChannels:outputChannels:kernelSize:stride:padding:dilation:groups:bias:)`](./conv2d/init%28inputchannels,outputchannels,kernelsize,stride,padding,dilation,groups,bias%29.md)

## Topics

### Initializers
- [init(inputChannels: Int, outputChannels: Int, kernelSize: IntOrPair, stride: IntOrPair, padding: IntOrPair, dilation: IntOrPair, groups: Int, bias: Bool)](./conv2d/init%28inputchannels,outputchannels,kernelsize,stride,padding,dilation,groups,bias%29.md)
  Applies a 2-dimensional convolution over the multi-channel input image.
### Instance Properties
- [let bias: MLXArray?](./conv2d/bias.md)
- [let dilation: (Int, Int)](./conv2d/dilation.md)
- [let groups: Int](./conv2d/groups.md)
- [let padding: (Int, Int)](./conv2d/padding.md)
- [let stride: (Int, Int)](./conv2d/stride.md)
- [let weight: MLXArray](./conv2d/weight.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./conv2d/callasfunction%28_%29.md)

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
- [class Sequential](./sequential.md)
  A layer that calls the passed [`UnaryLayer`](./unarylayer.md) in order.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/conv2d)*