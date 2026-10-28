---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/elu"
framework: "mlx-swift/MLXNN"
---

# ELU

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies the Exponential Linear Unit.

## Declaration

```swift
class ELU
```

## Overview

This is:

```swift
MLX.which(x .> 0, x, alpha * (exp(x) - 1))
```

### See Also

- [Activation Functions and Layers](./activations.md)
- [`elu(_:alpha:)`](./elu%28_,alpha%29.md)

## Topics

### Initializers
- [init(alpha: Float)](./elu/init%28alpha%29.md)
### Instance Properties
- [var alpha: Float](./elu/alpha.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./elu/callasfunction%28_%29.md)

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
- [class CELU](./celu.md)
  Applies the Continuously Differentiable Exponential Linear Unit.
- [class GELU](./gelu.md)
  Applies the Gaussian Error Linear Units function.
- [class GLU](./glu.md)
  Applies the gated linear unit function.
- [class HardShrink](./hardshrink.md)
  Applies the HardShrink activation function.
- [class HardSwish](./hardswish.md)
  Applies the hardswish function, element-wise
- [class HardTanh](./hardtanh.md)
  Applies the HardTanh function.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/elu)*