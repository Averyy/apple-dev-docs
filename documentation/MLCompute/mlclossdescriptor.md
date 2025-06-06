# MLCLossDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create a loss layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCLossDescriptor
```

## Topics

### Creating Loss Descriptors
- [convenience init(type: MLCLossType, reductionType: MLCReductionType)](mlclossdescriptor/init(type:reductiontype:).md)
  Creates a loss descriptor with the loss function and reduction type you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float)](mlclossdescriptor/init(type:reductiontype:weight:).md)
  Creates a loss descriptor with the loss function, reduction type, and weight you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int)](mlclossdescriptor/init(type:reductiontype:weight:labelsmoothing:classcount:).md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int, epsilon: Float, delta: Float)](mlclossdescriptor/init(type:reductiontype:weight:labelsmoothing:classcount:epsilon:delta:).md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes, epsilon, and delta that you specify.
### Inspecting Loss Descriptors
- [var lossType: MLCLossType](mlclossdescriptor/losstype.md)
  The loss function type.
- [var reductionType: MLCReductionType](mlclossdescriptor/reductiontype.md)
  The reduction operation performed by the loss function.
- [var weight: Float](mlclossdescriptor/weight.md)
  The scale factor you apply to each element of a result.
- [var labelSmoothing: Float](mlclossdescriptor/labelsmoothing.md)
  The value for label smoothing.
- [var classCount: Int](mlclossdescriptor/classcount.md)
  The number of classes.
- [var epsilon: Float](mlclossdescriptor/epsilon.md)
  The epsilon value.
- [var delta: Float](mlclossdescriptor/delta.md)
  The delta value.

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

- [convenience init(descriptor: MLCLossDescriptor)](mlclosslayer/init(descriptor:).md)
  Creates a loss layer with the descriptor you specify.
- [convenience init(descriptor: MLCLossDescriptor, weights: MLCTensor)](mlclosslayer/init(descriptor:weights:).md)
  Creates a loss layer with the descriptor and weights you specify.
- [enum MLCLossType](mlclosstype.md)
  A loss function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor)*