# gradientClipping

**Framework**: Accelerate  
**Kind**: property

The gradient clipping.

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
var gradientClipping: BNNS.GradientClipping { get set }
```

## See Also

- [var learningRate: Float](bnns/sgdmomentumoptimizer/learningrate.md)
  A value that specifies the learning rate.
- [var momentum: Float](bnns/sgdmomentumoptimizer/momentum.md)
  The rate of momentum decay.
- [var gradientScale: Float](bnns/sgdmomentumoptimizer/gradientscale.md)
  A value that specifies the gradient scaling factor.
- [var regularizationScale: Float](bnns/sgdmomentumoptimizer/regularizationscale.md)
  A value that specifies the regularization scaling factor.
- [var gradientBounds: ClosedRange<Float>?](bnns/sgdmomentumoptimizer/gradientbounds.md)
  The values for the minimum and maximum gradients.
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.
- [var usesNestrovMomentum: Bool](bnns/sgdmomentumoptimizer/usesnestrovmomentum.md)
  A Boolean value that specifies whether to use Nesterov momentum update.
- [var regularizationFunction: BNNSOptimizerRegularizationFunction](bnns/sgdmomentumoptimizer/regularizationfunction.md)
  The variable that specifies the regularization function.
- [var sgdMomentumVariant: BNNSOptimizerSGDMomentumVariant](bnns/sgdmomentumoptimizer/sgdmomentumvariant.md)
  The variable that specifies the momentum variant.
- [var accumulatorCountMultiplier: Int](bnns/sgdmomentumoptimizer/accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/sgdmomentumoptimizer/gradientclipping)*