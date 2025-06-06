# MLCTensorParameter

**Framework**: ML Compute  
**Kind**: class

A tensor parameter object.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCTensorParameter
```

#### Overview

Use a tensor parameter to describe input tensors that the optimizer updates during training.

## Topics

### Creating Tensor Parameters
- [convenience init(tensor: MLCTensor)](mlctensorparameter/init(tensor:).md)
  Creates a tensor parameter with the tensor you specify.
- [convenience init(tensor: MLCTensor, optimizerData: [MLCTensorData]?)](mlctensorparameter/init(tensor:optimizerdata:).md)
  Creates a tensor parameter with the tensor and optimizer data you specify.
### Inspecting Tensor Parameters
- [var tensor: MLCTensor](mlctensorparameter/tensor.md)
  The underlying tensor.
- [var isUpdatable: Bool](mlctensorparameter/isupdatable.md)
  A Boolean that indicates whether this tensor parameter is updatable.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(graphObjects: [MLCGraph], lossLayer: MLCLayer?, optimizer: MLCOptimizer?)](mlctraininggraph/init(graphobjects:losslayer:optimizer:).md)
  Creates a training graph with the layers from the graph objects, loss layer, and optimizer you specify.
- [Optimizers](optimizers.md)
  Create an optimizer to use with the training graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensorparameter)*