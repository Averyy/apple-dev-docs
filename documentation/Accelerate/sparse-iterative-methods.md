# Sparse Iterative Methods

**Framework**: Accelerate

Select a suitable iterative method to solve a system.

#### Overview

Sparse Iterative methods solve  through an iterative process that only requires multiplication by  or . However, if  is numerically difficult, the iterative process may fail to converge to a solution. Even for problems where the process converges, it may do so slowly. You can fix both of these issues through the application of a problem-specific preconditioner that approximates the inverse of .

## Topics

### Sparse Iterative Methods for Symmetric Positive-Definite Coefficient Matrices
- [func SparseConjugateGradient() -> SparseIterativeMethod](sparseconjugategradient().md)
  Returns a conjugate gradient (CG) method.
- [func SparseConjugateGradient(SparseCGOptions) -> SparseIterativeMethod](sparseconjugategradient(_:).md)
  Returns a conjugate gradient (CG) method with specified options.
- [struct SparseCGOptions](sparsecgoptions.md)
  Options for creating a conjugate gradient (CG) method.
### Sparse Iterative Methods for Symmetric Indefinite and Unsymmetric Coefficient Matrices
- [func SparseGMRES() -> SparseIterativeMethod](sparsegmres().md)
  Returns a generalized minimal residual (GMRES) method.
- [func SparseGMRES(SparseGMRESOptions) -> SparseIterativeMethod](sparsegmres(_:).md)
  Returns a generalized minimal residual (GMRES) method with specified options.
- [struct SparseGMRESOptions](sparsegmresoptions.md)
  Options for creating a generalized minimal residual (GMRES) method.
### Sparse Iterative Methods for Overdetermined and Underdetermined Systems
- [func SparseLSMR() -> SparseIterativeMethod](sparselsmr().md)
  Returns a default least squares minimum residual (LSMR) method.
- [func SparseLSMR(SparseLSMROptions) -> SparseIterativeMethod](sparselsmr(_:).md)
  Returns a least squares minimum residual method with specified options.
- [struct SparseLSMROptions](sparselsmroptions.md)
  Options for creating a least squares minimum residual method.
### Iterative Method Structure
- [struct SparseIterativeMethod](sparseiterativemethod.md)
  The base type for all iterative methods.

## See Also

- [Solving systems using iterative methods](solving-systems-using-iterative-methods.md)
  Use iterative methods to solve systems of equations where the coefficient matrix is sparse.
- [Sparse Iterative Solving Functions (Matrix RHS)](sparse-iterative-solving-functions-matrix-rhs.md)
  Solve a system with a right-hand-side dense matrix using iterative methods.
- [Sparse Iterative Solving Functions (Vector RHS)](sparse-iterative-solving-functions-vector-rhs.md)
  Solve a system with a right-hand-side dense vector using iterative methods.
- [Sparse Iterate Functions](sparse-iterate-functions.md)
  Perform a single iteration of the specified iterative method.
- [Preconditioners](preconditioners.md)
  Create preconditioners for iterative solves.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparse-iterative-methods)*