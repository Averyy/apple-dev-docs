---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/convtransposed3d"
framework: "mlx-swift/MLXNN"
---

# ConvTransposed3d

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies a 3-dimensional transposed convolution over the multi-channel input image.

## Declaration

```swift
class ConvTransposed3d
```

##### See Also

- [`ConvTransposed1d`](./convtransposed1d.md)
- [`ConvTransposed2d`](./convtransposed2d.md)
- [`init(inputChannels:outputChannels:kernelSize:stride:padding:outputPadding:dilation:groups:bias:)`](./convtransposed3d/init%28inputchannels,outputchannels,kernelsize,stride,padding,outputpadding,dilation,groups,bias%29.md)

## Topics

### Initializers
- [init(inputChannels: Int, outputChannels: Int, kernelSize: IntOrTriple, stride: IntOrTriple, padding: IntOrTriple, outputPadding: IntOrTriple, dilation: IntOrTriple, groups: Int, bias: Bool)](./convtransposed3d/init%28inputchannels,outputchannels,kernelsize,stride,padding,outputpadding,dilation,groups,bias%29.md)
  Applies a 3-dimensional transposed convolution over the multi-channel input image.
### Instance Properties
- [let bias: MLXArray?](./convtransposed3d/bias.md)
- [let dilation: (Int, Int, Int)](./convtransposed3d/dilation.md)
- [let groups: Int](./convtransposed3d/groups.md)
- [let outputPadding: (Int, Int, Int)](./convtransposed3d/outputpadding.md)
- [let padding: (Int, Int, Int)](./convtransposed3d/padding.md)
- [let stride: (Int, Int, Int)](./convtransposed3d/stride.md)
- [let weight: MLXArray](./convtransposed3d/weight.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./convtransposed3d/callasfunction%28_%29.md)

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
- [class Conv3d](./conv3d.md)
  Applies a 3-dimensional convolution over the multi-channel input image.
- [class ConvTransposed1d](./convtransposed1d.md)
  Applies a 1-dimensional transposed convolution over the multi-channel input sequence.
- [class ConvTransposed2d](./convtransposed2d.md)
  Applies a 2-dimensional transposed convolution over the multi-channel input image.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/convtransposed3d)*