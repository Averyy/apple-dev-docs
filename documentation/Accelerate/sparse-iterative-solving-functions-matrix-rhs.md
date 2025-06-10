# Sparse Iterative Solving Functions (Matrix RHS)

**Framework**: Accelerate

Solve a system with a right-hand-side dense matrix using iterative methods.

## Topics

### Iterative sparse solve functions
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-3ft19.md)
  Solves the equation  for matrices of double-precision values using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-1f00y.md)
  Solves the equation  for matrices of single-precision values using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void, DenseMatrix_Double, DenseMatrix_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-vewd.md)
  Solves the equation  for matrices of double-precision values, treating  as an operator and using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void, DenseMatrix_Float, DenseMatrix_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-8mtxu.md)
  Solves the equation  for matrices of single-precision values, treating  as an operator and using the specified iterative method.
### Iterative sparse solve functions with preconditioner
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double, SparseOpaquePreconditioner_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-5yh8m.md)
  Solves the equation  for matrices of double-precision values using the specified iterative method and opaque preconditioner.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float, SparseOpaquePreconditioner_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7vrh0.md)
  Solves the equation  for matrices of single-precision values using the specified iterative method and opaque preconditioner.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseMatrix_Double, DenseMatrix_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-5d7vf.md)
  Solves the equation  for matrices of double-precision values using the specified iterative method and preconditioner type.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseMatrix_Float, DenseMatrix_Float, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7apig.md)
  Solves the equation  for matrices of single-precision values using the specified iterative method and preconditioner type.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Double, DenseMatrix_Double) -> Void, DenseMatrix_Double, DenseMatrix_Double, SparseOpaquePreconditioner_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-8nfbc.md)
  Solves the equation  for matrices of double-precision values, treating  as an operator and using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Float, DenseMatrix_Float) -> Void, DenseMatrix_Float, DenseMatrix_Float, SparseOpaquePreconditioner_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-80ri4.md)
  Solves the equation  for matrices of single-precision values, treating  as an operator and using the specified iterative method.
### Iterative sparse solve functions for complex matrices
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-41c6p.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-4xwsw.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-155od.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-1fw3p.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-1i6u8.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-4fvqm.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-4fvqm.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-4fvqm.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-655i9.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7hdp4.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7m9vp.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-6wjj9.md)
  Solve `AX=B` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-7zp1d.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-8bndu.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-8yld7.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-4xd4z.md)
  Solve `AX=B` using the specified iterative method for complex double values.
### Supporting types
- [struct SparseIterativeStatus_t](sparseiterativestatus_t.md)
  Constants that define the status of the iterative solve.

## See Also

- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)
  Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Sparse Iterative Solving Functions (Vector RHS)](sparse-iterative-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using iterative methods.
- [Sparse Iterate Functions](sparse-iterate-functions.md)
  Perform a single iteration of the specified iterative method.
- [Sparse Iterative Methods](sparse-iterative-methods.md)
  Select a suitable iterative method to solve a system.
- [Preconditioners](preconditioners.md)
  Create preconditioners for iterative solves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-iterative-solving-functions-matrix-rhs)*