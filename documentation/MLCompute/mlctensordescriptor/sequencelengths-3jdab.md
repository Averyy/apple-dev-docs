# sequenceLengths

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

An array that contains the variable lengths of sequences stored in the tensor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.0
- iPadOS 14.0+ - Deprecated in 17.0
- Mac Catalyst 14.0+ - Deprecated in 17.0
- macOS 11.0+ - Deprecated in 14.0
- tvOS 14.0+ - Deprecated in 17.0

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
var sequenceLengths: [Int]? { get }
```

## See Also

### Inspecting Tensor Descriptors
- [var dataType: MLCDataType](./datatype.md)
  The tensor data type.
- [var dimensionCount: Int](./dimensioncount.md)
  The number of dimensions in the tensor.
- [var shape: [Int]](./shape-7i1rw.md)
  An array that contains the size in each dimension.
- [var stride: [Int]](./stride-5mzlt.md)
  An array that contains the stride, in bytes, in each dimension.
- [var tensorAllocationSizeInBytes: Int](./tensorallocationsizeinbytes.md)
  The allocation size, in bytes, for a tensor.
- [var sortedSequences: Bool](./sortedsequences.md)
  A Boolean that indicates whether you provided the sequence lengths sorted in descending order.
- [var batchSizePerSequenceStep: [Int]?](./batchsizepersequencestep-6iz59.md)
  The batch size for each sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/sequencelengths-3jdab)*