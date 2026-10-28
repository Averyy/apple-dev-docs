---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/softshrink"
framework: "mlx-swift/MLXNN"
---

# Softshrink

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies the Softshrink activation function.

## Declaration

```swift
class Softshrink
```

## Overview

This is (element-wise):

```swift
if x > lambda {
    x - lambda
}  else if x < -lambda {
    x + lambda
} else {
    0
}
```

### See Also

- [Activation Functions and Layers](./activations.md)
- [`softshrink(_:lambda:)`](./softshrink%28_,lambda%29.md)

## Topics

### Initializers
- [init(lambda: Float)](./softshrink/init%28lambda%29.md)
### Instance Properties
- [var lambda: Float](./softshrink/lambda.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./softshrink/callasfunction%28_%29.md)

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
- [class ELU](./elu.md)
  Applies the Exponential Linear Unit.
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/softshrink)*