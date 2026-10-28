# norm_type

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The norm type.

**Availability**:
- iOS 15.0+ - Deprecated in 18.0
- iPadOS 15.0+ - Deprecated in 18.0
- Mac Catalyst 15.0+ - Deprecated in 18.0
- macOS 12.0+ - Deprecated in 15.0
- tvOS 15.0+ - Deprecated in 18.0
- visionOS 1.0+ - Deprecated in 2.0
- watchOS 8.0+ - Deprecated in 11.0

> **Deprecated**: Use BNNSGraph* APIs

## Declaration

```swift
var norm_type: Float
```

```c
float norm_type;
```

## Discussion

If `max_norm` is nonzero, this value specifies the p-norm where `p = norm_type`.

## See Also

### Instance Properties
- [var flags: BNNSEmbeddingFlags](./flags.md)
  A bit field for flags that specify additional behavior, such as scaling gradient by frequency.
- [struct BNNSEmbeddingFlags](../bnnsembeddingflags.md)
  Flags that control behavior of embedding layers.
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The signed or unsigned integer descriptor of the input.
- [var o_desc: BNNSNDArrayDescriptor](./o_desc.md)
  The descriptor of the output.
- [var dictionary: BNNSNDArrayDescriptor](./dictionary.md)
  The descriptor of the dictionary.
- [var padding_idx: Int](./padding_idx.md)
  The padding index.
- [var max_norm: Float](./max_norm.md)
  The maximum norm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersembedding/norm_type)*