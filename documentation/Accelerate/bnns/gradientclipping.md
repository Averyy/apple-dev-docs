# BNNS.GradientClipping

**Framework**: Accelerate  
**Kind**: enum

Constants that describe clipping functions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+

## Declaration

```swift
enum GradientClipping
```

## Topics

### Gradient Clipping Functions
- [BNNS.GradientClipping.none](bnns/gradientclipping/none.md)
  A constant that indicates that the operation doesn’t clip gradients.
- [case byValue(bounds: ClosedRange<Float>)](bnns/gradientclipping/byvalue(bounds:).md)
  A constant that indicates that the operation clips gradients to a specified range.
- [BNNS.GradientClipping.byNorm(threshold:)](bnns/gradientclipping/bynorm(threshold:).md)
  A constant that indicates that the operation clips gradients to a specified Euclidean norm.
- [BNNS.GradientClipping.byGlobalNorm(threshold:globalNorm:)](bnns/gradientclipping/byglobalnorm(threshold:globalnorm:).md)
  A constant that indicates that the operation clips gradients to a specified global Euclidean norm.

## See Also

- [var learningRate: Float](bnns/adamoptimizer/learningrate.md)
  A value that specifies the learning rate.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/gradientclipping)*