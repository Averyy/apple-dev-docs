# softmax

**Framework**: Accelerate  
**Kind**: property

An activation function that returns the softmax function of its input.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+
- watchOS 4.0+
- Unknown ?+ - Deprecated
- Mac Catalyst ?+

## Declaration

```swift
static var softmax: BNNSActivationFunction { get }
```

#### Discussion

This constant defines an activation function that returns values using the following formula:

![General formula that describes mathematically the softmax activation function. s open bracket x sub i close bracket equals  the exponential of x sub i over summation from j equals one to n times the exponential of x sub j.](https://docs-assets.developer.apple.com/published/ce7621b84d5ab53d3174d8b6b257582c/media-3402491%402x.png)

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

- [static var abs: BNNSActivationFunction](bnnsactivationfunction/abs.md)
  An activation function that returns the absolute value of its input.
- [static var clamp: BNNSActivationFunction](bnnsactivationfunction/clamp.md)
  An activation function that returns its input clamped to a specified range.
- [static var identity: BNNSActivationFunction](bnnsactivationfunction/identity.md)
  An activation function that returns its input.
- [static var integerLinearSaturate: BNNSActivationFunction](bnnsactivationfunction/integerlinearsaturate.md)
  An activation function that returns an arithmetic shift, preserving sign.
- [static var integerLinearSaturatePerChannel: BNNSActivationFunction](bnnsactivationfunction/integerlinearsaturateperchannel.md)
  An activation function that returns an arithmetic shift, preserving sign for each channel.
- [static var leakyRectifiedLinear: BNNSActivationFunction](bnnsactivationfunction/leakyrectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns its input multiplied by a specified value.
- [static var linear: BNNSActivationFunction](bnnsactivationfunction/linear.md)
  An activation function that returns its input multiplied by a specified value.
- [static var rectifiedLinear: BNNSActivationFunction](bnnsactivationfunction/rectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns zero.
- [static var scaledTanh: BNNSActivationFunction](bnnsactivationfunction/scaledtanh.md)
  An activation function that returns the scaled hyperbolic tangent of its input.
- [static var sigmoid: BNNSActivationFunction](bnnsactivationfunction/sigmoid.md)
  An activation function that returns the sigmoid function of its input.
- [static var tanh: BNNSActivationFunction](bnnsactivationfunction/tanh.md)
  An activation function that returns the hyperbolic tangent of its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/softmax)*