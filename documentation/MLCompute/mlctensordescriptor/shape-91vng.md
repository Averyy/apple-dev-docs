# shape

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An array that contains the size in each dimension.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```objc
@property (nonatomic, copy, readonly) NSArray<NSNumber *> * shape;
```

## See Also

### Inspecting Tensor Descriptors
- [var dataType: MLCDataType](./datatype.md)
  The tensor data type.
- [var dimensionCount: Int](./dimensioncount.md)
  The number of dimensions in the tensor.
- [stride](./stride-3ydik.md)
  An array that contains the stride, in bytes, in each dimension.
- [var tensorAllocationSizeInBytes: Int](./tensorallocationsizeinbytes.md)
  The allocation size, in bytes, for a tensor.
- [sequenceLengths](./sequencelengths-3ntsa.md)
  An array that contains the variable lengths of sequences stored in the tensor.
- [var sortedSequences: Bool](./sortedsequences.md)
  A Boolean that indicates whether you provided the sequence lengths sorted in descending order.
- [batchSizePerSequenceStep](./batchsizepersequencestep-55mp8.md)
  The batch size for each sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/shape-91vng)*