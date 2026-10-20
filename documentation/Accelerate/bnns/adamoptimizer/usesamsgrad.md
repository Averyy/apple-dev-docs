# usesAMSGrad

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A Boolean value that specifies whether to use the AMSGrad variant.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
var usesAMSGrad: Bool { get set }
```

## See Also

### Inspecting the Properties of an Adam Optimizer
- [var learningRate: Float](./learningrate.md)
  A value that specifies the learning rate.
- [var beta1: Float](./beta1.md)
  A value that specifies the first-moment constant, in the range `0` to `1`.
- [var beta2: Float](./beta2.md)
  A value that specifies the second-moment constant, in the range `0` to `1`.
- [var timeStep: Float](./timestep.md)
  A value that’s at least `1` and represents the optimizer’s current time.
- [var epsilon: Float](./epsilon.md)
  The epsilon value you use to improve numerical stability.
- [var gradientScale: Float](./gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](./regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](./gradientbounds.md)
  The values for the minimum and maximum gradients.
- [var gradientClipping: BNNS.GradientClipping](./gradientclipping.md)
  The gradient clipping.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](./regularizationfunction.md)
  The variable that specifies the regularization function.
- [var accumulatorCountMultiplier: Int](./accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.
- [BNNS.GradientClipping](../gradientclipping.md)
  Constants that describe clipping functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/adamoptimizer/usesamsgrad)*