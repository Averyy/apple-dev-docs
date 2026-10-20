# BNNS.GradientClipping

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe clipping functions.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS
- watchOS 8.0+

## Declaration

```swift
enum GradientClipping
```

## Topics

### Gradient Clipping Functions
- [BNNS.GradientClipping.none](./gradientclipping/none.md)
  A constant that indicates that the operation doesn’t clip gradients.
- [case byValue(bounds: ClosedRange<Float>)](./gradientclipping/byvalue%28bounds%29.md)
  A constant that indicates that the operation clips gradients to a specified range.
- [BNNS.GradientClipping.byNorm(threshold:)](./gradientclipping/bynorm%28threshold%29.md)
  A constant that indicates that the operation clips gradients to a specified Euclidean norm.
- [BNNS.GradientClipping.byGlobalNorm(threshold:globalNorm:)](./gradientclipping/byglobalnorm%28threshold,globalnorm%29.md)
  A constant that indicates that the operation clips gradients to a specified global Euclidean norm.

## See Also

### Inspecting the Properties of an Adam Optimizer
- [var learningRate: Float](./adamoptimizer/learningrate.md)
  A value that specifies the learning rate.
- [var beta1: Float](./adamoptimizer/beta1.md)
  A value that specifies the first-moment constant, in the range `0` to `1`.
- [var beta2: Float](./adamoptimizer/beta2.md)
  A value that specifies the second-moment constant, in the range `0` to `1`.
- [var timeStep: Float](./adamoptimizer/timestep.md)
  A value that’s at least `1` and represents the optimizer’s current time.
- [var epsilon: Float](./adamoptimizer/epsilon.md)
  The epsilon value you use to improve numerical stability.
- [var gradientScale: Float](./adamoptimizer/gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](./adamoptimizer/regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](./adamoptimizer/gradientbounds.md)
  The values for the minimum and maximum gradients.
- [var gradientClipping: BNNS.GradientClipping](./adamoptimizer/gradientclipping.md)
  The gradient clipping.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](./adamoptimizer/regularizationfunction.md)
  The variable that specifies the regularization function.
- [var usesAMSGrad: Bool](./adamoptimizer/usesamsgrad.md)
  A Boolean value that specifies whether to use the AMSGrad variant.
- [var accumulatorCountMultiplier: Int](./adamoptimizer/accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/gradientclipping)*