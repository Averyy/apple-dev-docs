# BNNS.ActivationFunction

**Framework**: Accelerate  
**Kind**: enum

Constants that describe activation functions.

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
enum ActivationFunction
```

## Topics

### Activation Functions
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
- [BNNS.ActivationFunction.linearWithBias(alpha:beta:)](bnns/activationfunction/linearwithbias(alpha:beta:).md)
  An activation function that returns its input multiplied by a scale and added to a bias.
- [BNNS.ActivationFunction.logSigmoid](bnns/activationfunction/logsigmoid.md)
  An activation function that returns the logarithm of the sigmoid function of its input.
- [BNNS.ActivationFunction.logSoftmax](bnns/activationfunction/logsoftmax.md)
  An activation function that returns the logarithm of the softmax function of its input.
- [BNNS.ActivationFunction.rectifiedLinear](bnns/activationfunction/rectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns zero.
- [BNNS.ActivationFunction.scaledTanh(alpha:beta:)](bnns/activationfunction/scaledtanh(alpha:beta:).md)
  An activation function that returns the scaled hyperbolic tangent of its input.
- [BNNS.ActivationFunction.selu](bnns/activationfunction/selu.md)
  An activation function that evaluates the scaled exponential linear units (SELU) on its input.
- [BNNS.ActivationFunction.sigmoid](bnns/activationfunction/sigmoid.md)
  An activation function that returns the sigmoid function of its input.
- [BNNS.ActivationFunction.silu](bnns/activationfunction/silu.md)
  An activation function that returns the sigmoid linear unit (SiLU) function of its input.
- [BNNS.ActivationFunction.softShrink(alpha:)](bnns/activationfunction/softshrink(alpha:).md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input minus alpha.
- [BNNS.ActivationFunction.softmax](bnns/activationfunction/softmax.md)
  An activation function that returns the softmax function of its input.
- [BNNS.ActivationFunction.softplus(alpha:beta:)](bnns/activationfunction/softplus(alpha:beta:).md)
  An activation function that returns the softplus function of its input.
- [BNNS.ActivationFunction.softsign](bnns/activationfunction/softsign.md)
  An activation function that returns the softsign function of its input.
- [BNNS.ActivationFunction.tanh](bnns/activationfunction/tanh.md)
  An activation function that returns the hyperbolic tangent of its input.
- [BNNS.ActivationFunction.tanhShrink](bnns/activationfunction/tanhshrink.md)
  An activation function that returns its input minus the hyperbolic tangent of its input.
- [BNNS.ActivationFunction.threshold(alpha:beta:)](bnns/activationfunction/threshold(alpha:beta:).md)
  An activation function that returns beta if its input is less than a specified threshold, otherwise it returns its input.
### Instance Properties
- [var bnnsActivation: BNNSActivation](bnns/activationfunction/bnnsactivation.md)
  The underlying activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/activationfunction)*