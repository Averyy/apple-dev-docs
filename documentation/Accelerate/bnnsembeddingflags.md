# BNNSEmbeddingFlags

**Framework**: Accelerate  
**Kind**: struct

Flags that control behavior of embedding layers.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct BNNSEmbeddingFlags
```

## Topics

### Embedding Flags
- [init(UInt32)](bnnsembeddingflags/init(_:).md)
  Creates a new instance with the specified raw value.
- [init(rawValue: UInt32)](bnnsembeddingflags/init(rawvalue:).md)
  Creates a new instance with the specified raw value.
- [var rawValue: UInt32](bnnsembeddingflags/rawvalue.md)
  The corresponding value of the raw type.
- [var BNNSEmbeddingFlagScaleGradientByFrequency: BNNSEmbeddingFlags](bnnsembeddingflagscalegradientbyfrequency.md)
  A flag that specifies that the operation scales calculated gradients based on the number of occurrence of the corresponding index in the input.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var flags: BNNSEmbeddingFlags](bnnslayerparametersembedding/flags.md)
  A bit field for flags that specify additional behavior, such as scaling gradient by frequency.
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnsembeddingflags)*