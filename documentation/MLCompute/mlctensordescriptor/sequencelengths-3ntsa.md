# sequenceLengths

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An array that contains the variable lengths of sequences stored in the tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
@property (nonatomic, copy, readonly, nullable) NSArray<NSNumber *> * sequenceLengths;
```

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
- [var sortedSequences: Bool](./sortedsequences.md)
  A Boolean that indicates whether you provided the sequence lengths sorted in descending order.
- [batchSizePerSequenceStep](./batchsizepersequencestep-55mp8.md)
  The batch size for each sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/sequencelengths-3ntsa)*