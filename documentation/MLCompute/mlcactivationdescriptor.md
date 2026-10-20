# MLCActivationDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A configuration object you use to create an activation layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCActivationDescriptor
```

```objc
@interface MLCActivationDescriptor : NSObject
```

#### Overview

The framework provides the following activation descriptor initializers to create the associated descriptors:

- **[`init(type:)`](./mlcactivationdescriptor/init%28type%29.md)**: Absolute, GELU, Identity, LogSigmoid, Parametric Soft Sign, SELU, Sigmoid, TanhShrink
- **[`init(type:a:)`](./mlcactivationdescriptor/init%28type,a%29.md)**: CELU, HardShrink, Parametric ELU, ReLU, SoftShrink
- **[`init(type:a:b:)`](./mlcactivationdescriptor/init%28type,a,b%29.md)**: Hard Sigmoid, Hyperbolic tangent (TanH), Linear, Parametric Soft Plus, ReLUN, Threshold

## Topics

### Creating Activation Descriptors
- [convenience init?(type: MLCActivationType)](./mlcactivationdescriptor/init%28type%29.md)
  Creates an activation descriptor with the activation type you specify.
- [convenience init?(type: MLCActivationType, a: Float)](./mlcactivationdescriptor/init%28type,a%29.md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float)](./mlcactivationdescriptor/init%28type,a,b%29.md)
  Creates an activation descriptor with the activation type and parameters a and b that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float, c: Float)](./mlcactivationdescriptor/init%28type,a,b,c%29.md)
  Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.
- [enum MLCActivationType](./mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.
### Inspecting Activation Descriptors
- [var activationType: MLCActivationType](./mlcactivationdescriptor/activationtype.md)
  The type of activation function.
- [var a: Float](./mlcactivationdescriptor/a.md)
  The parameter a to the activation function.
- [var b: Float](./mlcactivationdescriptor/b.md)
  The parameter b to the activation function.
- [var c: Float](./mlcactivationdescriptor/c.md)
  The parameter c to the activation function.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Activation Layers
- [convenience init(descriptor: MLCActivationDescriptor)](./mlcactivationlayer/init%28descriptor%29.md)
  Creates an activation layer with the descriptor you specify.
- [Preconfigured Activation Layers](./preconfigured-activation-layers.md)
  Obtain a preconfigured activation layer with common behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor)*