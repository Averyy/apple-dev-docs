# MLCConvolutionLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that applies a convolution over a signal.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCConvolutionLayer
```

```objc
@interface MLCConvolutionLayer : MLCLayer
```

## Topics

### Creating Convolution Layers
- [convenience init?(weights: MLCTensor, biases: MLCTensor?, descriptor: MLCConvolutionDescriptor)](./mlcconvolutionlayer/init%28weights,biases,descriptor%29.md)
  Creates a convolution layer with the weights, biases, and descriptor you specify.
- [class MLCConvolutionDescriptor](./mlcconvolutiondescriptor.md)
  A configuration object you use to create a convolution or fully connected layer.
### Inspecting Convolution Layers
- [var descriptor: MLCConvolutionDescriptor](./mlcconvolutionlayer/descriptor.md)
  The configuration object you use to create the convolution layer.
- [var weights: MLCTensor](./mlcconvolutionlayer/weights.md)
  The weights tensor you use for the convolution layer.
- [var biases: MLCTensor?](./mlcconvolutionlayer/biases.md)
  The biases tensor you use for the convolution layer.
- [var weightsParameter: MLCTensorParameter](./mlcconvolutionlayer/weightsparameter.md)
  The weights tensor parameter you use for optimizer updates.
- [var biasesParameter: MLCTensorParameter?](./mlcconvolutionlayer/biasesparameter.md)
  The biases tensor parameter you use for optimizer updates.

## Relationships

### Inherits From
- [MLCLayer](./mlclayer.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Convolution and Recurrent Layers
- [class MLCLSTMLayer](./mlclstmlayer.md)
  A layer that represents long short-term memory (LSTM) networks.
- [class MLCPoolingLayer](./mlcpoolinglayer.md)
  A layer that summarizes the average presence of a feature.
- [class MLCUpsampleLayer](./mlcupsamplelayer.md)
  A layer that applies upsampling with the shape you specify.
- [class MLCEmbeddingLayer](./mlcembeddinglayer.md)
  A layer that stores a word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcconvolutionlayer)*