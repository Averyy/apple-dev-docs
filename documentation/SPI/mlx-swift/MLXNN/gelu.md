---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/gelu"
framework: "mlx-swift/MLXNN"
---

# GELU

**Framework**: mlx-swift/MLXNN  
**Kind**: class  
**Role**: Class

Applies the Gaussian Error Linear Units function.

## Declaration

```swift
class GELU
```

#### Overview

There are three variations:

- [`GELU.Approximation.none`](./gelu/approximation-swift.enum/none.md)
- [`GELU.Approximation.precise`](./gelu/approximation-swift.enum/precise.md)
- [`GELU.Approximation.fast`](./gelu/approximation-swift.enum/fast.md)

##### See Also

- [Activation Functions and Layers](./activations.md)
- [`gelu(_:)`](./gelu%28_%29.md)
- [`geluApproximate(_:)`](./geluapproximate%28_%29.md)
- [`geluFastApproximate(_:)`](./gelufastapproximate%28_%29.md)

## Topics

### Initializers
- [init(approximation: GELU.Approximation)](./gelu/init%28approximation%29.md)
### Instance Properties
- [let approximation: GELU.Approximation](./gelu/approximation-swift.property.md)
### Instance Methods
- [func callAsFunction(MLXArray) -> MLXArray](./gelu/callasfunction%28_%29.md)
### Enumerations
- [GELU.Approximation](./gelu/approximation-swift.enum.md)

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

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/gelu)*