# batchSizePerSequenceStep

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The batch size for each sequence.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSNumber *> * batchSizePerSequenceStep;
```

## Discussion

The framework only populates this value when [`sequenceLengths`](./sequencelengths-3ntsa.md) is valid. The length of this array is equal to the maximum sequence length in `sequenceLengths`; that’s `sequenceLengths[0]` when [`sortedSequences`](./sortedsequences.md) is `YES`.

## See Also

### Inspecting Tensor Descriptors
- [var dataType: MLCDataType](./datatype.md)
  The tensor data type.
- [var dimensionCount: Int](./dimensioncount.md)
  The number of dimensions in the tensor.
- [shape](./shape-91vng.md)
  An array that contains the size in each dimension.
- [stride](./stride-3ydik.md)
  An array that contains the stride, in bytes, in each dimension.
- [var tensorAllocationSizeInBytes: Int](./tensorallocationsizeinbytes.md)
  The allocation size, in bytes, for a tensor.
- [sequenceLengths](./sequencelengths-3ntsa.md)
  An array that contains the variable lengths of sequences stored in the tensor.
- [var sortedSequences: Bool](./sortedsequences.md)
  A Boolean that indicates whether you provided the sequence lengths sorted in descending order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/batchsizepersequencestep-55mp8)*