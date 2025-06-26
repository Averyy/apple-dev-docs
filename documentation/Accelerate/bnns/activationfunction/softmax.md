# BNNS.ActivationFunction.softmax

**Framework**: Accelerate  
**Kind**: case

An activation function that returns the softmax function of its input.

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
case softmax
```

#### Discussion

This constant defines an activation function that returns values using the following formula:

![General formula that describes mathematically the softmax activation function. s open bracket x sub i close bracket equals  the exponential of x sub i over summation from j equals one to n times the exponential of x sub j.](https://docs-assets.developer.apple.com/published/ce7621b84d5ab53d3174d8b6b257582c/media-3654663%402x.png)

The softmax function transforms a vector of real numbers into a vector of probabilities. Each probability in the result is in the range 0…1, and the sum of the probabilities is 1.

For example, given and array that contains the values `[3.0, 5.0, 1.0, 6.0, 2.0, 1.0, 4.0]`, the softmax function calculates the following values:

| Inputs | Outputs |
| --- | --- |
| `3.0` | `0.031415492` |
| `5.0` | `0.23213086` |
| `1.0` | `0.004251625` |
| `6.0` | `0.63099706` |
| `2.0` | `0.011557114` |
| `1.0` | `0.004251625` |
| `4.0` | `0.08539616` |

Changing the fourth element from `6.0` to `10.0` increases its probability to almost 1.0:

| Inputs | Outputs |
| --- | --- |
| `3.0` | `0.00090221845` |
| `5.0` | `0.0066665425` |
| `1.0` | `0.00012210199` |
| `10.0` | `0.98940265` |
| `2.0` | `0.00033190762` |
| `1.0` | `0.00012210199` |
| `4.0` | `0.002452484` |

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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnns/activationfunction/softmax)*