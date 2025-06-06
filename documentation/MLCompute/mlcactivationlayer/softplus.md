# softPlus

**Framework**: ML Compute  
**Kind**: property

Creates an instance of a parametric soft plus activation layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class var softPlus: MLCActivationLayer { get }
```

#### Discussion

This factory creates an activation descriptor using [`init(type:a:b:)`](mlcactivationdescriptor/init(type:a:b:).md), where `type =` [`MLCActivationType.softPlus`](mlcactivationtype/softplus.md), `a = 1.0`, and `b = 1.0`, and passes that descriptor to [`init(descriptor:)`](mlcactivationlayer/init(descriptor:).md).

## See Also

- [class var absolute: MLCActivationLayer](mlcactivationlayer/absolute.md)
  Creates an instance of an absolute activation layer.
- [class var celu: MLCActivationLayer](mlcactivationlayer/celu.md)
  Creates an instance of a CELU activation layer.
- [class var elu: MLCActivationLayer](mlcactivationlayer/elu.md)
  Creates an instance of a parametric ELU activation layer.
- [class var gelu: MLCActivationLayer](mlcactivationlayer/gelu.md)
  Creates an instance of a GELU activation layer.
- [class var hardShrink: MLCActivationLayer](mlcactivationlayer/hardshrink.md)
  Creates an instance of a hard shrink activation layer.
- [class var hardSigmoid: MLCActivationLayer](mlcactivationlayer/hardsigmoid.md)
  Creates an instance of a hard sigmoid activation layer.
- [class var hardSwish: MLCActivationLayer](mlcactivationlayer/hardswish.md)
  Creates an instance of a hard swish activation layer.
- [class var leakyReLU: MLCActivationLayer](mlcactivationlayer/leakyrelu.md)
  Creates an instance of a leaky ReLU activation layer.
- [class var logSigmoid: MLCActivationLayer](mlcactivationlayer/logsigmoid.md)
  Creates an instance of a log sigmoid activation layer.
- [class var relu: MLCActivationLayer](mlcactivationlayer/relu.md)
  Creates an instance of a ReLU activation layer.
- [class var relu6: MLCActivationLayer](mlcactivationlayer/relu6.md)
  Creates an instance of a ReLU6 activation layer.
- [class var selu: MLCActivationLayer](mlcactivationlayer/selu.md)
  Creates an instance of a SELU activation layer.
- [class var sigmoid: MLCActivationLayer](mlcactivationlayer/sigmoid.md)
  Creates an instance of a sigmoid activation layer.
- [class var softShrink: MLCActivationLayer](mlcactivationlayer/softshrink.md)
  Creates an instance of a soft shrink activation layer.
- [class var softSign: MLCActivationLayer](mlcactivationlayer/softsign.md)
  Creates an instance of a parametric soft sign activation layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationlayer/softplus)*