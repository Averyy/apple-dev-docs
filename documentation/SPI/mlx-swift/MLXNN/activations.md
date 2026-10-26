---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/activations"
framework: "mlx-swift/MLXNN"
---

# Activation Functions and Layers

**Framework**: mlx-swift/MLXNN  
**Role**: API Collection

Built-in activation functions and layers.

#### Overview

`MLXNN` provides a number of activation functions and modules.  The modules simply wrap the functions, though some like [`GELU`](./gelu.md) provide some settings that select between different functions.  Others, like [`CELU`](./celu.md) encapsulate parameters such as `alpha`.

## Topics

### Activation Free Functions
- [func celu(MLXArray, alpha: Float) -> MLXArray](./celu%28_,alpha%29.md)
  Applies the Continuously Differentiable Exponential Linear Unit.
- [func elu(MLXArray, alpha: Float) -> MLXArray](./elu%28_,alpha%29.md)
  Applies the Exponential Linear Unit.
- [func gelu(MLXArray) -> MLXArray](./gelu%28_%29.md)
  Applies the Gaussian Error Linear Units function.
- [func geluApproximate(MLXArray) -> MLXArray](./geluapproximate%28_%29.md)
  An approximation to Gaussian Error Linear Unit.
- [func geluFastApproximate(MLXArray) -> MLXArray](./gelufastapproximate%28_%29.md)
  A fast approximation to Gaussian Error Linear Unit.
- [func glu(MLXArray, axis: Int) -> MLXArray](./glu%28_,axis%29.md)
  Applies the gated linear unit function.
- [func hardShrink(MLXArray, lambda: Float) -> MLXArray](./hardshrink%28_,lambda%29.md)
  Applies the HardShrink activation function.
- [func hardSwish(MLXArray) -> MLXArray](./hardswish%28_%29.md)
  Applies the hardswish function, element-wise
- [func hardTanH(MLXArray, min: Float, max: Float) -> MLXArray](./hardtanh%28_,min,max%29.md)
  Applies the HardTanh function.
- [func leakyRelu(MLXArray, negativeSlope: Float) -> MLXArray](./leakyrelu%28_,negativeslope%29.md)
  Applies the Leaky Rectified Linear Unit.
- [func logSigmoid(MLXArray) -> MLXArray](./logsigmoid%28_%29.md)
  Applies the Log Sigmoid function.
- [func logSoftmax(MLXArray, axis: Int) -> MLXArray](./logsoftmax%28_,axis%29.md)
  Applies the Log Softmax function.
- [func mish(MLXArray) -> MLXArray](./mish%28_%29.md)
  Applies the Mish function, element-wise.
- [func prelu(MLXArray, alpha: MLXArray) -> MLXArray](./prelu%28_,alpha%29.md)
  Applies the element-wise parametric ReLU.
- [func relu(MLXArray) -> MLXArray](./relu%28_%29.md)
  Applies the Rectified Linear Unit.
- [func relu6(MLXArray) -> MLXArray](./relu6%28_%29.md)
  Applies the Rectified Linear Unit 6.
- [func reluSquared(MLXArray) -> MLXArray](./relusquared%28_%29.md)
  Applies the squared Rectified Linear Unit.
- [func selu(MLXArray) -> MLXArray](./selu%28_%29.md)
  Applies the Scaled Exponential Linear Unit.
- [func sigmoid(MLXArray) -> MLXArray](./sigmoid%28_%29.md)
  Applies the element-wise logistic sigmoid.
- [func silu(MLXArray) -> MLXArray](./silu%28_%29.md)
  Applies the Sigmoid Linear Unit. Also known as Swish.
- [func softmin(MLXArray, axis: Int) -> MLXArray](./softmin%28_,axis%29.md)
  Applies the Softmin function.
- [func softplus(MLXArray) -> MLXArray](./softplus%28_%29.md)
  Applies the Softplus function.
- [func softshrink(MLXArray, lambda: Float) -> MLXArray](./softshrink%28_,lambda%29.md)
  Applies the Softshrink activation function.
- [func softsign(MLXArray) -> MLXArray](./softsign%28_%29.md)
  Applies the Softsign function.
- [func step(MLXArray, threshold: Float) -> MLXArray](./step%28_,threshold%29.md)
  Applies the Step Activation Function.
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
- [class SELU](./selu.md)
  Applies the Scaled Exponential Linear Unit.
- [class Sigmoid](./sigmoid.md)
  Applies the element-wise logistic sigmoid.
- [class SiLU](./silu.md)
  Applies the Sigmoid Linear Unit. Also known as Swish.
- [class Softmax](./softmax.md)
  Applies the Softmax function.
- [class Softmin](./softmin.md)
  Applies the Softmin function.
- [class Softplus](./softplus.md)
  Applies the Softplus function.
- [class Softshrink](./softshrink.md)
  Applies the Softshrink activation function.
- [class Softsign](./softsign.md)
  Applies the Softsign function.
- [class Step](./step.md)
  Applies the Step Activation Function.
- [class Tanh](./tanh.md)
  Applies the hyperbolic tangent function


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/activations)*