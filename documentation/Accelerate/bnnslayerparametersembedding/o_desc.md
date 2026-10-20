# o_desc

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The descriptor of the output.

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
var o_desc: BNNSNDArrayDescriptor
```

```c
BNNSNDArrayDescriptor o_desc;
```

## See Also

### Instance Properties
- [var flags: BNNSEmbeddingFlags](./flags.md)
  A bit field for flags that specify additional behavior, such as scaling gradient by frequency.
- [struct BNNSEmbeddingFlags](../bnnsembeddingflags.md)
  Flags that control behavior of embedding layers.
- [var i_desc: BNNSNDArrayDescriptor](./i_desc.md)
  The signed or unsigned integer descriptor of the input.
- [var dictionary: BNNSNDArrayDescriptor](./dictionary.md)
  The descriptor of the dictionary.
- [var padding_idx: Int](./padding_idx.md)
  The padding index.
- [var max_norm: Float](./max_norm.md)
  The maximum norm.
- [var norm_type: Float](./norm_type.md)
  The norm type.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersembedding/o_desc)*