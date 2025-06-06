# init(flags:i_desc:o_desc:dictionary:padding_idx:max_norm:norm_type:)

**Framework**: Accelerate  
**Kind**: init

Returns a new embedding layer parameter structure from the specified parameters.

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
init(flags: BNNSEmbeddingFlags, i_desc: BNNSNDArrayDescriptor, o_desc: BNNSNDArrayDescriptor, dictionary: BNNSNDArrayDescriptor, padding_idx: Int, max_norm: Float, norm_type: Float)
```

## Parameters

- `flags`: A bit field for flags that specify additional behavior, such as scaling gradient by frequency.
- `i_desc`: The signed or unsigned integer descriptor of the input.
- `o_desc`: The descriptor of the output.
- `dictionary`: The descriptor of the dictionary.
- `padding_idx`: The padding index. The operation returns a zero tensor for dictionary items with an index that corresponds to the padding index.
- `max_norm`: The maximum norm. If nonzero, the operation renormalizes any vector with a norm greater than   during forward lookups.
- `norm_type`: The norm type. If   is nonzero, this value specifies the p-norm where  .

## See Also

- [init()](bnnslayerparametersembedding/init.md)
  Returns a new embedding layer parameters structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/bnnslayerparametersembedding/init(flags:i_desc:o_desc:dictionary:padding_idx:max_norm:norm_type:))*