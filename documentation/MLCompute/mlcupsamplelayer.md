# MLCUpsampleLayer

**Framework**: ML Compute  
**Kind**: class

A layer that applies upsampling with the shape you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCUpsampleLayer
```

## Topics

### Creating Upsample Layers
- [convenience init?(shape: [Int])](mlcupsamplelayer/init(shape:).md)
  Creates an upsample layer with the shape you specify.
- [convenience init?(shape: [Int], sampleMode: MLCSampleMode, alignsCorners: Bool)](mlcupsamplelayer/init(shape:samplemode:alignscorners:).md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignment option you specify.
- [enum MLCSampleMode](mlcsamplemode.md)
  A sampling mode for an upsample layer.
### Inspecting Upsample Layers
- [var shape: [Int]](mlcupsamplelayer/shape-61n1u.md)
  An array that contains the dimensions of the result tensor.
- [var sampleMode: MLCSampleMode](mlcupsamplelayer/samplemode.md)
  The upsampling algorithm type.
- [var alignsCorners: Bool](mlcupsamplelayer/alignscorners.md)
  A Boolean that indicates whether the layer aligns the corner pixels of the input and output tensors.

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
- [class MLCEmbeddingLayer](mlcembeddinglayer.md)
  A layer that stores a word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer)*