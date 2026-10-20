# MLCEmbeddingDescriptor

**Framework**: ML Compute  
**Kind**: class  
**Role**: Class

A configuration object you use to create an embedding layer.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
class MLCEmbeddingDescriptor
```

```objc
@interface MLCEmbeddingDescriptor : NSObject
```

## Topics

### Creating Embedding Descriptors
- [convenience init?(embeddingCount: Int, embeddingDimension: Int)](./mlcembeddingdescriptor/init%28embeddingcount,embeddingdimension%29.md)
  Creates an embedding descriptor with the size of the dictionary and dimension of embedding vectors you specify.
- [convenience init?(embeddingCount: Int, embeddingDimension: Int, paddingIndex: Int?, maximumNorm: Float?, pNorm: Float?, scalesGradientByFrequency: Bool)](./mlcembeddingdescriptor/init%28embeddingcount,embeddingdimension,paddingindex,maximumnorm,pnorm,scalesgradientbyfrequency%29.md)
  Creates an embedding descriptor with the size and dimension of embedding vectors, padding index, and norm and scaling options that you specify.
### Inspecting Embedding Descriptors
- [var embeddingCount: Int](./mlcembeddingdescriptor/embeddingcount-77gxz.md)
  The size of the dictionary.
- [var embeddingDimension: Int](./mlcembeddingdescriptor/embeddingdimension-1u9g.md)
  The dimension of embedding vectors.
- [var paddingIndex: Int?](./mlcembeddingdescriptor/paddingindex-pb1e.md)
  An unsigned integer value that, if set, causes the layer to initialize the embedding vector at that index to zero.
- [var maximumNorm: Float?](./mlcembeddingdescriptor/maximumnorm-17u0k.md)
  A float value that, if set, causes the layer to renormalize the selected embedding vectors to have an Lp norm less than this value.
- [var pNorm: Float?](./mlcembeddingdescriptor/pnorm-8vhw1.md)
  The p of the Lp norm.
- [var scalesGradientByFrequency: Bool](./mlcembeddingdescriptor/scalesgradientbyfrequency.md)
  A Boolean that indicates whether the layer scales gradients by the inverse of the frequency of words in batch before the weight update.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/nsobject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/cvararg.md)
- [CustomDebugStringConvertible](../Swift/customdebugstringconvertible.md)
- [CustomStringConvertible](../Swift/customstringconvertible.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [NSCopying](../Foundation/nscopying.md)
- [NSObjectProtocol](../ObjectiveC/nsobjectprotocol.md)

## See Also

### Creating Embedding Layers
- [convenience init(descriptor: MLCEmbeddingDescriptor, weights: MLCTensor)](./mlcembeddinglayer/init%28descriptor,weights%29.md)
  Creates an embedding layer with the descriptor and word embedding weights tensor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor)*