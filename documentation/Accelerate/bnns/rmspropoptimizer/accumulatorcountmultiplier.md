# accumulatorCountMultiplier

**Framework**: Accelerate  
**Kind**: property

The number of accumulators required for each parameter.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
var accumulatorCountMultiplier: Int { get }
```

## See Also

- [var learningRate: Float](bnns/rmspropoptimizer/learningrate.md)
  A value that specifies the learning rate.
- [var alpha: Float](bnns/rmspropoptimizer/alpha.md)
  A constant that specifies smoothing.
- [var epsilon: Float](bnns/rmspropoptimizer/epsilon.md)
  A term that the optimizer adds to the denominator.
- [var centered: Bool](bnns/rmspropoptimizer/centered.md)
  A Boolean value that specifies whether to use the centered variant.
- [var momentum: Float](bnns/rmspropoptimizer/momentum.md)
  The rate of momentum decay.
- [var gradientScale: Float](bnns/rmspropoptimizer/gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](bnns/rmspropoptimizer/regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](bnns/rmspropoptimizer/gradientbounds.md)
  The values for the minimum and maximum gradients.
- [var gradientClipping: BNNS.GradientClipping](bnns/rmspropoptimizer/gradientclipping.md)
  The gradient clipping.
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](bnns/rmspropoptimizer/regularizationfunction.md)
  The variable that specifies the regularization function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/rmspropoptimizer/accumulatorcountmultiplier)*