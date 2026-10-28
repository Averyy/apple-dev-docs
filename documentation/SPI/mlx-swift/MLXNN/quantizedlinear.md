---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear"
framework: "mlx-swift/MLXNN"
---

# QuantizedLinear

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies an affine transformation to the input using a quantized weight matrix.

## Declaration

```swift
class QuantizedLinear
```

## Mentions

- [Creating Modules](./custom-layers.md)

## Overview

It is the quantized equivalent of [`Linear`](./linear.md).  For now its parameters are frozen and will not be included in any gradient computation but this will probably change in the future.

QuantizedLinear also provides several useful static to convert linear layers to QuantizedLinear layers.

- [`from(linear:groupSize:bits:)`](./quantizedlinear/from%28linear,groupsize,bits%29.md) – returns a `QuantizedLinear` that applies the same linear transformation up to the quantization error
- [`quantize(model:groupSize:bits:predicate:)`](./quantizedlinear/quantize%28model,groupsize,bits,predicate%29.md) – swaps all the linear layers of the module with `QuantizedLinear` ones

Please see the discussion in [`Linear`](./linear.md) for considerations when replacing layers.

### See Also

- [`init(_:_:bias:groupSize:bits:mode:)`](./quantizedlinear/init%28_,_,bias,groupsize,bits,mode%29.md)

## Topics

### Initializers
- [convenience init(Int, Int, bias: Bool, groupSize: Int, bits: Int, mode: QuantizationMode)](./quantizedlinear/init%28_,_,bias,groupsize,bits,mode%29.md)
  Applies an affine transformation to the input using a quantized weight matrix.
- [convenience init(Linear, groupSize: Int, bits: Int, mode: QuantizationMode)](./quantizedlinear/init%28_,groupsize,bits,mode%29.md)
  Initialize a QuantizedLinear layer that applies the same linear transformation up to the quantization error.
- [init(weight: MLXArray, bias: MLXArray?, groupSize: Int, bits: Int, mode: QuantizationMode, globalScale: MLXArray?)](./quantizedlinear/init%28weight,bias,groupsize,bits,mode,globalscale%29.md)
  Initialize a [`QuantizedLinear`](./quantizedlinear.md) with non-quantized weights and bias.
- [init(weight: MLXArray, bias: MLXArray?, scales: MLXArray, biases: MLXArray?, groupSize: Int, bits: Int, mode: QuantizationMode, globalScale: MLXArray?)](./quantizedlinear/init%28weight,bias,scales,biases,groupsize,bits,mode,globalscale%29.md)
  Initializer meant for subclasses to provide arrays directly.
### Instance Properties
- [let biases: MLXArray?](./quantizedlinear/biases.md)
- [let bits: Int](./quantizedlinear/bits.md)
- [var globalScale: MLXArray?](./quantizedlinear/globalscale.md)
- [let groupSize: Int](./quantizedlinear/groupsize.md)
- [let mode: QuantizationMode](./quantizedlinear/mode.md)
- [let scales: MLXArray](./quantizedlinear/scales.md)
- [var shape: (Int, Int)](./quantizedlinear/shape.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./quantizedlinear/callasfunction%28_%29.md)
- [func unfreeze(recursive: Bool, keys: [String]?, strict: Bool) throws](./quantizedlinear/unfreeze%28recursive,keys,strict%29.md)
  Unfreeze the `Module`’s parameters or subset.
### Type Methods
- [static func from(linear: Linear, groupSize: Int, bits: Int) -> QuantizedLinear](./quantizedlinear/from%28linear,groupsize,bits%29.md)
  Returns a QuantizedLinear layer that applies the same linear transformation up to the quantization error.
- [static func quantize(model: Module, groupSize: Int, bits: Int, predicate: (Linear) -> Bool)](./quantizedlinear/quantize%28model,groupsize,bits,predicate%29.md)
  Replace [`Linear`](./linear.md) layers with `QuantizedLinear`.

## Relationships

### Inherits From
- [Linear](./linear.md)
### Inherited By
- [QuantizedAllToShardedLinear](./quantizedalltoshardedlinear.md)
- [QuantizedShardedToAllLinear](./quantizedshardedtoalllinear.md)
### Conforms To
- MLX.Evaluatable
- MLX.IndentedDescription
- MLX.Updatable
- [Quantizable](./quantizable.md)
- [Quantized](./quantized.md)
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
- [class RoPE](./rope.md)
  Implements the rotary positional encoding.
- [class RMSNorm](./rmsnorm.md)
  Applies Root Mean Square normalization [1] to the inputs.
- [class Sequential](./sequential.md)
  A layer that calls the passed [`UnaryLayer`](./unarylayer.md) in order.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/quantizedlinear)*