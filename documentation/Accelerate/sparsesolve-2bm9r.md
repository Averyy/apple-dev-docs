# SparseSolve(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve `Ax=b` using the specified iterative method for complex float values.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseSolve(_ method: SparseIterativeMethod, _ ApplyOperator: @escaping (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Float, DenseVector_Complex_Float) -> Void, _ b: DenseVector_Complex_Float, _ x: DenseVector_Complex_Float, _ Preconditioner: SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t
```

## Parameters

- `method`: (Input) Iterative method specification, eg return value of `SparseConjugateGradient()`.
- `ApplyOperator`: `ApplyOperator(accumulate, trans, X, Y)` should perform the operation `Y = op(A)X` if `accumulate` is `false`, or `Y += op(A)X` if `accumulate` is `true`. - **`accumulate`**: (input) Indicates whether to perform `Y += op(A)X` (if true) or `Y = op(A)X` (if false).
- **`trans`**: (input) Indicates whether `op(A)` is the application of `A` (`trans=CblasNoTrans`) or `A^T` (`trans=CblasTrans`).
- **`x`**: The vector to multiply.
- **`y`**: The vector in which to accumulate or store the result.
- `b`: The right-hand side `b` to solve for. If `a` has dimension `m x n`, then `b` must have length `m`.
- `x`: On entry, initial guess for solution, on return the solution. If `A` has dimension `m x n`, then `x` must have length `n`. If no good initial estimate is available, user should set the initial guess to be the zero vector.
- `Preconditioner`: (Input) The preconditioner to use.

## See Also

- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Float, DenseVector_Complex_Float) -> Void, DenseVector_Complex_Float, DenseVector_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-2cenj.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Double, DenseVector_Complex_Double) -> Void, DenseVector_Complex_Double, DenseVector_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-35kl2.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Double, DenseVector_Complex_Double) -> Void, DenseVector_Complex_Double, DenseVector_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-1ogxn.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-2ygeh.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7yfqx.md)
  Solve `Ax=b` using the specified iterative method for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:_:)-2bm9r)*