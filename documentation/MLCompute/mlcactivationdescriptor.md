# MLCActivationDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create an activation layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCActivationDescriptor
```

#### Overview

The framework provides the following activation descriptor initializers to create the associated descriptors:

## Topics

### Creating Activation Descriptors
- [convenience init?(type: MLCActivationType)](mlcactivationdescriptor/init(type:).md)
  Creates an activation descriptor with the activation type you specify.
- [convenience init?(type: MLCActivationType, a: Float)](mlcactivationdescriptor/init(type:a:).md)
  Creates an activation descriptor with the activation type and parameter a that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float)](mlcactivationdescriptor/init(type:a:b:).md)
  Creates an activation descriptor with the activation type and parameters a and b that you specify.
- [convenience init?(type: MLCActivationType, a: Float, b: Float, c: Float)](mlcactivationdescriptor/init(type:a:b:c:).md)
  Creates an activation descriptor with the activation type and parameters a, b, and c that you specify.
- [enum MLCActivationType](mlcactivationtype.md)
  An activation type that you specify for an activation descriptor.
### Inspecting Activation Descriptors
- [var activationType: MLCActivationType](mlcactivationdescriptor/activationtype.md)
  The type of activation function.
- [var a: Float](mlcactivationdescriptor/a.md)
  The parameter a to the activation function.
- [var b: Float](mlcactivationdescriptor/b.md)
  The parameter b to the activation function.
- [var c: Float](mlcactivationdescriptor/c.md)
  The parameter c to the activation function.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(descriptor: MLCActivationDescriptor)](mlcactivationlayer/init(descriptor:).md)
  Creates an activation layer with the descriptor you specify.
- [Preconfigured Activation Layers](preconfigured-activation-layers.md)
  Obtain a preconfigured activation layer with common behavior.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcactivationdescriptor)*