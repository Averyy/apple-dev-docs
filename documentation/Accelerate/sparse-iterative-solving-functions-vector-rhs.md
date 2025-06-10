# Sparse Iterative Solving Functions (Vector RHS)

**Framework**: Accelerate

Solve a system with a right-hand-side dense vector using iterative methods.

## Topics

### Iterative sparse solve functions
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseVector_Double, DenseVector_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-7f1sp.md)
  Solves the equation  for vectors of double-precision values using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseVector_Float, DenseVector_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-97k3a.md)
  Solves the equation  for vectors of single-precision values using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Double, DenseVector_Double) -> Void, DenseVector_Double, DenseVector_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-26fae.md)
  Solves the equation  for vectors of double-precision values, treating  as an operator and using the specified iterative method.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Float, DenseVector_Float) -> Void, DenseVector_Float, DenseVector_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-9yhgp.md)
  Solves the equation  for vectors of single-precision values, treating  as an operator and using the specified iterative method.
### Iterative sparse solve functions with preconditioner
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseVector_Double, DenseVector_Double, SparseOpaquePreconditioner_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-1qwax.md)
  Solves the equation  for vectors of double-precision values using the specified iterative method and opaque preconditioner.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseVector_Float, DenseVector_Float, SparseOpaquePreconditioner_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-3aphv.md)
  Solves the equation  for vectors of single-precision values using the specified iterative method and opaque preconditioner.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Double, DenseVector_Double, DenseVector_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-5vs11.md)
  Solves the equation  for vectors of double-precision values using the specified iterative method and preconditioner type.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Float, DenseVector_Float, DenseVector_Float, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-9nzvm.md)
  Solves the equation  for vectors of single-precision values using the specified iterative method and preconditioner type.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Double, DenseVector_Double) -> Void, DenseVector_Double, DenseVector_Double, SparseOpaquePreconditioner_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-6i1nx.md)
  Solves the equation  for vectors of double-precision values, treating  as an operator and using the specified iterative method and preconditioner.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Float, DenseVector_Float) -> Void, DenseVector_Float, DenseVector_Float, SparseOpaquePreconditioner_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7wnum.md)
  Solves the equation  for vectors of single-precision values, treating  as an operator and using the specified iterative method and preconditioner.
### Iterative sparse solve functions for complex matrices
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Float, DenseVector_Complex_Float) -> Void, DenseVector_Complex_Float, DenseVector_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-2cenj.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Double, DenseVector_Complex_Double) -> Void, DenseVector_Complex_Double, DenseVector_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-35kl2.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Double, DenseVector_Complex_Double) -> Void, DenseVector_Complex_Double, DenseVector_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-1ogxn.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Float, DenseVector_Complex_Float) -> Void, DenseVector_Complex_Float, DenseVector_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-2bm9r.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-2ygeh.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7yfqx.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
### Supporting types
- [struct SparseIterativeStatus_t](sparseiterativestatus_t.md)
  Constants that define the status of the iterative solve.

## See Also

- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)
  Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Sparse Iterative Solving Functions (Matrix RHS)](sparse-iterative-solving-functions-matrix-rhs.md)
  Solve a system with a right-hand-side dense matrix using iterative methods.
- [Sparse Iterate Functions](sparse-iterate-functions.md)
  Perform a single iteration of the specified iterative method.
- [Sparse Iterative Methods](sparse-iterative-methods.md)
  Select a suitable iterative method to solve a system.
- [Preconditioners](preconditioners.md)
  Create preconditioners for iterative solves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-iterative-solving-functions-vector-rhs)*