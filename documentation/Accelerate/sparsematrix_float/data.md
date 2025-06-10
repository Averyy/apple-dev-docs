# data

**Framework**: Accelerate  
**Kind**: property

The array of contiguous values in the nonzero blocks of the matrix.

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
var data: UnsafeMutablePointer<Float>
```

#### Discussion

The matrix stores each block in column-major order. The number of elements in [`data`](sparsematrix_double/data.md) must be equal to [`blockSize`](sparsematrixstructure/blocksize.md) x [`blockSize`](sparsematrixstructure/blocksize.md) x the number of nonzero blocks in the matrix.

## See Also

- [var structure: SparseMatrixStructure](sparsematrix_float/structure.md)
  The sparsity structure of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrix_float/data)*