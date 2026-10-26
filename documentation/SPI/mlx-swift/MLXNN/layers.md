---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/layers"
framework: "mlx-swift/MLXNN"
---

# Layers

**Framework**: mlx-swift/MLXNN  
**Role**: API Collection

Built-in layers.

#### Overview

`MLXNN` provides a number of built-in layers that can be used to build models.
See also [Activation Functions and Layers](./activations.md) for Activation Layers and [Creating Modules](./custom-layers.md) for examples of their use

## Topics

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
- [class ConvTransposed3d](./convtransposed3d.md)
  Applies a 3-dimensional transposed convolution over the multi-channel input image.
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
### Sampling
- [class Upsample](./upsample.md)
  Upsample the input signal spatially.
### Recurrent
- [class RNN](./rnn.md)
  An Elman recurrent layer.
- [class GRU](./gru.md)
  A gated recurrent unit (GRU) RNN layer.
- [class LSTM](./lstm.md)
  An LSTM recurrent layer.
### Other Layers
- [class Bilinear](./bilinear.md)
  Applies a bilinear transformation to the inputs.
- [class MultiHeadAttention](./multiheadattention.md)
  Implements the scaled dot product attention with multiple heads.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/layers)*