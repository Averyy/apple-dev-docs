# gradientScale

**Framework**: Accelerate  
**Kind**: property

A value that specifies the gradient scaling factor.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst ?+
- macOS 12.0+
- tvOS 15.0+
- visionOS ?+
- watchOS 8.0+
- Unknown ?+ - Deprecated

## Declaration

```swift
var gradientScale: Float { get set }
```

## See Also

- [var learningRate: Float](bnns/adamwoptimizer/learningrate.md)
  A value that specifies the learning rate.
- [var beta1: Float](bnns/adamwoptimizer/beta1.md)
  A value that specifies the first-moment constant, in the range `0` to `1`.
- [var beta2: Float](bnns/adamwoptimizer/beta2.md)
  A value that specifies the second-moment constant, in the range `0` to `1`.
- [var timeStep: Float](bnns/adamwoptimizer/timestep.md)
  A value that’s at least `1` and represents the optimizer’s current time.
- [var epsilon: Float](bnns/adamwoptimizer/epsilon.md)
  The epsilon value you use to improve numerical stability.
- [var weightDecay: Float](bnns/adamwoptimizer/weightdecay.md)
  The weight decay coefficient.
- [var gradientClipping: BNNS.GradientClipping](bnns/adamwoptimizer/gradientclipping.md)
  The gradient clipping function and bounds.
- [BNNS.GradientClipping](bnns/gradientclipping.md)
  Constants that describe clipping functions.
- [var accumulatorCountMultiplier: Int](bnns/adamwoptimizer/accumulatorcountmultiplier.md)
  The number of accumulators required for each parameter.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/adamwoptimizer/gradientscale)*