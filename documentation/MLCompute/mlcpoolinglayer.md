# MLCPoolingLayer

**Framework**: ML Compute  
**Kind**: class

A layer that summarizes the average presence of a feature.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCPoolingLayer
```

## Topics

### Creating Pooling Layers
- [convenience init(descriptor: MLCPoolingDescriptor)](mlcpoolinglayer/init(descriptor:).md)
  Creates a pooling layer with the descriptor you specify.
- [class MLCPoolingDescriptor](mlcpoolingdescriptor.md)
  A configuration object you use to create a pooling layer.
- [enum MLCPoolingType](mlcpoolingtype-wb8j.md)
  A pooling function type for a pooling layer.
### Inspecting Pooling Layers
- [var descriptor: MLCPoolingDescriptor](mlcpoolinglayer/descriptor.md)
  The configuration object you use to create the pooling layer.

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
- [class MLCUpsampleLayer](mlcupsamplelayer.md)
  A layer that applies upsampling with the shape you specify.
- [class MLCEmbeddingLayer](mlcembeddinglayer.md)
  A layer that stores a word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolinglayer)*