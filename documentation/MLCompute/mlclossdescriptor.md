# MLCLossDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A configuration object you use to create a loss layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCLossDescriptor
```

```objc
@interface MLCLossDescriptor : NSObject
```

## Topics

### Creating Loss Descriptors
- [convenience init(type: MLCLossType, reductionType: MLCReductionType)](./mlclossdescriptor/init%28type,reductiontype%29.md)
  Creates a loss descriptor with the loss function and reduction type you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float)](./mlclossdescriptor/init%28type,reductiontype,weight%29.md)
  Creates a loss descriptor with the loss function, reduction type, and weight you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int)](./mlclossdescriptor/init%28type,reductiontype,weight,labelsmoothing,classcount%29.md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes you specify.
- [convenience init(type: MLCLossType, reductionType: MLCReductionType, weight: Float, labelSmoothing: Float, classCount: Int, epsilon: Float, delta: Float)](./mlclossdescriptor/init%28type,reductiontype,weight,labelsmoothing,classcount,epsilon,delta%29.md)
  Creates a loss descriptor with the loss function, reduction type, weight, label smoothing, and number of classes, epsilon, and delta that you specify.
### Inspecting Loss Descriptors
- [var lossType: MLCLossType](./mlclossdescriptor/losstype.md)
  The loss function type.
- [var reductionType: MLCReductionType](./mlclossdescriptor/reductiontype.md)
  The reduction operation performed by the loss function.
- [var weight: Float](./mlclossdescriptor/weight.md)
  The scale factor you apply to each element of a result.
- [var labelSmoothing: Float](./mlclossdescriptor/labelsmoothing.md)
  The value for label smoothing.
- [var classCount: Int](./mlclossdescriptor/classcount.md)
  The number of classes.
- [var epsilon: Float](./mlclossdescriptor/epsilon.md)
  The epsilon value.
- [var delta: Float](./mlclossdescriptor/delta.md)
  The delta value.

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

### Creating Loss Layers with Descriptors
- [convenience init(descriptor: MLCLossDescriptor)](./mlclosslayer/init%28descriptor%29.md)
  Creates a loss layer with the descriptor you specify.
- [convenience init(descriptor: MLCLossDescriptor, weights: MLCTensor)](./mlclosslayer/init%28descriptor,weights%29.md)
  Creates a loss layer with the descriptor and weights you specify.
- [enum MLCLossType](./mlclosstype.md)
  A loss function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlclossdescriptor)*