# gradientClipping

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The gradient clipping.

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
var gradientClipping: BNNS.GradientClipping { get set }
```

## See Also

### Inspecting the Properties of an RMSProp Optimizer
- [var learningRate: Float](./learningrate.md)
  A value that specifies the learning rate.
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
- [BNNS.GradientClipping](../gradientclipping.md)
  Constants that describe clipping functions.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](./regularizationfunction.md)
  The variable that specifies the regularization function.
- [var accumulatorCountMultiplier: Int](./accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/rmspropoptimizer/gradientclipping)*