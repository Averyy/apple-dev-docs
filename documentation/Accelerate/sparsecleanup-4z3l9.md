# SparseCleanup(_:)

**Framework**: Accelerate  
**Kind**: func

Release a Sparse matrix’s references to any memory allocated by the Sparse library.

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
func SparseCleanup(_ toFree: SparseMatrix_Complex_Float)
```

#### Discussion

Reports an error if the matrix was not allocated by Sparse.

## See Also

- [func SparseCleanup(SparseMatrix_Double)](sparsecleanup(_:)-6ywzn.md)
  Releases a matrix of double-precision values’ references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseMatrix_Float)](sparsecleanup(_:)-9f4vi.md)
  Releases a matrix of single-precision values’ references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueFactorization_Double)](sparsecleanup(_:)-3cnxt.md)
  Releases a factorization of a matrix of double-precision values’ references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueFactorization_Float)](sparsecleanup(_:)-4kus5.md)
  Releases a factorization of a matrix of single-precision values’ references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueSymbolicFactorization)](sparsecleanup(_:)-6jpd8.md)
  Releases a matrix factorization’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueSubfactor_Double)](sparsecleanup(_:)-15kpj.md)
  Releases a double-precision subfactor object’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueSubfactor_Float)](sparsecleanup(_:)-1mrmc.md)
  Releases a single-precision subfactor object’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaquePreconditioner_Double)](sparsecleanup(_:)-45lq7.md)
  Releases a double-precision preconditioner’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaquePreconditioner_Float)](sparsecleanup(_:)-1qhk8.md)
  Releases a single-precision preconditioner’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaquePreconditioner_Complex_Float)](sparsecleanup(_:)-1jxdh.md)
  Release a Sparse Preconditioner’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseOpaqueFactorization_Complex_Double)](sparsecleanup(_:)-28nz7.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseMatrix_Complex_Double)](sparsecleanup(_:)-3wccz.md)
  Release a Sparse matrix’s references to any memory allocated by the Sparse library.
- [func SparseCleanup(SparseMatrix_Complex_Double)](sparsecleanup(_:)-3wccz.md)
  Release a Sparse matrix’s references to any memory allocated by the Sparse library.
- [func SparseCleanup(SparseOpaqueSubfactor_Complex_Float)](sparsecleanup(_:)-4enlt.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseOpaquePreconditioner_Complex_Double)](sparsecleanup(_:)-5ajx.md)
  Release a Sparse Preconditioner’s references to any memory allocated by the sparse library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecleanup(_:)-4z3l9)*