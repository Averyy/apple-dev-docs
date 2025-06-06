# MLCActivationType.hardSwish

**Framework**: ML Compute  
**Kind**: case

An activation type that implements the hard swish activation function.

**Availability**:
- iOS 14.5+
- iPadOS 14.5+
- Mac Catalyst 14.5+
- macOS 11.3+
- tvOS 14.5+

## Declaration

```swift
case hardSwish
```

#### Discussion

This activation type implements the following function:

`f(x) = 0, if x <= -3`

`f(x) = x, if x >= +3`

`f(x) = x * (x + 3)/6`

## See Also

- [MLCActivationType.absolute](mlcactivationtype/absolute.md)
  An activation type that implements the absolute activation function.
- [MLCActivationType.celu](mlcactivationtype/celu.md)
  An activation type that implements the CELU activation function.
- [MLCActivationType.clamp](mlcactivationtype/clamp.md)
  An activation type that implements the clamp activation function.
- [MLCActivationType.elu](mlcactivationtype/elu.md)
  An activation type that implements the exponential linear unit activation function.
- [MLCActivationType.gelu](mlcactivationtype/gelu.md)
  An activation type that implements the gaussian error linear unit activation function.
- [MLCActivationType.hardShrink](mlcactivationtype/hardshrink.md)
  An activation type that implements the hard shrink activation function.
- [MLCActivationType.hardSigmoid](mlcactivationtype/hardsigmoid.md)
  An activation type that implements the hard sigmoid activation function.
- [MLCActivationType.linear](mlcactivationtype/linear.md)
  An activation type that implements the linear activation function.
- [MLCActivationType.logSigmoid](mlcactivationtype/logsigmoid.md)
  An activation type that implements the log sigmoid activation function.
- [MLCActivationType.none](mlcactivationtype/none.md)
  An activation type that implements the identity function.
- [MLCActivationType.relu](mlcactivationtype/relu.md)
  An activation type that implements the rectified linear unit activation function.
- [MLCActivationType.relun](mlcactivationtype/relun.md)
  An activation type that implements the ReLUN activation function.
- [MLCActivationType.selu](mlcactivationtype/selu.md)
  An activation type that implements the scaled exponential linear unit activation function.
- [MLCActivationType.sigmoid](mlcactivationtype/sigmoid.md)
  An activation type that implements the sigmoid activation function.
- [MLCActivationType.softPlus](mlcactivationtype/softplus.md)
  An activation type that implements the soft plus activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationtype/hardswish)*