# Sparse Direct Solving Functions (Vector RHS)

**Framework**: Accelerate

Solve a system with a right-hand-side dense vector using a factored sparse coefficient matrix.

## Topics

### In-place direct solving functions
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseVector_Double)](sparsesolve(_:_:)-pofy.md)
  Solves the system  using the supplied double-precision factorization of .
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseVector_Float)](sparsesolve(_:_:)-60ngw.md)
  Solves the system  using the supplied single-precision factorization of , in place.
### Out-of-place direct solving functions
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseVector_Double, DenseVector_Double)](sparsesolve(_:_:_:)-416bj.md)
  Solves the system  using the supplied double-precision factorization of .
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseVector_Float, DenseVector_Float)](sparsesolve(_:_:_:)-666oh.md)
  Solves the system  using the supplied single-precision factorization of .
### In-place direct solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-14nj.md)
  Solves the system  using the supplied double-precision factorization of , in place and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseVector_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-9hs9y.md)
  Solves the system  using the supplied single-precision factorization of , in place and without any internal memory allocations.
### Out-of-place direct solving functions with user-defined workspace
- [func SparseSolve(SparseOpaqueFactorization_Double, DenseVector_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-7k9ll.md)
  Solves the system  using the supplied double-precision factorization of , without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Float, DenseVector_Float, DenseVector_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6bmr8.md)
  Solves the system  using the supplied single-precision factorization of , without any internal memory allocations.
### Complex direct solving functions
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-4fydu.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:)-1psgz.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-4fydu.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-5apxy.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-3482l.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:_:)-3hev5.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-3qkkl.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:_:)-76ge0.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:_:)-7day5.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-7ltk8.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:_:)-85y2u.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-90ojf.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.

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
- [Sparse Symbolic Factorization Functions](sparse-symbolic-factorization-functions.md)
  Calculate the symbolic factorization of a matrix, and solve systems using precalculated symbolic factorizations.
- [Sparse Refactor Functions](sparse-refactor-functions.md)
  Recompute a factorization using the numerical data from a matrix.
- [Subfactor Functions](subfactor-functions.md)
  Extract and work with subfactors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-direct-solving-functions-vector-rhs)*