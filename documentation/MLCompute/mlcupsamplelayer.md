# MLCUpsampleLayer

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A layer that applies upsampling with the shape you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCUpsampleLayer
```

```objc
@interface MLCUpsampleLayer : MLCLayer
```

## Topics

### Creating Upsample Layers
- [convenience init?(shape: [Int])](./mlcupsamplelayer/init%28shape%29.md)
  Creates an upsample layer with the shape you specify.
- [convenience init?(shape: [Int], sampleMode: MLCSampleMode, alignsCorners: Bool)](./mlcupsamplelayer/init%28shape,samplemode,alignscorners%29.md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignment option you specify.
- [enum MLCSampleMode](./mlcsamplemode.md)
  A sampling mode for an upsample layer.
- [+ layerWithShape:](./mlcupsamplelayer/layerwithshape_.md)
  Creates an upsample layer with the shape you specify.
- [+ layerWithShape:sampleMode:alignsCorners:](./mlcupsamplelayer/layerwithshape_samplemode_alignscorners_.md)
  Creates an upsample layer with the shape, upsampling algorithm, and corner alignement option you specify.
### Inspecting Upsample Layers
- [var shape: [Int]](./mlcupsamplelayer/shape-61n1u.md)
  An array that contains the dimensions of the result tensor.
- [var sampleMode: MLCSampleMode](./mlcupsamplelayer/samplemode.md)
  The upsampling algorithm type.
- [var alignsCorners: Bool](./mlcupsamplelayer/alignscorners.md)
  A Boolean that indicates whether the layer aligns the corner pixels of the input and output tensors.
- [shape](./mlcupsamplelayer/shape-7j6sf.md)
  An array that contains the dimensions of the result tensor.

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
- [class MLCPoolingLayer](./mlcpoolinglayer.md)
  A layer that summarizes the average presence of a feature.
- [class MLCEmbeddingLayer](./mlcembeddinglayer.md)
  A layer that stores a word embedding.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcupsamplelayer)*