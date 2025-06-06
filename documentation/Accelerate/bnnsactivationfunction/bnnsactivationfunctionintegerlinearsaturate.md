# BNNSActivationFunctionIntegerLinearSaturate

**Framework**: Accelerate  
**Kind**: case

An activation function that returns an arithmetic shift, preserving sign.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
BNNSActivationFunctionIntegerLinearSaturate
```

#### Discussion

This constant defines an activation function that returns values using the following operation:

```c
saturate<output_type>((iscale * x + ioffset) >> ishift)
```

## See Also

- [var BNNSActivationFunctionCELU: BNNSActivationFunction](bnnsactivationfunctioncelu.md)
  An activation function that evaluates the continuously differentiable exponential linear units (CELU) on its input.
- [BNNSActivationFunctionClamp](bnnsactivationfunction/bnnsactivationfunctionclamp.md)
  An activation function that returns its input clamped to the specified range.
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
- [var BNNSActivationFunctionHardSigmoid: BNNSActivationFunction](bnnsactivationfunctionhardsigmoid.md)
  An activation function that returns the hard sigmoid function of its input.
- [var BNNSActivationFunctionHardSwish: BNNSActivationFunction](bnnsactivationfunctionhardswish.md)
  An activation function that returns the hard swish function of its input.
- [BNNSActivationFunctionIntegerLinearSaturatePerChannel](bnnsactivationfunction/bnnsactivationfunctionintegerlinearsaturateperchannel.md)
  An activation function that returns an arithmetic shift, preserving sign for each channel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctionintegerlinearsaturate)*