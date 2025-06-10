# SparseConvertFromOpaque(_:)

**Framework**: Accelerate  
**Kind**: func

Converts an opaque matrix of complex float values object to a transparent sparse matrix object. When you are done with this matrix, release the memory that has been allocated by calling `SparseCleanup` on it.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseConvertFromOpaque(_ matrix: sparse_matrix_float_complex) -> SparseMatrix_Complex_Float
```

## Parameters

- `matrix`: The matrix to be converted.

## See Also

- [func SparseConvertFromOpaque(sparse_matrix_double) -> SparseMatrix_Double](sparseconvertfromopaque(_:)-6n7rw.md)
  Returns a sparse matrix of double-precision, floating-point values from a BLAS opaque matrix.
- [func SparseConvertFromOpaque(sparse_matrix_float) -> SparseMatrix_Float](sparseconvertfromopaque(_:)-4u519.md)
  Returns a sparse matrix of single-precision, floating-point values from a BLAS opaque matrix.
- [func SparseConvertFromOpaque(sparse_matrix_double_complex) -> SparseMatrix_Complex_Double](sparseconvertfromopaque(_:)-9xju4.md)
  Converts an opaque matrix of complex double values object to a transparent sparse matrix object. When you are done with this matrix, release the memory that has been allocated by calling `SparseCleanup` on it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseconvertfromopaque(_:)-9ll2d)*