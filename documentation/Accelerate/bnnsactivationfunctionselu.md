# BNNSActivationFunctionSELU

**Framework**: Accelerate  
**Kind**: var

An activation function that evaluates the scaled exponential linear units (SELU) on its input.

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
var BNNSActivationFunctionSELU: BNNSActivationFunction { get }
```

#### Discussion

This constant defines an activation function that returns values using the following operation:

```None
// λ and ɑ have the values given by Klambauer, Unterthiner and Mayr 
// (~1.0507 and ~1.6733, respectively)

if x < 0
    λɑ(exp(x)-1)
else
    λx
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://docs-assets.developer.apple.com/published/6d06ab19caa65397994f694396e05d88/media-3560501%402x.png)

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunctionselu)*