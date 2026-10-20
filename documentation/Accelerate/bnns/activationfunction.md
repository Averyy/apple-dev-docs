# BNNS.ActivationFunction

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that describe activation functions.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+
- visionOS
- watchOS 7.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
enum ActivationFunction
```

## Topics

### Activation Functions
- [BNNS.ActivationFunction.abs](./activationfunction/abs.md)
  An activation function that returns the absolute value of its input.
- [BNNS.ActivationFunction.celu(alpha:)](./activationfunction/celu%28alpha%29.md)
  An activation function that evaluates the continuously differentiable exponential linear units (CELU) on its input.
- [BNNS.ActivationFunction.clamp(bounds:)](./activationfunction/clamp%28bounds%29.md)
  An activation function that returns its input clamped to the specified range.
- [BNNS.ActivationFunction.clampedLeakyRectifiedLinear(alpha:beta:)](./activationfunction/clampedleakyrectifiedlinear%28alpha,beta%29.md)
  An activation function that returns its input clamped to beta when that is greater than or equal to zero, otherwise it returns its input multiplied by alpha clamped to beta.
- [BNNS.ActivationFunction.elu(alpha:)](./activationfunction/elu%28alpha%29.md)
  An activation function that evaluates the exponential linear units (ELU) on its input.
- [BNNS.ActivationFunction.geluApproximation(alpha:beta:)](./activationfunction/geluapproximation%28alpha,beta%29.md)
  An activation function that evaluates the Gaussian error linear units (GELU) approximation on its input.
- [BNNS.ActivationFunction.geluApproximation2(alpha:beta:)](./activationfunction/geluapproximation2%28alpha,beta%29.md)
  An activation function that provides a fast evaluation of the Gaussian error linear units (GELU) approximation on its input.
- [BNNS.ActivationFunction.gumbel(alpha:beta:)](./activationfunction/gumbel%28alpha,beta%29.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [BNNS.ActivationFunction.gumbelMax(alpha:beta:)](./activationfunction/gumbelmax%28alpha,beta%29.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [BNNS.ActivationFunction.hardShrink(alpha:)](./activationfunction/hardshrink%28alpha%29.md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input.
- [BNNS.ActivationFunction.hardSigmoid(alpha:beta:)](./activationfunction/hardsigmoid%28alpha,beta%29.md)
  An activation function that returns the hard sigmoid function of its input.
- [BNNS.ActivationFunction.hardSwish(alpha:beta:)](./activationfunction/hardswish%28alpha,beta%29.md)
  An activation function that returns the hard swish function of its input.
- [BNNS.ActivationFunction.identity](./activationfunction/identity.md)
  An activation function that returns its input.
- [BNNS.ActivationFunction.leakyRectifiedLinear(alpha:)](./activationfunction/leakyrectifiedlinear%28alpha%29.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns its input multiplied by a specified value.
- [BNNS.ActivationFunction.linear(alpha:)](./activationfunction/linear%28alpha%29.md)
  An activation function that returns its input multiplied by a specified value.
- [BNNS.ActivationFunction.linearWithBias(alpha:beta:)](./activationfunction/linearwithbias%28alpha,beta%29.md)
  An activation function that returns its input multiplied by a scale and added to a bias.
- [BNNS.ActivationFunction.logSigmoid](./activationfunction/logsigmoid.md)
  An activation function that returns the logarithm of the sigmoid function of its input.
- [BNNS.ActivationFunction.logSoftmax](./activationfunction/logsoftmax.md)
  An activation function that returns the logarithm of the softmax function of its input.
- [BNNS.ActivationFunction.rectifiedLinear](./activationfunction/rectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns zero.
- [BNNS.ActivationFunction.scaledTanh(alpha:beta:)](./activationfunction/scaledtanh%28alpha,beta%29.md)
  An activation function that returns the scaled hyperbolic tangent of its input.
- [BNNS.ActivationFunction.selu](./activationfunction/selu.md)
  An activation function that evaluates the scaled exponential linear units (SELU) on its input.
- [BNNS.ActivationFunction.sigmoid](./activationfunction/sigmoid.md)
  An activation function that returns the sigmoid function of its input.
- [BNNS.ActivationFunction.silu](./activationfunction/silu.md)
  An activation function that returns the sigmoid linear unit (SiLU) function of its input.
- [BNNS.ActivationFunction.softShrink(alpha:)](./activationfunction/softshrink%28alpha%29.md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input minus alpha.
- [BNNS.ActivationFunction.softmax](./activationfunction/softmax.md)
  An activation function that returns the softmax function of its input.
- [BNNS.ActivationFunction.softplus(alpha:beta:)](./activationfunction/softplus%28alpha,beta%29.md)
  An activation function that returns the softplus function of its input.
- [BNNS.ActivationFunction.softsign](./activationfunction/softsign.md)
  An activation function that returns the softsign function of its input.
- [BNNS.ActivationFunction.tanh](./activationfunction/tanh.md)
  An activation function that returns the hyperbolic tangent of its input.
- [BNNS.ActivationFunction.tanhShrink](./activationfunction/tanhshrink.md)
  An activation function that returns its input minus the hyperbolic tangent of its input.
- [BNNS.ActivationFunction.threshold(alpha:beta:)](./activationfunction/threshold%28alpha,beta%29.md)
  An activation function that returns beta if its input is less than a specified threshold, otherwise it returns its input.
### Instance Properties
- [var bnnsActivation: BNNSActivation](./activationfunction/bnnsactivation.md)
  The underlying activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/activationfunction)*