# MLCEmbeddingLayer

**Framework**: ML Compute  
**Kind**: class

A layer that stores a word embedding.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCEmbeddingLayer
```

## Topics

### Creating Embedding Layers
- [convenience init(descriptor: MLCEmbeddingDescriptor, weights: MLCTensor)](mlcembeddinglayer/init(descriptor:weights:).md)
  Creates an embedding layer with the descriptor and word embedding weights tensor you specify.
- [class MLCEmbeddingDescriptor](mlcembeddingdescriptor.md)
  A configuration object you use to create an embedding layer.
### Inspecting Embedding Layers
- [var descriptor: MLCEmbeddingDescriptor](mlcembeddinglayer/descriptor.md)
  The configuration object you use to create the embedding layer.
- [var weights: MLCTensor](mlcembeddinglayer/weights.md)
  The weights tensor that contains the word embedding.
- [var weightsParameter: MLCTensorParameter](mlcembeddinglayer/weightsparameter.md)
  The tensor parameter that describes the weights for the optimizer update.

## Relationships

### Inherits From
- [MLCLayer](mlclayer.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [class MLCConvolutionLayer](mlcconvolutionlayer.md)
  A layer that applies a convolution over a signal.
- [class MLCLSTMLayer](mlclstmlayer.md)
  A layer that represents long short-term memory (LSTM) networks.
- [class MLCPoolingLayer](mlcpoolinglayer.md)
  A layer that summarizes the average presence of a feature.
- [class MLCUpsampleLayer](mlcupsamplelayer.md)
  A layer that applies upsampling with the shape you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddinglayer)*