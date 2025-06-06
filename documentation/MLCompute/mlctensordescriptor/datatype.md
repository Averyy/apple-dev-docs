# dataType

**Framework**: ML Compute  
**Kind**: property

The tensor data type.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var dataType: MLCDataType { get }
```

## See Also

- [var dimensionCount: Int](mlctensordescriptor/dimensioncount.md)
  The number of dimensions in the tensor.
- [var shape: [Int]](mlctensordescriptor/shape-7i1rw.md)
  An array that contains the size in each dimension.
- [var stride: [Int]](mlctensordescriptor/stride-5mzlt.md)
  An array that contains the stride, in bytes, in each dimension.
- [var tensorAllocationSizeInBytes: Int](mlctensordescriptor/tensorallocationsizeinbytes.md)
  The allocation size, in bytes, for a tensor.
- [var sequenceLengths: [Int]?](mlctensordescriptor/sequencelengths-3jdab.md)
  An array that contains the variable lengths of sequences stored in the tensor.
- [var sortedSequences: Bool](mlctensordescriptor/sortedsequences.md)
  A Boolean that indicates whether you provided the sequence lengths sorted in descending order.
- [var batchSizePerSequenceStep: [Int]?](mlctensordescriptor/batchsizepersequencestep-6iz59.md)
  The batch size for each sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/datatype)*