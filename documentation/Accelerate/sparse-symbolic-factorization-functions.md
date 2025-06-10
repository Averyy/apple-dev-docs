# Sparse Symbolic Factorization Functions

**Framework**: Accelerate

Calculate the symbolic factorization of a matrix, and solve systems using precalculated symbolic factorizations.

## Topics

### Matrix symbolic factorization functions
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructure) -> SparseOpaqueSymbolicFactorization](sparsefactor(_:_:)-3697o.md)
  Returns a symbolic factorization of the requested type for a specified sparsity structure.
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructure, SparseSymbolicFactorOptions) -> SparseOpaqueSymbolicFactorization](sparsefactor(_:_:_:)-45gsz.md)
  Returns a symbolic factorization of the requested type for a single-precision matrix with the specified structure.
### Matrix factorizations using precalculated symbolic factorization
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Double) -> SparseOpaqueFactorization_Double](sparsefactor(_:_:)-58oq8.md)
  Returns the factorization of a sparse matrix of double-precision values that corresponds to the supplied symbolic factorization.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Float) -> SparseOpaqueFactorization_Float](sparsefactor(_:_:)-1p6im.md)
  Returns the factorization of a sparse matrix of single-precision values that corresponds to the supplied symbolic factorization.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Double, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Double](sparsefactor(_:_:_:)-3ddg.md)
  Returns the factorization of a sparse matrix of double-precision values that corresponds to the supplied symbolic factorization using specified options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Float, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Float](sparsefactor(_:_:_:)-797fl.md)
  Returns the factorization of a sparse matrix of single-precision values that corresponds to the supplied symbolic factorization using specified options.
### Matrix factorizations using precalculated symbolic factorization with user-defined workspace
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Double, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Double](sparsefactor(_:_:_:_:_:)-68hki.md)
  Returns the factorization of a sparse matrix of double-precision values that corresponds to the supplied symbolic factorization using user-defined workspace and factor storage.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Float, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Float](sparsefactor(_:_:_:_:_:)-8afz.md)
  Returns the factorization of a sparse matrix of single-precision values that corresponds to the supplied symbolic factorization using user-defined workspace and factor storage.
### Supporting types
- [struct SparseOpaqueSymbolicFactorization](sparseopaquesymbolicfactorization.md)
  A semi-opaque type that represents symbolic matrix factorization.
- [struct SparseFactorization_t](sparsefactorization_t.md)
  Constants that define the factorization type.
- [struct SparseSymbolicFactorOptions](sparsesymbolicfactoroptions.md)
  A structure that contains options that affect the symbolic stage of a sparse factorization.
### Complex factorization functions
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:)-7a3l4.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization.
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructureComplex, SparseSymbolicFactorOptions) -> SparseOpaqueSymbolicFactorization](sparsefactor(_:_:_:)-6s9g.md)
  Returns a symbolic factorization of the requested type for a complex matrix with the given structure, with the supplied options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:)-7kqvi.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:)-9ypz5.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization, using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:_:)-6hqfp.md)
  Returns the specified factorization of a sparse matrix of complex double values, using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:_:)-9ykfp.md)
  Returns the specified factorization of a sparse matrix of complex float values, using the specified options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:_:_:)-2dqfv.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:_:_:)-7j0dm.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.

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
- [Sparse Refactor Functions](sparse-refactor-functions.md)
  Recompute a factorization using the numerical data from a matrix.
- [Subfactor Functions](subfactor-functions.md)
  Extract and work with subfactors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-symbolic-factorization-functions)*