# MLCTensorParameter

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A tensor parameter object.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCTensorParameter
```

```objc
@interface MLCTensorParameter : NSObject
```

## Overview

Use a tensor parameter to describe input tensors that the optimizer updates during training.

## Topics

### Creating Tensor Parameters
- [convenience init(tensor: MLCTensor)](./mlctensorparameter/init%28tensor%29.md)
  Creates a tensor parameter with the tensor you specify.
- [convenience init(tensor: MLCTensor, optimizerData: [MLCTensorData]?)](./mlctensorparameter/init%28tensor,optimizerdata%29.md)
  Creates a tensor parameter with the tensor and optimizer data you specify.
### Inspecting Tensor Parameters
- [var tensor: MLCTensor](./mlctensorparameter/tensor.md)
  The underlying tensor.
- [var isUpdatable: Bool](./mlctensorparameter/isupdatable.md)
  A Boolean that indicates whether this tensor parameter is updatable.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Training Graphs
- [convenience init(graphObjects: [MLCGraph], lossLayer: MLCLayer?, optimizer: MLCOptimizer?)](./mlctraininggraph/init%28graphobjects,losslayer,optimizer%29.md)
  Creates a training graph with the layers from the graph objects, loss layer, and optimizer you specify.
- [Optimizers](./optimizers.md)
  Create an optimizer to use with the training graph.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensorparameter)*