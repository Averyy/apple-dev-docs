# dataType

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The tensor data type.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var dataType: MLCDataType { get }
```

```objc
@property (nonatomic, readonly) MLCDataType dataType;
```

## See Also

### Inspecting Tensor Descriptors
- [var dimensionCount: Int](./dimensioncount.md)
  The number of dimensions in the tensor.
- [var shape: [Int]](./shape-7i1rw.md)
  An array that contains the size in each dimension.
- [var stride: [Int]](./stride-5mzlt.md)
  An array that contains the stride, in bytes, in each dimension.
- [var tensorAllocationSizeInBytes: Int](./tensorallocationsizeinbytes.md)
  The allocation size, in bytes, for a tensor.
- [var sequenceLengths: [Int]?](./sequencelengths-3jdab.md)
  An array that contains the variable lengths of sequences stored in the tensor.
- [var sortedSequences: Bool](./sortedsequences.md)
  A Boolean that indicates whether you provided the sequence lengths sorted in descending order.
- [var batchSizePerSequenceStep: [Int]?](./batchsizepersequencestep-6iz59.md)
  The batch size for each sequence.
- [shape](./shape-91vng.md)
  An array that contains the size in each dimension.
- [stride](./stride-3ydik.md)
  An array that contains the stride, in bytes, in each dimension.
- [sequenceLengths](./sequencelengths-3ntsa.md)
  An array that contains the variable lengths of sequences stored in the tensor.
- [batchSizePerSequenceStep](./batchsizepersequencestep-55mp8.md)
  The batch size for each sequence.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlctensordescriptor/datatype)*