# SparseConvertFromCoordinate(_:_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a sparse matrix of double-precision values from individual coordinate format arrays, without any internal memory allocations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseConvertFromCoordinate(_ rowCount: Int32, _ columnCount: Int32, _ blockCount: Int, _ blockSize: UInt8, _ attributes: SparseAttributes_t, _ row: UnsafePointer<Int32>, _ column: UnsafePointer<Int32>, _ data: UnsafePointer<Double>, _ storage: UnsafeMutableRawPointer, _ workspace: UnsafeMutableRawPointer) -> SparseMatrix_Double
```

## Mentions

- [Creating a sparse matrix from coordinate format arrays](creating-a-sparse-matrix-from-coordinate-format-arrays.md)

#### Return Value

A new [`SparseMatrix_Double`](sparsematrix_double.md) object, using the memory you provide in the storage parameter. After you finish using a sparse matrix, call [`SparseCleanup(_:)`](sparsecleanup(_:)-6ywzn.md) to release its references to any memory that the Sparse Solvers library allocates.

#### Discussion

The conversion drops out-of-range entries, and sums duplicate entries.

You may supply entries in either triangle for symmetric matrices. The conversion transposes entries in the triangle that [`triangle`](sparseattributes_t/triangle.md) doesn’t specify, and sums duplicate entries.

For triangular matrices, the conversion drops entries in the triangle that [`triangle`](sparseattributes_t/triangle.md) doesn’t specify.

## Parameters

- `rowCount`: The number of rows in the structure.
- `columnCount`: The number of columns in the structure.
- `blockCount`: The number of blocks in the matrix.
- `blockSize`: The block size for data storage on both input and output.
- `attributes`: The attributes of the matrix to create. The conversion forces the matrix to conform to the specified attributes by copying or dropping elements as necessary.
- `row`: The row indices of the matrix structure.
- `column`: The column indices of the matrix structure.
- `data`: The contents of the structurally nonzero (block) matrix elements.
- `storage`: A block of memory to store the returned matrix.
- `workspace`: The workspace of size  .

## See Also

- [Creating a sparse matrix from coordinate format arrays](creating-a-sparse-matrix-from-coordinate-format-arrays.md)
  Use separate coordinate format arrays to create sparse matrices.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributes_t, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Double>) -> SparseMatrix_Double](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:)-4n2el.md)
  Returns a sparse matrix of double-precision values from individual coordinate format arrays.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributes_t, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Float>) -> SparseMatrix_Float](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:)-4n2th.md)
  Returns a sparse matrix of single-precision values from individual coordinate format arrays.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributes_t, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Float>, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> SparseMatrix_Float](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-84plp.md)
  Returns a sparse matrix of single-precision values from individual coordinate format arrays, without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-56hv8)*