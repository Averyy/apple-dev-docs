# leakyRectifiedLinear

**Framework**: Accelerate  
**Kind**: property

An activation function that returns its input when that is greater than or equal to zero, otherwise it returns its input multiplied by a specified value.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- visionOS ?+
- watchOS 3.0+

## Declaration

```swift
static var leakyRectifiedLinear: BNNSActivationFunction { get }
```

#### Discussion

This constant defines an activation function that returns values using the following operation:

```c
alpha*x if x<0, and x if x>=0
```

Use `alpha` to specify the multiplier for values less than zero range:

```swift
var activation = BNNSActivation(function: .leakyRectifiedLinear, 
                                alpha: 0.25)
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://docs-assets.developer.apple.com/published/a1f886520463acacd8f05c6f39ab052b/media-3401559%402x.png)

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
- [static var linear: BNNSActivationFunction](bnnsactivationfunction/linear.md)
  An activation function that returns its input multiplied by a specified value.
- [static var rectifiedLinear: BNNSActivationFunction](bnnsactivationfunction/rectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns zero.
- [static var scaledTanh: BNNSActivationFunction](bnnsactivationfunction/scaledtanh.md)
  An activation function that returns the scaled hyperbolic tangent of its input.
- [static var sigmoid: BNNSActivationFunction](bnnsactivationfunction/sigmoid.md)
  An activation function that returns the sigmoid function of its input.
- [static var softmax: BNNSActivationFunction](bnnsactivationfunction/softmax.md)
  An activation function that returns the softmax function of its input.
- [static var tanh: BNNSActivationFunction](bnnsactivationfunction/tanh.md)
  An activation function that returns the hyperbolic tangent of its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/leakyrectifiedlinear)*