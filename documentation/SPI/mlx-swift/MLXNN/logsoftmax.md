---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/logsoftmax"
framework: "mlx-swift/MLXNN"
---

# LogSoftmax

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies the Log Softmax function.

## Declaration

```swift
class LogSoftmax
```

#### Overview

This is:

```swift
x - MLX.logSumExp(x, axis: axis, keepDims: true)
```

##### See Also

- [Activation Functions and Layers](./activations.md)
- [`logSoftmax(_:axis:)`](./logsoftmax%28_,axis%29.md)

## Topics

### Initializers
- [init(axis: Int)](./logsoftmax/init%28axis%29.md)
### Instance Properties
- [var axis: Int](./logsoftmax/axis.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./logsoftmax/callasfunction%28_%29.md)

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
- [class HardSwish](./hardswish.md)
  Applies the hardswish function, element-wise
- [class LeakyReLU](./leakyrelu.md)
  Applies the Leaky Rectified Linear Unit.
- [class LogSigmoid](./logsigmoid.md)
  Applies the Log Sigmoid function.
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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/logsoftmax)*