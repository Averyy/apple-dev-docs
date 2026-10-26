---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/step(_:threshold:)"
framework: "mlx-swift/MLXNN"
---

# step(_:threshold:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Applies the Step Activation Function.

## Declaration

```swift
func step(_ x: MLXArray, threshold: Float = 0.0) -> MLXArray
```

#### Discussion

This function implements a binary step activation, where the output is set to 1 if the input is greater than a specified threshold, and 0 otherwise.

This is:

```swift
MLX.where(x .> threshold, 1, 0)
```

##### See Also

- [Activation Functions and Layers](./activations.md)
- [`Step`](./step.md)

## See Also

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
- [func hardSwish(MLXArray) -> MLXArray](./hardswish%28_%29.md)
  Applies the hardswish function, element-wise
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


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/step(_:threshold:))*