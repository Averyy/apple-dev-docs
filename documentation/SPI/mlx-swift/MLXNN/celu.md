---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/celu"
framework: "mlx-swift/MLXNN"
---

# CELU

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies the Continuously Differentiable Exponential Linear Unit.

## Declaration

```swift
class CELU
```

## Overview

This is:

```swift
MLX.maximum(x, 0.0) + alpha * (MLX.exp(MLX.minimum(x, 0.0) / alpha) - 1)
```

### See Also

- [Activation Functions and Layers](./activations.md)
- [`celu(_:alpha:)`](./celu%28_,alpha%29.md)

## Topics

### Initializers
- [init(alpha: Float)](./celu/init%28alpha%29.md)
### Instance Properties
- [var alpha: Float](./celu/alpha.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./celu/callasfunction%28_%29.md)

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

### Activation Modules
- [class GELU](./gelu.md)
  Applies the Gaussian Error Linear Units function.
- [class GLU](./glu.md)
  Applies the gated linear unit function.
- [class HardSwish](./hardswish.md)
  Applies the hardswish function, element-wise
- [class LeakyReLU](./leakyrelu.md)
  Applies the Leaky Rectified Linear Unit.
- [class LogSigmoid](./logsigmoid.md)
  Applies the Log Sigmoid function.
- [class LogSoftmax](./logsoftmax.md)
  Applies the Log Softmax function.
- [class Mish](./mish.md)
  Applies the Mish function, element-wise.
- [class PReLU](./prelu.md)
  Applies the element-wise parametric ReLU.
- [class ReLU](./relu.md)
  Applies the Rectified Linear Unit.
- [class ReLU6](./relu6.md)
  Applies the Rectified Linear Unit 6.
- [class ReLUSquared](./relusquared.md)
  Applies the squared Rectified Linear Unit.
- [class SELU](./selu.md)
  Applies the Scaled Exponential Linear Unit.
- [class SiLU](./silu.md)
  Applies the Sigmoid Linear Unit. Also known as Swish.
- [class Sigmoid](./sigmoid.md)
  Applies the element-wise logistic sigmoid.
- [class Softmax](./softmax.md)
  Applies the Softmax function.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/celu)*