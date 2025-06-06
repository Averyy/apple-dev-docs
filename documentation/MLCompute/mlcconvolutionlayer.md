# MLCConvolutionLayer

**Framework**: ML Compute  
**Kind**: class

A layer that applies a convolution over a signal.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCConvolutionLayer
```

## Topics

### Creating Convolution Layers
- [convenience init?(weights: MLCTensor, biases: MLCTensor?, descriptor: MLCConvolutionDescriptor)](mlcconvolutionlayer/init(weights:biases:descriptor:).md)
  Creates a convolution layer with the weights, biases, and descriptor you specify.
- [class MLCConvolutionDescriptor](mlcconvolutiondescriptor.md)
  A configuration object you use to create a convolution or fully connected layer.
### Inspecting Convolution Layers
- [var descriptor: MLCConvolutionDescriptor](mlcconvolutionlayer/descriptor.md)
  The configuration object you use to create the convolution layer.
- [var weights: MLCTensor](mlcconvolutionlayer/weights.md)
  The weights tensor you use for the convolution layer.
- [var biases: MLCTensor?](mlcconvolutionlayer/biases.md)
  The biases tensor you use for the convolution layer.
- [var weightsParameter: MLCTensorParameter](mlcconvolutionlayer/weightsparameter.md)
  The weights tensor parameter you use for optimizer updates.
- [var biasesParameter: MLCTensorParameter?](mlcconvolutionlayer/biasesparameter.md)
  The biases tensor parameter you use for optimizer updates.

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

- [class MLCLSTMLayer](mlclstmlayer.md)
  A layer that represents long short-term memory (LSTM) networks.
- [class MLCPoolingLayer](mlcpoolinglayer.md)
  A layer that summarizes the average presence of a feature.
- [class MLCUpsampleLayer](mlcupsamplelayer.md)
  A layer that applies upsampling with the shape you specify.
- [class MLCEmbeddingLayer](mlcembeddinglayer.md)
  A layer that stores a word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutionlayer)*