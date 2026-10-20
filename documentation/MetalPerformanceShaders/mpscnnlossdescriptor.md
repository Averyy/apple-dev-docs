# MPSCNNLossDescriptor

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

An object that specifies properties used by a loss kernel.

**Availability**:
- iOS 11.3+
- iPadOS 11.3+
- Mac Catalyst 13.0+
- macOS 10.13.4+
- tvOS 11.3+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNLossDescriptor
```

```objc
@interface MPSCNNLossDescriptor : NSObject
```

## Topics

### Initializers
- [init(type: MPSCNNLossType, reductionType: MPSCNNReductionType)](./mpscnnlossdescriptor/init%28type,reductiontype%29.md)
### Instance Properties
- [var delta: Float](./mpscnnlossdescriptor/delta.md)
- [var epsilon: Float](./mpscnnlossdescriptor/epsilon.md)
- [var labelSmoothing: Float](./mpscnnlossdescriptor/labelsmoothing.md)
- [var lossType: MPSCNNLossType](./mpscnnlossdescriptor/losstype.md)
- [var numberOfClasses: Int](./mpscnnlossdescriptor/numberofclasses.md)
- [var reduceAcrossBatch: Bool](./mpscnnlossdescriptor/reduceacrossbatch.md)
- [var reductionType: MPSCNNReductionType](./mpscnnlossdescriptor/reductiontype.md)
- [var weight: Float](./mpscnnlossdescriptor/weight.md)

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

### Loss Layers
- [class MPSCNNLoss](./mpscnnloss.md)
  A kernel that computes the loss and loss gradient between specified predictions and labels.
- [class MPSCNNLossDataDescriptor](./mpscnnlossdatadescriptor.md)
  An object that specifies properties used by a loss data descriptor.
- [class MPSCNNLossLabels](./mpscnnlosslabels.md)
  A class that stores the per-element weight buffer used by loss and gradient loss kernels.
- [class MPSCNNYOLOLoss](./mpscnnyololoss.md)
  A kernel that computes the YOLO loss and loss gradient between specified predictions and labels.
- [class MPSCNNYOLOLossDescriptor](./mpscnnyololossdescriptor.md)
  An object that specifies properties used by a YOLO loss kernel.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnlossdescriptor)*