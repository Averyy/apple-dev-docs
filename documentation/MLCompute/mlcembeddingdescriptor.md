# MLCEmbeddingDescriptor

**Framework**: ML Compute  
**Kind**: class

A configuration object you use to create an embedding layer.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
class MLCEmbeddingDescriptor
```

## Topics

### Creating Embedding Descriptors
- [convenience init?(embeddingCount: Int, embeddingDimension: Int)](mlcembeddingdescriptor/init(embeddingcount:embeddingdimension:).md)
  Creates an embedding descriptor with the size of the dictionary and dimension of embedding vectors you specify.
- [convenience init?(embeddingCount: Int, embeddingDimension: Int, paddingIndex: Int?, maximumNorm: Float?, pNorm: Float?, scalesGradientByFrequency: Bool)](mlcembeddingdescriptor/init(embeddingcount:embeddingdimension:paddingindex:maximumnorm:pnorm:scalesgradientbyfrequency:).md)
  Creates an embedding descriptor with the size and dimension of embedding vectors, padding index, and norm and scaling options that you specify.
### Inspecting Embedding Descriptors
- [var embeddingCount: Int](mlcembeddingdescriptor/embeddingcount-77gxz.md)
  The size of the dictionary.
- [var embeddingDimension: Int](mlcembeddingdescriptor/embeddingdimension-1u9g.md)
  The dimension of embedding vectors.
- [var paddingIndex: Int?](mlcembeddingdescriptor/paddingindex-pb1e.md)
  An unsigned integer value that, if set, causes the layer to initialize the embedding vector at that index to zero.
- [var maximumNorm: Float?](mlcembeddingdescriptor/maximumnorm-17u0k.md)
  A float value that, if set, causes the layer to renormalize the selected embedding vectors to have an Lp norm less than this value.
- [var pNorm: Float?](mlcembeddingdescriptor/pnorm-8vhw1.md)
  The p of the Lp norm.
- [var scalesGradientByFrequency: Bool](mlcembeddingdescriptor/scalesgradientbyfrequency.md)
  A Boolean that indicates whether the layer scales gradients by the inverse of the frequency of words in batch before the weight update.

## Relationships

### Inherits From
- [NSObject](../ObjectiveC/NSObject-swift.class.md)
### Conforms To
- [CVarArg](../Swift/CVarArg.md)
- [CustomDebugStringConvertible](../Swift/CustomDebugStringConvertible.md)
- [CustomStringConvertible](../Swift/CustomStringConvertible.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [NSCopying](../Foundation/NSCopying.md)
- [NSObjectProtocol](../ObjectiveC/NSObjectProtocol.md)

## See Also

- [convenience init(descriptor: MLCEmbeddingDescriptor, weights: MLCTensor)](mlcembeddinglayer/init(descriptor:weights:).md)
  Creates an embedding layer with the descriptor and word embedding weights tensor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcembeddingdescriptor)*