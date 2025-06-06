# BNNSLayerParametersEmbedding

**Framework**: Accelerate  
**Kind**: struct

A structure that contains the parameters of an embedding layer.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+
- visionOS 1.0+
- watchOS 8.0+

## Declaration

```swift
struct BNNSLayerParametersEmbedding
```

## Topics

### Initializers
- [init()](bnnslayerparametersembedding/init.md)
  Returns a new embedding layer parameters structure.
- [init(flags: BNNSEmbeddingFlags, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, dictionary: BNNSNDArrayDescriptor, padding_idx: Int, max_norm: Float, norm_type: Float)](bnnslayerparametersembedding/init(flags:i_desc:o_desc:dictionary:padding_idx:max_norm:norm_type:).md)
  Returns a new embedding layer parameter structure from the specified parameters.
### Instance Properties
- [var flags: BNNSEmbeddingFlags](bnnslayerparametersembedding/flags.md)
  A bit field for flags that specify additional behavior, such as scaling gradient by frequency.
- [struct BNNSEmbeddingFlags](bnnsembeddingflags.md)
  Flags that control behavior of embedding layers.
- [var i_desc: BNNSNDArrayDescriptor](bnnslayerparametersembedding/i_desc.md)
  The signed or unsigned integer descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](bnnslayerparametersembedding/o_desc.md)
  The descriptor of the output.
- [var dictionary: BNNSNDArrayDescriptor](bnnslayerparametersembedding/dictionary.md)
  The descriptor of the dictionary.
- [var padding_idx: Int](bnnslayerparametersembedding/padding_idx.md)
  The padding index.
- [var max_norm: Float](bnnslayerparametersembedding/max_norm.md)
  The maximum norm.
- [var norm_type: Float](bnnslayerparametersembedding/norm_type.md)
  The norm type.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [class EmbeddingLayer](bnns/embeddinglayer.md)
  A layer object that wraps an embedding filter and manages its deinitialization.
- [func BNNSFilterCreateLayerEmbedding(UnsafePointer<BNNSLayerParametersEmbedding>, UnsafePointer<BNNSFilterParameters>?) -> BNNSFilter?](bnnsfiltercreatelayerembedding(_:_:).md)
  Returns a new embedding layer.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersembedding)*