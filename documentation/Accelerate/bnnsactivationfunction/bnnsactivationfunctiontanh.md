# BNNSActivationFunctionTanh

**Framework**: Accelerate  
**Kind**: case  
**Role**: Enumeration Case

An activation function that returns the hyperbolic tangent of its input.

**Availability**:
- iOS 10.0+
- iPadOS 10.0+
- Mac Catalyst 13.1+
- macOS 10.12+
- tvOS 10.0+
- visionOS 1.0+
- watchOS 3.0+

## Declaration

```c
BNNSActivationFunctionTanh
```

## Discussion

This constant defines an activation function that returns values using the following operation:

```c
tanh(x)
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis.](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3401550@2x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctiontanh)*