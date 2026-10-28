# selu

**Framework**: ML Compute  
**Kind**: property  
**Role**: Type Property

Creates an instance of a SELU activation layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class var selu: MLCActivationLayer { get }
```

```objc
@property (class, nonatomic, readonly) MLCActivationLayer * seluLayer;
```

## Discussion

This factory creates an activation descriptor using [`init(type:)`](../mlcactivationdescriptor/init%28type%29.md), where `type =` [`MLCActivationType.selu`](../mlcactivationtype/selu.md), and passes that descriptor to [`init(descriptor:)`](./init%28descriptor%29.md).

## See Also

### Factory Properties
- [class var absolute: MLCActivationLayer](./absolute.md)
  Creates an instance of an absolute activation layer.
- [class var celu: MLCActivationLayer](./celu.md)
  Creates an instance of a CELU activation layer.
- [class var elu: MLCActivationLayer](./elu.md)
  Creates an instance of a parametric ELU activation layer.
- [class var gelu: MLCActivationLayer](./gelu.md)
  Creates an instance of a GELU activation layer.
- [class var hardShrink: MLCActivationLayer](./hardshrink.md)
  Creates an instance of a hard shrink activation layer.
- [class var hardSigmoid: MLCActivationLayer](./hardsigmoid.md)
  Creates an instance of a hard sigmoid activation layer.
- [class var hardSwish: MLCActivationLayer](./hardswish.md)
  Creates an instance of a hard swish activation layer.
- [class var leakyReLU: MLCActivationLayer](./leakyrelu.md)
  Creates an instance of a leaky ReLU activation layer.
- [class var logSigmoid: MLCActivationLayer](./logsigmoid.md)
  Creates an instance of a log sigmoid activation layer.
- [class var relu: MLCActivationLayer](./relu.md)
  Creates an instance of a ReLU activation layer.
- [class var relu6: MLCActivationLayer](./relu6.md)
  Creates an instance of a ReLU6 activation layer.
- [class var sigmoid: MLCActivationLayer](./sigmoid.md)
  Creates an instance of a sigmoid activation layer.
- [class var softPlus: MLCActivationLayer](./softplus.md)
  Creates an instance of a parametric soft plus activation layer.
- [class var softShrink: MLCActivationLayer](./softshrink.md)
  Creates an instance of a soft shrink activation layer.
- [class var softSign: MLCActivationLayer](./softsign.md)
  Creates an instance of a parametric soft sign activation layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationlayer/selu)*