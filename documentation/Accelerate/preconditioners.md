# Preconditioners

**Framework**: Accelerate

Create preconditioners for iterative solves.

#### Overview

In many cases, applying a preconditioner to the coefficient matrix reduces the number of iterations necessary to solve the system. The Sparse Solvers library provides Jacobi and diagonal scaling preconditioners, and the functionality to create user-defined preconditioners.

## Topics

### Preconditioners
- [struct SparsePreconditioner_t](sparsepreconditioner_t.md)
  Constants that define the preconditioner type.
- [struct SparseOpaquePreconditioner_Complex_Double](sparseopaquepreconditioner_complex_double.md)
  Represents a preconditioner for matrices of complex double values .
- [struct SparseOpaquePreconditioner_Complex_Float](sparseopaquepreconditioner_complex_float.md)
  Represents a preconditioner for matrices of complex float values .
### Creating preconditioners
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Double) -> SparseOpaquePreconditioner_Double](sparsecreatepreconditioner(_:_:)-4ysww.md)
  Creates a preconditioner for the specified matrix of double-precision values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Float) -> SparseOpaquePreconditioner_Float](sparsecreatepreconditioner(_:_:)-59ql5.md)
  Creates a preconditioner for the specified matrix of single-precision values.
- [struct SparseOpaquePreconditioner_Double](sparseopaquepreconditioner_double.md)
  A structure that represents a double-precision preconditioner.
- [struct SparseOpaquePreconditioner_Float](sparseopaquepreconditioner_float.md)
  A structure that represents a single-precision preconditioner.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Double) -> SparseOpaquePreconditioner_Complex_Double](sparsecreatepreconditioner(_:_:)-1yp4n.md)
  Create a preconditioner for the given matrix of complex double values.
- [func SparseCreatePreconditioner(SparsePreconditioner_t, SparseMatrix_Complex_Float) -> SparseOpaquePreconditioner_Complex_Float](sparsecreatepreconditioner(_:_:)-95u9p.md)
  Create a preconditioner for the given matrix of complex float values.

## See Also

- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)
  Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Sparse Iterative Solving Functions (Matrix RHS)](sparse-iterative-solving-functions-matrix-rhs.md)
  Solve a system with a right-hand-side dense matrix using iterative methods.
- [Sparse Iterative Solving Functions (Vector RHS)](sparse-iterative-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using iterative methods.
- [Sparse Iterate Functions](sparse-iterate-functions.md)
  Perform a single iteration of the specified iterative method.
- [Sparse Iterative Methods](sparse-iterative-methods.md)
  Select a suitable iterative method to solve a system.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/preconditioners)*