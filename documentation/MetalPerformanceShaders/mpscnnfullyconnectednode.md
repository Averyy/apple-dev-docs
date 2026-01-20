# MPSCNNFullyConnectedNode

**Framework**: Metal Performance Shaders  
**Kind**: class

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

## Topics

### Initializers
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource)](mpscnnfullyconnectednode/init(source:weights:).md)

## Relationships

### Inherits From
- [MPSCNNConvolutionNode](mpscnnconvolutionnode.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [MPSNNTrainableNode](mpsnntrainablenode.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MPSCNNBinaryFullyConnectedNode](mpscnnbinaryfullyconnectednode.md)
  A representation of a fully connected convolution layer with binary weights and optionally binarized input image.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnfullyconnectednode)*