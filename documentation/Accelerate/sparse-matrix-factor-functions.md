# Sparse Matrix Factor Functions

**Framework**: Accelerate

Compute the factorization of a matrix.

## Topics

### Matrix factorization functions
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Double) -> SparseOpaqueFactorization_Double](sparsefactor(_:_:)-8gl6j.md)
  Returns the specified factorization of a sparse matrix of double-precision values.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Float) -> SparseOpaqueFactorization_Float](sparsefactor(_:_:)-38shj.md)
  Returns the specified factorization of a sparse matrix of single-precision values.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Double, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Double](sparsefactor(_:_:_:_:)-88xmk.md)
  Returns the specified factorization of a sparse matrix of double-precision values using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Float, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Float](sparsefactor(_:_:_:_:)-8apyz.md)
  Returns the specified factorization of a sparse matrix of single-precision values using the specified options.
### Complex matrix factorization functions
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:)-1avkp.md)
  Returns the specified factorization of a sparse matrix of complex double values.
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructureComplex) -> SparseOpaqueSymbolicFactorization](sparsefactor(_:_:)-55tzk.md)
  Returns a symbolic factorization of the requested type for a complex matrix with the given structure.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:)-5zzpu.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:)-73n38.md)
  Returns the specified factorization of a sparse matrix of complex float values.
### Factorization inertia functions
- [func SparseGetInertia(SparseOpaqueFactorization_Float, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-6r90r.md)
  Returns the inertia of a single-precision  factorization.
- [func SparseGetInertia(SparseOpaqueFactorization_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-2ykzq.md)
  Returns the inertia of a double-precision  factorization.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Double, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-2gc7f.md)
  Returns the inertia of an LDLT factorization in complex double.
- [func SparseGetInertia(SparseOpaqueFactorization_Complex_Float, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>, UnsafeMutablePointer<Int32>) -> Int32](sparsegetinertia(_:_:_:_:)-6ca5h.md)
  Returns the inertia of an LDLT factorization in complex float.
- [struct SparseUpdate_t](sparseupdate_t.md)
  Low-rank update algorithm selector
- [var SparseUpdatePartialRefactor: SparseUpdate_t](sparseupdatepartialrefactor.md)
  Low-rank update algorithm selector
### Factorization update functions
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, Int32, UnsafePointer<Int32>, SparseMatrix_Complex_Float)](sparseupdatefactor(_:_:_:_:_:)-1n2be.md)
  Apply a low-rank update to an existing factorization of a matrix of complex float values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, Int32, UnsafePointer<Int32>, SparseMatrix_Complex_Double)](sparseupdatefactor(_:_:_:_:_:)-9h956.md)
  Apply a low-rank update to an existing factorization of a matrix of complex double values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, Int32, UnsafePointer<Int32>, SparseMatrix_Float)](sparseupdatefactor(_:_:_:_:_:)-9qg54.md)
  Apply a low-rank update to an existing factorization of a matrix of float values.
- [func SparseUpdateFactor(SparseUpdate_t, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, Int32, UnsafePointer<Int32>, SparseMatrix_Double)](sparseupdatefactor(_:_:_:_:_:)-wrqg.md)
  Apply a low-rank update to an existing factorization of a matrix of double values.
### Structures that specify factorization type and factorization options
- [struct SparseFactorization_t](sparsefactorization_t.md)
  Constants that define the factorization type.
- [struct SparseSymbolicFactorOptions](sparsesymbolicfactoroptions.md)
  A structure that contains options that affect the symbolic stage of a sparse factorization.
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
- [Sparse Direct Solving Functions (Matrix RHS)](sparse-direct-solving-functions-matrix-rhs.md)
  Solve a system with a right-hand-side dense matrix using a factored sparse coefficient matrix.
- [Sparse Direct Solving Functions (Vector RHS)](sparse-direct-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using a factored sparse coefficient matrix.
- [Sparse Symbolic Factorization Functions](sparse-symbolic-factorization-functions.md)
  Calculate the symbolic factorization of a matrix, and solve systems using precalculated symbolic factorizations.
- [Sparse Refactor Functions](sparse-refactor-functions.md)
  Recompute a factorization using the numerical data from a matrix.
- [Subfactor Functions](subfactor-functions.md)
  Extract and work with subfactors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-matrix-factor-functions)*