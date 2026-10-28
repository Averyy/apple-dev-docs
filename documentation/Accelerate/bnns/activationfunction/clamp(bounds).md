# BNNS.ActivationFunction.clamp(bounds:)

**Framework**: Accelerate  
**Kind**: case  
**Role**: Case

An activation function that returns its input clamped to the specified range.

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
case clamp(bounds: ClosedRange<Float>)
```

## Discussion

This constant defines an activation function that returns values using the following operation:

```c
min(max(x, alpha), beta)
```

Use `alpha` and `beta` to specify the clamping range:

```swift
var activation = BNNSActivation(function: .clamp, 
                                alpha: -5, 
                                beta: 5)
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3654621@2x.png)

## See Also

### Activation Functions
- [BNNS.ActivationFunction.abs](./abs.md)
  An activation function that returns the absolute value of its input.
- [BNNS.ActivationFunction.celu(alpha:)](./celu%28alpha%29.md)
  An activation function that evaluates the continuously differentiable exponential linear units (CELU) on its input.
- [BNNS.ActivationFunction.clampedLeakyRectifiedLinear(alpha:beta:)](./clampedleakyrectifiedlinear%28alpha,beta%29.md)
  An activation function that returns its input clamped to beta when that is greater than or equal to zero, otherwise it returns its input multiplied by alpha clamped to beta.
- [BNNS.ActivationFunction.elu(alpha:)](./elu%28alpha%29.md)
  An activation function that evaluates the exponential linear units (ELU) on its input.
- [BNNS.ActivationFunction.geluApproximation(alpha:beta:)](./geluapproximation%28alpha,beta%29.md)
  An activation function that evaluates the Gaussian error linear units (GELU) approximation on its input.
- [BNNS.ActivationFunction.geluApproximation2(alpha:beta:)](./geluapproximation2%28alpha,beta%29.md)
  An activation function that provides a fast evaluation of the Gaussian error linear units (GELU) approximation on its input.
- [BNNS.ActivationFunction.gumbel(alpha:beta:)](./gumbel%28alpha,beta%29.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [BNNS.ActivationFunction.gumbelMax(alpha:beta:)](./gumbelmax%28alpha,beta%29.md)
  An activation function that returns random numbers from the Gumbel distribution.
- [BNNS.ActivationFunction.hardShrink(alpha:)](./hardshrink%28alpha%29.md)
  An activation function that returns zero when the absolute input is less than alpha, otherwise it returns its input.
- [BNNS.ActivationFunction.hardSigmoid(alpha:beta:)](./hardsigmoid%28alpha,beta%29.md)
  An activation function that returns the hard sigmoid function of its input.
- [BNNS.ActivationFunction.hardSwish(alpha:beta:)](./hardswish%28alpha,beta%29.md)
  An activation function that returns the hard swish function of its input.
- [BNNS.ActivationFunction.identity](./identity.md)
  An activation function that returns its input.
- [BNNS.ActivationFunction.leakyRectifiedLinear(alpha:)](./leakyrectifiedlinear%28alpha%29.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns its input multiplied by a specified value.
- [BNNS.ActivationFunction.linear(alpha:)](./linear%28alpha%29.md)
  An activation function that returns its input multiplied by a specified value.
- [BNNS.ActivationFunction.linearWithBias(alpha:beta:)](./linearwithbias%28alpha,beta%29.md)
  An activation function that returns its input multiplied by a scale and added to a bias.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/activationfunction/clamp(bounds:))*