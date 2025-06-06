# sigmoid

**Framework**: Accelerate  
**Kind**: property

An activation function that returns the sigmoid function of its input.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst ?+
- macOS 10.12+
- tvOS 10.0+
- watchOS 3.0+
- Unknown ?+ - Deprecated
- visionOS ?+

## Declaration

```swift
static var sigmoid: BNNSActivationFunction { get }
```

## Mentions

- [Using Long Short-Term Memory Layers (LSTM)](using-long-short-term-memory-layers-lstm.md)

#### Discussion

This constant defines an activation function that returns values using the logistic function:

```c
1.0 / (1.0 + exp(-x))
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://docs-assets.developer.apple.com/published/9d01fae6d0725bbdc18882310bd0832a/media-3394561%402x.png)

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
- [static var softmax: BNNSActivationFunction](bnnsactivationfunction/softmax.md)
  An activation function that returns the softmax function of its input.
- [static var tanh: BNNSActivationFunction](bnnsactivationfunction/tanh.md)
  An activation function that returns the hyperbolic tangent of its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/sigmoid)*