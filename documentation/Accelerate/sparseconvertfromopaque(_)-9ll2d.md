# SparseConvertFromOpaque(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
static SparseMatrix_Complex_Float SparseConvertFromOpaque(sparse_matrix_float_complex matrix);
```

## Parameters

- `matrix`: The matrix to be converted.

## See Also

### BLAS support
- [func SparseConvertFromOpaque(sparse_matrix_double) -> SparseMatrix_Double](./sparseconvertfromopaque%28_%29-6n7rw.md)
  Returns a sparse matrix of double-precision, floating-point values from a BLAS opaque matrix.
- [func SparseConvertFromOpaque(sparse_matrix_float) -> SparseMatrix_Float](./sparseconvertfromopaque%28_%29-4u519.md)
  Returns a sparse matrix of single-precision, floating-point values from a BLAS opaque matrix.
- [func SparseConvertFromOpaque(sparse_matrix_double_complex) -> SparseMatrix_Complex_Double](./sparseconvertfromopaque%28_%29-9xju4.md)
  Converts an opaque matrix of complex double values object to a transparent sparse matrix object. When you are done with this matrix, release the memory that has been allocated by calling `SparseCleanup` on it.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseconvertfromopaque(_:)-9ll2d)*