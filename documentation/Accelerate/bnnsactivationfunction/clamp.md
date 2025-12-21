# clamp

**Framework**: Accelerate  
**Kind**: property

An activation function that returns its input clamped to a specified range.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst ?+
- macOS 10.13+
- tvOS 11.0+
- visionOS ?+
- watchOS 4.0+

## Declaration

```swift
static var clamp: BNNSActivationFunction { get }
```

#### Discussion

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

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://docs-assets.developer.apple.com/published/beed2d6163b4fc226d65d1ff6fc3e383/media-3401553%402x.png)

## See Also

- [static var abs: BNNSActivationFunction](bnnsactivationfunction/abs.md)
  An activation function that returns the absolute value of its input.
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
- [static var softmax: BNNSActivationFunction](bnnsactivationfunction/softmax.md)
  An activation function that returns the softmax function of its input.
- [static var tanh: BNNSActivationFunction](bnnsactivationfunction/tanh.md)
  An activation function that returns the hyperbolic tangent of its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/clamp)*