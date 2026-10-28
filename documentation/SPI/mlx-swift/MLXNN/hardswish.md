---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/hardswish"
framework: "mlx-swift/MLXNN"
---

# HardSwish

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies the hardswish function, element-wise

## Declaration

```swift
class HardSwish
```

## Overview

This is:

```swift
x * MLX.minimum(MLX.maximum(x + 3, 0), 6) / 6
```

### See Also

- [Activation Functions and Layers](./activations.md)
- [`hardSwish(_:)`](./hardswish%28_%29.md)

## Topics

### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./hardswish/callasfunction%28_%29.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/hardswish)*