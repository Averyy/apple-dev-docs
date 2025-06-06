# BNNS.ActivationFunction.selu

**Framework**: Accelerate  
**Kind**: case

An activation function that evaluates the scaled exponential linear units (SELU) on its input.

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
case selu
```

#### Discussion

This constant defines an activation function that returns values using the following operation:

```c
// λ and ɑ have the values given by Klambauer, Unterthiner and Mayr 
// (~1.0507 and ~1.6733, respectively)

if x < 0
    λɑ(exp(x)-1)
else
    λx
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://docs-assets.developer.apple.com/published/be10a271a529d567537ef2f67daa29f7/media-3654657%402x.png)

## See Also

- [BNNS.ActivationFunction.abs](bnns/activationfunction/abs.md)
  An activation function that returns the absolute value of its input.
- [BNNS.ActivationFunction.celu(alpha:)](bnns/activationfunction/celu(alpha:).md)
  An activation function that evaluates the continuously differentiable exponential linear units (CELU) on its input.
- [BNNS.ActivationFunction.clamp(bounds:)](bnns/activationfunction/clamp(bounds:).md)
  An activation function that returns its input clamped to the specified range.
- [BNNS.ActivationFunction.clampedLeakyRectifiedLinear(alpha:beta:)](bnns/activationfunction/clampedleakyrectifiedlinear(alpha:beta:).md)
  An activation function that returns its input clamped to beta when that is greater than or equal to zero, otherwise it returns its input multiplied by alpha clamped to beta.
- [BNNS.ActivationFunction.elu(alpha:)](bnns/activationfunction/elu(alpha:).md)
  An activation function that evaluates the exponential linear units (ELU) on its input.
- [BNNS.ActivationFunction.geluApproximation(alpha:beta:)](bnns/activationfunction/geluapproximation(alpha:beta:).md)
  An activation function that evaluates the Gaussian error linear units (GELU) approximation on its input.
- [BNNS.ActivationFunction.geluApproximation2(alpha:beta:)](bnns/activationfunction/geluapproximation2(alpha:beta:).md)
  An activation function that provides a fast evaluation of the Gaussian error linear units (GELU) approximation on its input.
- [BNNS.ActivationFunction.gumbel(alpha:beta:)](bnns/activationfunction/gumbel(alpha:beta:).md)
  An activation function that returns random numbers from the Gumbel distribution.
- [BNNS.ActivationFunction.gumbelMax(alpha:beta:)](bnns/activationfunction/gumbelmax(alpha:beta:).md)
  An activation function that returns random numbers from the Gumbel distribution.
- [BNNS.ActivationFunction.hardShrink(alpha:)](bnns/activationfunction/hardshrink(alpha:).md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input.
- [BNNS.ActivationFunction.hardSigmoid(alpha:beta:)](bnns/activationfunction/hardsigmoid(alpha:beta:).md)
  An activation function that returns the hard sigmoid function of its input.
- [BNNS.ActivationFunction.hardSwish(alpha:beta:)](bnns/activationfunction/hardswish(alpha:beta:).md)
  An activation function that returns the hard swish function of its input.
- [BNNS.ActivationFunction.identity](bnns/activationfunction/identity.md)
  An activation function that returns its input.
- [BNNS.ActivationFunction.leakyRectifiedLinear(alpha:)](bnns/activationfunction/leakyrectifiedlinear(alpha:).md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns its input multiplied by a specified value.
- [BNNS.ActivationFunction.linear(alpha:)](bnns/activationfunction/linear(alpha:).md)
  An activation function that returns its input multiplied by a specified value.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/activationfunction/selu)*