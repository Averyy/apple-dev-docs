# learningRate

**Framework**: Accelerate  
**Kind**: property

A value that specifies the learning rate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
var learningRate: Float { get set }
```

## See Also

- [var beta1: Float](bnns/adamoptimizer/beta1.md)
  A value that specifies the first-moment constant, in the range `0` to `1`.
- [var beta2: Float](bnns/adamoptimizer/beta2.md)
  A value that specifies the second-moment constant, in the range `0` to `1`.
- [var timeStep: Float](bnns/adamoptimizer/timestep.md)
  A value that’s at least `1` and represents the optimizer’s current time.
- [var epsilon: Float](bnns/adamoptimizer/epsilon.md)
  The epsilon value you use to improve numerical stability.
- [var gradientScale: Float](bnns/adamoptimizer/gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](bnns/adamoptimizer/regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](bnns/adamoptimizer/gradientbounds.md)
  The values for the minimum and maximum gradients.
- [var gradientClipping: BNNS.GradientClipping](bnns/adamoptimizer/gradientclipping.md)
  The gradient clipping.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](bnns/adamoptimizer/regularizationfunction.md)
  The variable that specifies the regularization function.
- [var usesAMSGrad: Bool](bnns/adamoptimizer/usesamsgrad.md)
  A Boolean value that specifies whether to use the AMSGrad variant.
- [var accumulatorCountMultiplier: Int](bnns/adamoptimizer/accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/adamoptimizer/learningrate)*