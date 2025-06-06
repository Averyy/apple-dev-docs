# norm_type

**Framework**: Accelerate  
**Kind**: property

The norm type.

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
var norm_type: Float
```

#### Discussion

If `max_norm` is nonzero, this value specifies the p-norm where `p = norm_type`.

## See Also

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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersembedding/norm_type)*