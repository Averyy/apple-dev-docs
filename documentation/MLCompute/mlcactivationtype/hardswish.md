# MLCActivationType.hardSwish

**Framework**: ML Compute  
**Kind**: case  
**Role**: Case

An activation type that implements the hard swish activation function.

**Availability**:
- iOS 14.5+ - Deprecated in 17.4
- iPadOS 14.5+ - Deprecated in 17.4
- Mac Catalyst 14.5+ - Deprecated in 17.4
- macOS 11.3+ - Deprecated in 14.3
- tvOS 14.5+ - Deprecated in 17.4

## Declaration

```swift
case hardSwish
```

```c
MLCActivationTypeHardSwish
```

#### Discussion

This activation type implements the following function:

`f(x) = 0, if x <= -3`

`f(x) = x, if x >= +3`

`f(x) = x * (x + 3)/6`

## See Also

### Enumeration Cases
- [MLCActivationType.absolute](./absolute.md)
  An activation type that implements the absolute activation function.
- [MLCActivationType.celu](./celu.md)
  An activation type that implements the CELU activation function.
- [MLCActivationType.clamp](./clamp.md)
  An activation type that implements the clamp activation function.
- [MLCActivationType.elu](./elu.md)
  An activation type that implements the exponential linear unit activation function.
- [MLCActivationType.gelu](./gelu.md)
  An activation type that implements the gaussian error linear unit activation function.
- [MLCActivationType.hardShrink](./hardshrink.md)
  An activation type that implements the hard shrink activation function.
- [MLCActivationType.hardSigmoid](./hardsigmoid.md)
  An activation type that implements the hard sigmoid activation function.
- [MLCActivationType.linear](./linear.md)
  An activation type that implements the linear activation function.
- [MLCActivationType.logSigmoid](./logsigmoid.md)
  An activation type that implements the log sigmoid activation function.
- [MLCActivationType.none](./none.md)
  An activation type that implements the identity function.
- [MLCActivationType.relu](./relu.md)
  An activation type that implements the rectified linear unit activation function.
- [MLCActivationType.relun](./relun.md)
  An activation type that implements the ReLUN activation function.
- [MLCActivationType.selu](./selu.md)
  An activation type that implements the scaled exponential linear unit activation function.
- [MLCActivationType.sigmoid](./sigmoid.md)
  An activation type that implements the sigmoid activation function.
- [MLCActivationType.softPlus](./softplus.md)
  An activation type that implements the soft plus activation function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationtype/hardswish)*