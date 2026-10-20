# learningRate

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

A value that specifies the learning rate.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
var learningRate: Float { get set }
```

## See Also

### Inspecting the Properties of an RMSProp Optimizer
- [var alpha: Float](./alpha.md)
  A constant that specifies smoothing.
- [var epsilon: Float](./epsilon.md)
  A term that the optimizer adds to the denominator.
- [var centered: Bool](./centered.md)
  A Boolean value that specifies whether to use the centered variant.
- [var momentum: Float](./momentum.md)
  The rate of momentum decay.
- [var gradientScale: Float](./gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](./regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](./gradientbounds.md)
  The values for the minimum and maximum gradients.
- [var gradientClipping: BNNS.GradientClipping](./gradientclipping.md)
  The gradient clipping.
- [BNNS.GradientClipping](../gradientclipping.md)
  Constants that describe clipping functions.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](./regularizationfunction.md)
  The variable that specifies the regularization function.
- [var accumulatorCountMultiplier: Int](./accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/rmspropoptimizer/learningrate)*