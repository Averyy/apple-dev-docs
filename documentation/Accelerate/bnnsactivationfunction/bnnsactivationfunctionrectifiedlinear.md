# BNNSActivationFunctionRectifiedLinear

**Framework**: Accelerate  
**Kind**: case  
**Role**: Enumeration Case

An activation function that returns its input when that is greater than or equal to zero, otherwise it returns zero.

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
BNNSActivationFunctionRectifiedLinear
```

#### Discussion

This constant defines an activation function that returns values using the following operation:

```c
0 if x<0, and x if x>=0
```

The following illustrates the output that the activation function generates from inputs in the range `-10...10`:

![Graph that shows input values for the activation function on horizontal axis and its output values on vertical axis. ](https://developer.apple.com/tutorials/images/com.apple.accelerate/media-3394459@2x.png)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsactivationfunction/bnnsactivationfunctionrectifiedlinear)*