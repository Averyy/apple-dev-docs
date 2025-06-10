# SparseMatrix_Double

**Framework**: Accelerate  
**Kind**: struct

A structure that contains a sparse matrix of double-precision, floating-point values.

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
struct SparseMatrix_Double
```

## Mentions

- [Creating sparse matrices](creating-sparse-matrices.md)

#### Overview

You typically use sparse matrices to represent the sparse coefficient matrix in the matrix equation  A [`SparseMatrix_Double`](sparsematrix_double.md) structure provides a pointer to its underlying data, and information about its structure and attributes.

The Accelerate framework uses the compressed sparse column (CSC) format to store sparse matrices. CSC stores the matrix as a series of column vectors that specifies only the nonzero entries as `(row-index, value)` pairs. For more information, see [`Creating sparse matrices`](creating-sparse-matrices.md).

After you finish using a sparse matrix, call [`SparseCleanup(_:)`](sparsecleanup(_:)-6ywzn.md) to release its references to any memory that the Sparse Solvers library allocates.

## Topics

### Creating a Sparse Matrix
- [init(structure: SparseMatrixStructure, data: UnsafeMutablePointer<Double>)](sparsematrix_double/init(structure:data:).md)
  Creates a sparse matrix with the specified structure that contains double-precision values.
### Inspecting a Matrix’s Structure and Data
- [var structure: SparseMatrixStructure](sparsematrix_double/structure.md)
  The sparsity structure of the matrix.
- [var data: UnsafeMutablePointer<Double>](sparsematrix_double/data.md)
  The array of contiguous values in the nonzero blocks of the matrix.
### Specifying the Structure and Attributes of a Sparse Matrix
- [struct SparseMatrixStructure](sparsematrixstructure.md)
  A description of the sparsity structure of a sparse matrix.
- [struct SparseAttributes_t](sparseattributes_t.md)
  A structure that represents the attributes of a matrix.

## See Also

- [Creating sparse matrices](creating-sparse-matrices.md)
  Create sparse matrices for factorization and solving systems.
- [struct SparseMatrix_Float](sparsematrix_float.md)
  A structure that contains a sparse matrix of single-precision, floating-point values.
- [Conversion from Other Formats](conversion-from-other-formats.md)
  Create sparse matrices from coordinate format arrays and BLAS opaque matrices.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrix_double)*