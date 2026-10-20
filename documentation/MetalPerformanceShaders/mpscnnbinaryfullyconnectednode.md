# MPSCNNBinaryFullyConnectedNode

**Framework**: Metal Performance Shaders  
**Kind**: class  
**Role**: Class

A representation of a fully connected convolution layer with binary weights and optionally binarized input image.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.0+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+

## Declaration

```swift
class MPSCNNBinaryFullyConnectedNode
```

```objc
@interface MPSCNNBinaryFullyConnectedNode : MPSCNNBinaryConvolutionNode
```

## Topics

### Initializers
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource, scaleValue: Float, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./mpscnnbinaryfullyconnectednode/init%28source,weights,scalevalue,type,flags%29.md)
- [protocol MPSCNNConvolutionDataSource](./mpscnnconvolutiondatasource.md)
  The protocol that provides convolution filter weights and bias terms.
- [init(source: MPSNNImageNode, weights: any MPSCNNConvolutionDataSource, outputBiasTerms: UnsafePointer<Float>?, outputScaleTerms: UnsafePointer<Float>?, inputBiasTerms: UnsafePointer<Float>?, inputScaleTerms: UnsafePointer<Float>?, type: MPSCNNBinaryConvolutionType, flags: MPSCNNBinaryConvolutionFlags)](./mpscnnbinaryfullyconnectednode/init%28source,weights,outputbiasterms,outputscaleterms,inputbiasterms,inputscaleterms,type,flags%29.md)

## Relationships

### Inherits From
- [MPSCNNBinaryConvolutionNode](./mpscnnbinaryconvolutionnode.md)
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
- [class MPSCNNFullyConnectedNode](./mpscnnfullyconnectednode.md)
  A representation of a fully connected convolution layer, also known as an inner product layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/metalperformanceshaders/mpscnnbinaryfullyconnectednode)*