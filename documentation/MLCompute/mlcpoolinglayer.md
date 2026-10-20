# MLCPoolingLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that summarizes the average presence of a feature.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCPoolingLayer
```

```objc
@interface MLCPoolingLayer : MLCLayer
```

## Topics

### Creating Pooling Layers
- [convenience init(descriptor: MLCPoolingDescriptor)](./mlcpoolinglayer/init%28descriptor%29.md)
  Creates a pooling layer with the descriptor you specify.
- [class MLCPoolingDescriptor](./mlcpoolingdescriptor.md)
  A configuration object you use to create a pooling layer.
- [enum MLCPoolingType](./mlcpoolingtype-wb8j.md)
  A pooling function type for a pooling layer.
### Inspecting Pooling Layers
- [var descriptor: MLCPoolingDescriptor](./mlcpoolinglayer/descriptor.md)
  The configuration object you use to create the pooling layer.

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
- [class MLCConvolutionLayer](./mlcconvolutionlayer.md)
  A layer that applies a convolution over a signal.
- [class MLCLSTMLayer](./mlclstmlayer.md)
  A layer that represents long short-term memory (LSTM) networks.
- [class MLCUpsampleLayer](./mlcupsamplelayer.md)
  A layer that applies upsampling with the shape you specify.
- [class MLCEmbeddingLayer](./mlcembeddinglayer.md)
  A layer that stores a word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcpoolinglayer)*