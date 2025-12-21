# BNNS.ActivationFunction.geluApproximation(alpha:beta:)

**Framework**: Accelerate  
**Kind**: case

An activation function that evaluates the Gaussian error linear units (GELU) approximation on its input.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst ?+
- macOS 11.0+
- tvOS 14.0+
- visionOS ?+
- watchOS 7.0+

## Declaration

```swift
case geluApproximation(alpha: Float, beta: Float)
```

#### Discussion

This constant defines an activation function that returns values using the following operation:

```c
0.5f * x * (1.0f + tanh(alpha*(x + beta * x * x * x)))
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`, an `alpha` of `0.1` and a `beta` of `1.0`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis.](https://docs-assets.developer.apple.com/published/4267a193df0a51623971fe7f0c23464a/media-3654645%402x.png)

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
- [BNNS.ActivationFunction.linearWithBias(alpha:beta:)](bnns/activationfunction/linearwithbias(alpha:beta:).md)
  An activation function that returns its input multiplied by a scale and added to a bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/activationfunction/geluapproximation(alpha:beta:))*