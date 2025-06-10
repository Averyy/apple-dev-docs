# Sparse Refactor Functions

**Framework**: Accelerate

Recompute a factorization using the numerical data from a matrix.

## Topics

### Matrix Refactorization Functions
- [func SparseRefactor(SparseMatrix_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Double>)](sparserefactor(_:_:)-8vrf5.md)
  Computes a factorization of the specified double-precision matrix using an existing factorization’s storage.
- [func SparseRefactor(SparseMatrix_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Float>)](sparserefactor(_:_:)-21q4x.md)
  Computes a factorization of the specified single-precision matrix using an existing factorization’s storage.
- [func SparseRefactor(SparseMatrix_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-6ttkd.md)
  Computes a factorization of the specified double-precision matrix using an existing factorization’s storage and specified options.
- [func SparseRefactor(SparseMatrix_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-2ovxs.md)
  Computes a factorization of the specified single-precision matrix using an existing factorization’s storage and specified options.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>)](sparserefactor(_:_:)-mgni.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>)](sparserefactor(_:_:)-zegz.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-4chx2.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, using different options.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-q0va.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, using different options.
### Matrix Refactorizations Functions with User-Defined Workspace
- [func SparseRefactor(SparseMatrix_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-9mqeq.md)
  Computes a factorization of the specified double-precision matrix using an existing factorization’s storage, without internal memory allocation.
- [func SparseRefactor(SparseMatrix_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-2dqt8.md)
  Computes a factorization of the specified single-precision matrix using an existing factorization’s storage, without internal memory allocation.
- [func SparseRefactor(SparseMatrix_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-59ehf.md)
  Computes a factorization of the specified double-precision matrix using an existing factorization’s storage and specified options, and without internal memory allocation.
- [func SparseRefactor(SparseMatrix_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-8i8vi.md)
  Computes a factorization of the specified single-precision matrix using an existing factorization’s storage and specified options, and without internal memory allocation.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-4ofvz.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, without any internal allocations.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-593yb.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, without any internal allocations.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-201rh.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, using updated options and without any internal allocations.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-20xqc.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, using updated options and without any internal allocations.
### Numeric Factorization Options
- [struct SparseNumericFactorOptions](sparsenumericfactoroptions.md)
  A structure that contains options that affect the numerical stage of a sparse factorization.

## See Also

- [Solving systems using direct methods](solving-systems-using-direct-methods.md)
  Use direct methods to solve systems of equations where the coefficient matrix is sparse.
- [struct SparseOpaqueFactorization_Double](sparseopaquefactorization_double.md)
  A structure that represents the factorization of a matrix of double-precision, floating-point values.
- [struct SparseOpaqueFactorization_Float](sparseopaquefactorization_float.md)
  A structure that represents the factorization of a matrix of single-precision, floating-point values.
- [struct SparseOpaqueFactorization_Complex_Double](sparseopaquefactorization_complex_double.md)
  A semi-opaque type representing a matrix factorization in complex double.
- [struct SparseOpaqueFactorization_Complex_Float](sparseopaquefactorization_complex_float.md)
  A semi-opaque type representing a matrix factorization in complex float.
- [Sparse Matrix Factor Functions](sparse-matrix-factor-functions.md)
  Compute the factorization of a matrix.
- [Sparse Direct Solving Functions (Matrix RHS)](sparse-direct-solving-functions-matrix-rhs.md)
  Solve a system with a right-hand-side dense matrix using a factored sparse coefficient matrix.
- [Sparse Direct Solving Functions (Vector RHS)](sparse-direct-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using a factored sparse coefficient matrix.
- [Sparse Symbolic Factorization Functions](sparse-symbolic-factorization-functions.md)
  Calculate the symbolic factorization of a matrix, and solve systems using precalculated symbolic factorizations.
- [Subfactor Functions](subfactor-functions.md)
  Extract and work with subfactors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-refactor-functions)*