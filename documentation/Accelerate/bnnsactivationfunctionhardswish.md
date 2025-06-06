# BNNSActivationFunctionHardSwish

**Framework**: Accelerate  
**Kind**: var

An activation function that returns the hard swish function of its input.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
var BNNSActivationFunctionHardSwish: BNNSActivationFunction { get }
```

#### Discussion

This constant defines an activation function that returns values using the following operation:

```c
HardSwish(x) = x * (ReLU6(x + 3.0) * 1.0/6.0)
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://docs-assets.developer.apple.com/published/be309d29bd81c0f09389f408ab11e397/media-3760902%402x.png)

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
- [var BNNSActivationFunctionGELUApproximation2: BNNSActivationFunction](bnnsactivationfunctiongeluapproximation2.md)
  An activation function that provides a fast evaluation of the Gaussian error linear units (GELU) approximation on its input.
- [var BNNSActivationFunctionGELUApproximationSigmoid: BNNSActivationFunction](bnnsactivationfunctiongeluapproximationsigmoid.md)
- [var BNNSActivationFunctionGumbel: BNNSActivationFunction](bnnsactivationfunctiongumbel.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [var BNNSActivationFunctionGumbelMax: BNNSActivationFunction](bnnsactivationfunctiongumbelmax.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [var BNNSActivationFunctionHardShrink: BNNSActivationFunction](bnnsactivationfunctionhardshrink.md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunctionhardswish)*