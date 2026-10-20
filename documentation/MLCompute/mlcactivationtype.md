# MLCActivationType

**Framework**: ML Compute  
**Kind**: enum  
**Role**: Enumeration

An activation type that you specify for an activation descriptor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
enum MLCActivationType
```

```c
enum MLCActivationType : int32_t;
```

## Topics

### Enumeration Cases
- [MLCActivationType.absolute](./mlcactivationtype/absolute.md)
  An activation type that implements the absolute activation function.
- [MLCActivationType.celu](./mlcactivationtype/celu.md)
  An activation type that implements the CELU activation function.
- [MLCActivationType.clamp](./mlcactivationtype/clamp.md)
  An activation type that implements the clamp activation function.
- [MLCActivationType.elu](./mlcactivationtype/elu.md)
  An activation type that implements the exponential linear unit activation function.
- [MLCActivationType.gelu](./mlcactivationtype/gelu.md)
  An activation type that implements the gaussian error linear unit activation function.
- [MLCActivationType.hardShrink](./mlcactivationtype/hardshrink.md)
  An activation type that implements the hard shrink activation function.
- [MLCActivationType.hardSigmoid](./mlcactivationtype/hardsigmoid.md)
  An activation type that implements the hard sigmoid activation function.
- [MLCActivationType.hardSwish](./mlcactivationtype/hardswish.md)
  An activation type that implements the hard swish activation function.
- [MLCActivationType.linear](./mlcactivationtype/linear.md)
  An activation type that implements the linear activation function.
- [MLCActivationType.logSigmoid](./mlcactivationtype/logsigmoid.md)
  An activation type that implements the log sigmoid activation function.
- [MLCActivationType.none](./mlcactivationtype/none.md)
  An activation type that implements the identity function.
- [MLCActivationType.relu](./mlcactivationtype/relu.md)
  An activation type that implements the rectified linear unit activation function.
- [MLCActivationType.relun](./mlcactivationtype/relun.md)
  An activation type that implements the ReLUN activation function.
- [MLCActivationType.selu](./mlcactivationtype/selu.md)
  An activation type that implements the scaled exponential linear unit activation function.
- [MLCActivationType.sigmoid](./mlcactivationtype/sigmoid.md)
  An activation type that implements the sigmoid activation function.
- [MLCActivationType.softPlus](./mlcactivationtype/softplus.md)
  An activation type that implements the soft plus activation function.
- [MLCActivationType.softShrink](./mlcactivationtype/softshrink.md)
  An activation type that implements the soft shrink activation function.
- [MLCActivationType.softSign](./mlcactivationtype/softsign.md)
  An activation type that implements the parametric soft sign activation function.
- [MLCActivationType.tanh](./mlcactivationtype/tanh.md)
  An activation type that implements the hyperbolic tangent activation function.
- [MLCActivationType.tanhShrink](./mlcactivationtype/tanhshrink.md)
  An activation type that implements the hyperbolic tangent shrink activation function.
- [MLCActivationType.threshold](./mlcactivationtype/threshold.md)
  An activation type that implements the threshold activation function.
- [var debugDescription: String](./mlcactivationtype/debugdescription.md)
  A textual description of the activation type, suitable for debugging.
### Initializers
- [init?(rawValue: Int32)](./mlcactivationtype/init%28rawvalue%29.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)
- [SendableMetatype](../Swift/sendablemetatype.md)

## See Also

### Creating Activation Descriptors
- [convenience init?(type: MLCActivationType)](./mlcactivationdescriptor/init%28type%29.md)
  Creates an activation descriptor with the activation type you specify.
- [convenience init?(type: MLCActivationType, a: Float)](./mlcactivationdescriptor/init%28type,a%29.md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float)](./mlcactivationdescriptor/init%28type,a,b%29.md)
  Creates an activation descriptor with the activation type and parameters a and b that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float, c: Float)](./mlcactivationdescriptor/init%28type,a,b,c%29.md)
  Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationtype)*