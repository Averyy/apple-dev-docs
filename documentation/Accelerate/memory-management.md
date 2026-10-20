# Memory Management

**Framework**: Accelerate  
**Role**: API Collection

Retain and release sparse objects.

## Topics

### Resource Retention
- [func SparseRetain(SparseOpaqueSymbolicFactorization) -> SparseOpaqueSymbolicFactorization](./sparseretain%28_%29-8r2dm.md)
  Increases the reference count on a symbolic factorization object.
- [func SparseRetain(SparseOpaqueFactorization_Double) -> SparseOpaqueFactorization_Double](./sparseretain%28_%29-8943y.md)
  Increases the reference count on a double-precision numeric factorization object.
- [func SparseRetain(SparseOpaqueFactorization_Float) -> SparseOpaqueFactorization_Float](./sparseretain%28_%29-7onhr.md)
  Increases the reference count on a single-precision numeric factorization object.
- [func SparseRetain(SparseOpaqueSubfactor_Double) -> SparseOpaqueSubfactor_Double](./sparseretain%28_%29-2pmdl.md)
  Increases the reference count on a double-precision subfactor object.
- [func SparseRetain(SparseOpaqueSubfactor_Float) -> SparseOpaqueSubfactor_Float](./sparseretain%28_%29-6mr6d.md)
  Increases the reference count on a single-precision subfactor object.
- [func SparseRetain(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](./sparseretain%28_%29-5sahb.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](./sparseretain%28_%29-6pp40.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](./sparseretain%28_%29-92857.md)
  Increase reference count on a numeric factorization object, returning a copy.
- [func SparseRetain(SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](./sparseretain%28_%29-92v4w.md)
  Increase reference count on a numeric factorization object, returning a copy.
### Resource Cleanup
- [func SparseCleanup(SparseMatrix_Double)](./sparsecleanup%28_%29-6ywzn.md)
  Releases a matrix of double-precision values’ references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseMatrix_Float)](./sparsecleanup%28_%29-9f4vi.md)
  Releases a matrix of single-precision values’ references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueFactorization_Double)](./sparsecleanup%28_%29-3cnxt.md)
  Releases a factorization of a matrix of double-precision values’ references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueFactorization_Float)](./sparsecleanup%28_%29-4kus5.md)
  Releases a factorization of a matrix of single-precision values’ references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueSymbolicFactorization)](./sparsecleanup%28_%29-6jpd8.md)
  Releases a matrix factorization’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueSubfactor_Double)](./sparsecleanup%28_%29-15kpj.md)
  Releases a double-precision subfactor object’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaqueSubfactor_Float)](./sparsecleanup%28_%29-1mrmc.md)
  Releases a single-precision subfactor object’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaquePreconditioner_Double)](./sparsecleanup%28_%29-45lq7.md)
  Releases a double-precision preconditioner’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaquePreconditioner_Float)](./sparsecleanup%28_%29-1qhk8.md)
  Releases a single-precision preconditioner’s references to any memory that the Sparse Solvers library allocates.
- [func SparseCleanup(SparseOpaquePreconditioner_Complex_Float)](./sparsecleanup%28_%29-1jxdh.md)
  Release a Sparse Preconditioner’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseOpaqueFactorization_Complex_Double)](./sparsecleanup%28_%29-28nz7.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseMatrix_Complex_Double)](./sparsecleanup%28_%29-3wccz.md)
  Release a Sparse matrix’s references to any memory allocated by the Sparse library.
- [func SparseCleanup(SparseMatrix_Complex_Double)](./sparsecleanup%28_%29-3wccz.md)
  Release a Sparse matrix’s references to any memory allocated by the Sparse library.
- [func SparseCleanup(SparseOpaqueSubfactor_Complex_Float)](./sparsecleanup%28_%29-4enlt.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseMatrix_Complex_Float)](./sparsecleanup%28_%29-4z3l9.md)
  Release a Sparse matrix’s references to any memory allocated by the Sparse library.
- [func SparseCleanup(SparseOpaquePreconditioner_Complex_Double)](./sparsecleanup%28_%29-5ajx.md)
  Release a Sparse Preconditioner’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseOpaqueFactorization_Complex_Float)](./sparsecleanup%28_%29-61q1a.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.
- [func SparseCleanup(SparseOpaqueSubfactor_Complex_Double)](./sparsecleanup%28_%29-7nhza.md)
  Release a Sparse Object’s references to any memory allocated by the sparse library.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/memory-management)*