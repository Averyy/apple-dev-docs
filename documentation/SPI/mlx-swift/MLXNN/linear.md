---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/linear"
framework: "mlx-swift/MLXNN"
---

# Linear

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies an affine transformation to the input.

## Declaration

```swift
class Linear
```

## Mentions

- [Creating Modules](./custom-layers.md)

## Overview

Concretely:

```swift
matmul(x, W) + b
```

where `W` has shape `[inputDimensions, outputDimensions]` and `b` has shape `[outputDimensions]`.

The values are initialized from the uniform distribution:

```swift
scale = sqrt(1.0 / inputDimensions)
W = MLXRandom.uniform(-scale ..< scale, [outputDimensions, inputDimensions])
b = MLXRandom.uniform(-scale ..< scale, [outputDimensions])
```

## Using In A Module

> **Note**: Use `@ModuleInfo` with all your `Linear` module uses so that [`update(modules:verify:path:modulePath:)`](./module/update%28modules,verify,path,modulepath%29.md) can replace the modules, e.g. via [`quantize(model:groupSize:bits:predicate:)`](./quantizedlinear/quantize%28model,groupsize,bits,predicate%29.md).

For example:

```swift
public class FeedForward : Module {

    @ModuleInfo var w1: Linear
    @ModuleInfo var w2: Linear
    @ModuleInfo var w3: Linear

    public init(_ args: Configuration) {
        self.w1 = Linear(args.dimensions, args.hiddenDimensions, bias: false)
        self.w2 = Linear(args.hiddenDimensions, args.dimensions, bias: false)
        self.w3 = Linear(args.dimensions, args.hiddenDimensions, bias: false)
    }
```

If a `key` is needed (to change the parameters key for [`parameters()`](./module/parameters%28%29.md)) here is the way to initialize the ivar:

```swift
public class Example : Module {

    @ModuleInfo(key: "weights_1") var w1: Linear

    public init() {
        self._w1.wrappedValue = Linear(10, 20, bias: false)
    }
```

### See Also

- [Creating Modules](./custom-layers.md)
- [`QuantizedLinear`](./quantizedlinear.md)
- [`Bilinear`](./bilinear.md)

## Topics

### Initializers
- [init(Int, Int, bias: Bool)](./linear/init%28_,_,bias%29.md)
  Applies an affine transformation to the input.
- [convenience init(inputDimensions: Int, outputDimensions: Int, bias: Bool)](./linear/init%28inputdimensions,outputdimensions,bias%29.md)
  Convenience initializer giving parameter names.
- [init(weight: MLXArray, bias: MLXArray?)](./linear/init%28weight,bias%29.md)
  Initializer meant for subclasses to provide weight and bias arrays directly.
### Instance Properties
- [let bias: MLXArray?](./linear/bias.md)
- [var shape: (Int, Int)](./linear/shape.md)
- [let weight: MLXArray](./linear/weight.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./linear/callasfunction%28_%29.md)
- [func describeExtra(Int) -> String](./linear/describeextra%28_%29.md)
  Describe the `inputDimensions` and `outputDimensions`.
- [func toQuantized(groupSize: Int, bits: Int, mode: QuantizationMode) -> Module](./linear/toquantized%28groupsize,bits,mode%29.md)
  Return the module as a quantized representation
### Default Implementations
- [Quantizable Implementations](./linear/quantizable-implementations.md)

## Relationships

### Inherits From
- [Module](./module.md)
### Inherited By
- [AllToShardedLinear](./alltoshardedlinear.md)
- [QuantizedLinear](./quantizedlinear.md)
- [ShardedToAllLinear](./shardedtoalllinear.md)
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
- [class Embedding](./embedding.md)
  Implements a simple lookup table that maps each input integer to a high-dimensional vector.
- [class Identity](./identity.md)
  A placeholder identity operator that is argument-insensitive.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/linear)*