---
url: "https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/elu(_:alpha:)"
framework: "mlx-swift/MLXNN"
---

# elu(_:alpha:)

**Framework**: mlx-swift/MLXNN  
**Kind**: func  
**Role**: Function

Applies the Exponential Linear Unit.

## Declaration

```swift
func elu(_ x: MLXArray, alpha: Float = 1.0) -> MLXArray
```

## Discussion

This is:

```swift
MLX.which(x .> 0, x, alpha * (exp(x) - 1))
```

### See Also

- [Activation Functions and Layers](./activations.md)

## See Also

### Activation Free Functions
- [func celu(MLXArray, alpha: Float) -> MLXArray](./celu%28_,alpha%29.md)
  Applies the Continuously Differentiable Exponential Linear Unit.
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
- [func selu(MLXArray) -> MLXArray](./selu%28_%29.md)
  Applies the Scaled Exponential Linear Unit.


---

*[View on Swift Package Index](https://swiftpackageindex.com/ml-explore/mlx-swift/main/documentation/mlxnn/elu(_:alpha:))*