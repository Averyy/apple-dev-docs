# Sparse Direct Solving Functions (Matrix RHS)

**Framework**: Accelerate

Solve a system with a right-hand-side dense matrix using a factored sparse coefficient matrix.

## Topics

### In-place direct solving functions
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseMatrix_Double)](sparsesolve(_:_:)-9j9rw.md)
  Solves the system  using the supplied double-precision factorization of , in place.
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseMatrix_Float)](sparsesolve(_:_:)-1jp0k.md)
  Solves the system  using the supplied single-precision factorization of , in place.
### Out-of-place direct solving functions
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsesolve(_:_:_:)-3iav7.md)
  Solves the system  using the supplied double-precision factorization of .
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsesolve(_:_:_:)-2rxlq.md)
  Solves the system  using the supplied single-precision factorization of .
### In-place direct solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-l2kw.md)
  Solves the system  using the supplied double-precision factorization of , in place and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-749fu.md)
  Solves the system  using the supplied single-precision factorization of , in place and without any internal memory allocations.
### Out-of-place direct solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseMatrix_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-7aj3g.md)
  Solves the system  using the supplied double-precision factorization of , without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseMatrix_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-8xma8.md)
  Solves the system  using the supplied single-precision factorization of , without any internal memory allocations.
### Complex matrix solving functions
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:)-31yj7.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:)-3x0vj.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:)-4j17a.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-2qlwo.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex float values in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:_:)-2rk1c.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of A`,` in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-34okt.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:_:)-48njk.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of A`,` in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-6pudz.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex double values in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:_:)-7krer.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:_:)-7qdpl.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-8ikjb.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-5xn6p.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6demt.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6od6k.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-7mtyx.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, and without any internal memory allocations.

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
- [Sparse Direct Solving Functions (Vector RHS)](sparse-direct-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using a factored sparse coefficient matrix.
- [Sparse Symbolic Factorization Functions](sparse-symbolic-factorization-functions.md)
  Calculate the symbolic factorization of a matrix, and solve systems using precalculated symbolic factorizations.
- [Sparse Refactor Functions](sparse-refactor-functions.md)
  Recompute a factorization using the numerical data from a matrix.
- [Subfactor Functions](subfactor-functions.md)
  Extract and work with subfactors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-direct-solving-functions-matrix-rhs)*