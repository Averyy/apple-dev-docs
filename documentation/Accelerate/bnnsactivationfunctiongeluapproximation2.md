# BNNSActivationFunctionGELUApproximation2

**Framework**: Accelerate  
**Kind**: var

An activation function that provides a fast evaluation of the Gaussian error linear units (GELU) approximation on its input.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS 1.0+
- watchOS 7.0+

## Declaration

```swift
var BNNSActivationFunctionGELUApproximation2: BNNSActivationFunction { get }
```

#### Discussion

This constant defines an activation function that returns values using the following operation:

```c
x * (ReLU 6(x + 3.0) * 1.0 / 6.0)
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`, an `alpha` of `0.1`, and a `beta` of `1.0`. The thinner, dashed line shows, for comparison, the result of [`BNNSActivationFunctionGELUApproximation`](bnnsactivationfunctiongeluapproximation.md) using the same `alpha` and `beta` values:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://docs-assets.developer.apple.com/published/5ac577d745505877013fe1dec4d4194a/media-3604084%402x.png)

## See Also

- [init(UInt32)](bnnsactivationfunction/init(_:).md)
- [init(rawValue: UInt32)](bnnsactivationfunction/init(rawvalue:).md)
- [var rawValue: UInt32](bnnsactivationfunction/rawvalue.md)
- [var BNNSActivationFunctionAbs: BNNSActivationFunction](bnnsactivationfunctionabs.md)
- [var BNNSActivationFunctionCELU: BNNSActivationFunction](bnnsactivationfunctioncelu.md)
  An activation function that evaluates the continuously differentiable exponential linear units (CELU) on its input.
- [var BNNSActivationFunctionClampedLeakyRectifiedLinear: BNNSActivationFunction](bnnsactivationfunctionclampedleakyrectifiedlinear.md)
  An activation function that returns its input clamped to beta when that is greater than or equal to zero, otherwise it returns its input multiplied by alpha clamped to beta.
- [var BNNSActivationFunctionELU: BNNSActivationFunction](bnnsactivationfunctionelu.md)
  An activation function that evaluates the exponential linear units (ELU) on its input.
- [var BNNSActivationFunctionErf: BNNSActivationFunction](bnnsactivationfunctionerf.md)
- [var BNNSActivationFunctionGELU: BNNSActivationFunction](bnnsactivationfunctiongelu.md)
- [var BNNSActivationFunctionGELUApproximation: BNNSActivationFunction](bnnsactivationfunctiongeluapproximation.md)
  An activation function that evaluates the Gaussian error linear units (GELU) approximation on its input.
- [var BNNSActivationFunctionGELUApproximationSigmoid: BNNSActivationFunction](bnnsactivationfunctiongeluapproximationsigmoid.md)
- [var BNNSActivationFunctionGumbel: BNNSActivationFunction](bnnsactivationfunctiongumbel.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [var BNNSActivationFunctionGumbelMax: BNNSActivationFunction](bnnsactivationfunctiongumbelmax.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [var BNNSActivationFunctionHardShrink: BNNSActivationFunction](bnnsactivationfunctionhardshrink.md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input.
- [var BNNSActivationFunctionHardSigmoid: BNNSActivationFunction](bnnsactivationfunctionhardsigmoid.md)
  An activation function that returns the hard sigmoid function of its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunctiongeluapproximation2)*