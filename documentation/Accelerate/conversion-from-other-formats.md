# Conversion from Other Formats

**Framework**: Accelerate

Create sparse matrices from coordinate format arrays and BLAS opaque matrices.

## Topics

### Support for coordinate format arrays
- [Creating a sparse matrix from coordinate format arrays](creating-a-sparse-matrix-from-coordinate-format-arrays.md)
  Use separate coordinate format arrays to create sparse matrices.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributes_t, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Double>) -> SparseMatrix_Double](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:)-4n2el.md)
  Returns a sparse matrix of double-precision values from individual coordinate format arrays.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributes_t, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Float>) -> SparseMatrix_Float](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:)-4n2th.md)
  Returns a sparse matrix of single-precision values from individual coordinate format arrays.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributes_t, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Double>, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> SparseMatrix_Double](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-56hv8.md)
  Returns a sparse matrix of double-precision values from individual coordinate format arrays, without any internal memory allocations.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributes_t, UnsafePointer<Int32>, UnsafePointer<Int32>, UnsafePointer<Float>, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> SparseMatrix_Float](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-84plp.md)
  Returns a sparse matrix of single-precision values from individual coordinate format arrays, without any internal memory allocations.
### Support for complex coordinate format arrays
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributesComplex_t, UnsafePointer<Int32>, UnsafePointer<Int32>, OpaquePointer) -> SparseMatrix_Complex_Double](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:)-58kub.md)
  Convert from coordinate format arrays to a matrix of complex double values, dropping out-of-range entries and summing duplicates.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributesComplex_t, UnsafePointer<Int32>, UnsafePointer<Int32>, OpaquePointer) -> SparseMatrix_Complex_Float](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:)-58lgv.md)
  Convert from coordinate format arrays to a  matrix of complex float values, dropping out-of-range entries and summing duplicates.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributesComplex_t, UnsafePointer<Int32>, UnsafePointer<Int32>, OpaquePointer, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> SparseMatrix_Complex_Float](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-2blwb.md)
  Convert from coordinate format arrays to a  matrix of complex float values, dropping out-of-range entries and summing duplicates.
- [func SparseConvertFromCoordinate(Int32, Int32, Int, UInt8, SparseAttributesComplex_t, UnsafePointer<Int32>, UnsafePointer<Int32>, OpaquePointer, UnsafeMutableRawPointer, UnsafeMutableRawPointer) -> SparseMatrix_Complex_Double](sparseconvertfromcoordinate(_:_:_:_:_:_:_:_:_:_:)-6ocm1.md)
  Convert from coordinate format arrays to a  matrix of complex double values, dropping out-of-range entries and summing duplicates.
### BLAS support
- [func SparseConvertFromOpaque(sparse_matrix_double) -> SparseMatrix_Double](sparseconvertfromopaque(_:)-6n7rw.md)
  Returns a sparse matrix of double-precision, floating-point values from a BLAS opaque matrix.
- [func SparseConvertFromOpaque(sparse_matrix_float) -> SparseMatrix_Float](sparseconvertfromopaque(_:)-4u519.md)
  Returns a sparse matrix of single-precision, floating-point values from a BLAS opaque matrix.
- [func SparseConvertFromOpaque(sparse_matrix_float_complex) -> SparseMatrix_Complex_Float](sparseconvertfromopaque(_:)-9ll2d.md)
  Converts an opaque matrix of complex float values object to a transparent sparse matrix object. When you are done with this matrix, release the memory that has been allocated by calling `SparseCleanup` on it.
- [func SparseConvertFromOpaque(sparse_matrix_double_complex) -> SparseMatrix_Complex_Double](sparseconvertfromopaque(_:)-9xju4.md)
  Converts an opaque matrix of complex double values object to a transparent sparse matrix object. When you are done with this matrix, release the memory that has been allocated by calling `SparseCleanup` on it.

## See Also

- [Creating sparse matrices](creating-sparse-matrices.md)
  Create sparse matrices for factorization and solving systems.
- [struct SparseMatrix_Double](sparsematrix_double.md)
  A structure that contains a sparse matrix of double-precision, floating-point values.
- [struct SparseMatrix_Float](sparsematrix_float.md)
  A structure that contains a sparse matrix of single-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/conversion-from-other-formats)*