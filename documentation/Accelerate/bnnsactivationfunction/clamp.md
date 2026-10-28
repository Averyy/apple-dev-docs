# clamp

**Framework**: Accelerate  
**Kind**: property  
**Role**: Type Property

An activation function that returns its input clamped to a specified range.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 11.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS
- watchOS 4.0+

> **Deprecated**: Use the BNNSGraph API instead.

## Declaration

```swift
static var clamp: BNNSActivationFunction { get }
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

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3401553@2x.png)

## See Also

### Activation Functions
- [static var abs: BNNSActivationFunction](./abs.md)
  An activation function that returns the absolute value of its input.
- [static var identity: BNNSActivationFunction](./identity.md)
  An activation function that returns its input.
- [static var integerLinearSaturate: BNNSActivationFunction](./integerlinearsaturate.md)
  An activation function that returns an arithmetic shift, preserving sign.
- [static var integerLinearSaturatePerChannel: BNNSActivationFunction](./integerlinearsaturateperchannel.md)
  An activation function that returns an arithmetic shift, preserving sign for each channel.
- [static var leakyRectifiedLinear: BNNSActivationFunction](./leakyrectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns its input multiplied by a specified value.
- [static var linear: BNNSActivationFunction](./linear.md)
  An activation function that returns its input multiplied by a specified value.
- [static var rectifiedLinear: BNNSActivationFunction](./rectifiedlinear.md)
  An activation function that returns its input when that is greater than or equal to zero, otherwise it returns zero.
- [static var scaledTanh: BNNSActivationFunction](./scaledtanh.md)
  An activation function that returns the scaled hyperbolic tangent of its input.
- [static var sigmoid: BNNSActivationFunction](./sigmoid.md)
  An activation function that returns the sigmoid function of its input.
- [static var softmax: BNNSActivationFunction](./softmax.md)
  An activation function that returns the softmax function of its input.
- [static var tanh: BNNSActivationFunction](./tanh.md)
  An activation function that returns the hyperbolic tangent of its input.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/clamp)*