# MPSCNNFullyConnectedNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a fully connected convolution layer, also known as an inner product layer.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNFullyConnectedNode
```

```objc
@interface MPSCNNFullyConnectedNode : MPSCNNConvolutionNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource)](./mpscnnfullyconnectednode/init%28source,weights%29.md)
### Type Methods
- [+ nodeWithSource:weights:](./mpscnnfullyconnectednode/nodewithsource_weights_.md)

## Relationships

### Inherits From
- [MPSCNNConvolutionNode](./mpscnnconvolutionnode.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [MPSNNTrainableNode](./mpsnntrainablenode.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Fully Connected Layer Nodes
- [class MPSCNNBinaryFullyConnectedNode](./mpscnnbinaryfullyconnectednode.md)
  A representation of a fully connected convolution layer with binary weights and optionally binarized input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnectednode)*