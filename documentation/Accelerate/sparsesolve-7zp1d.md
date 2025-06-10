# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve `AX=B` using the specified iterative method for complex double values.

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
func SparseSolve(_ method: SparseIterativeMethod, _ A: SparseMatrix_Complex_Double, _ B: DenseMatrix_Complex_Double, _ X: DenseMatrix_Complex_Double) -> SparseIterativeStatus_t
```

## Parameters

- `method`: (Input) Iterative method specification, eg return value of   .
- `A`: (Input) The matrix   to solve the system for. Only used for   multiplication by   or  .
- `B`: The right-hand sides   to solve for. If   has dimension  , then    must have dimension  , where   is the number of   right-hand sides to find solutions for.
- `X`: On entry, initial guess for solution, on return the solution. If A   has dimension  , and   has dimension  , then   must have   dimension  . If no good initial estimate is available, user   should set the initial guess to be the zero vector.

## See Also

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
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-8bndu.md)
  Solve `AX=B` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-8yld7.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, SparsePreconditioner_t) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-4xd4z.md)
  Solve `AX=B` using the specified iterative method for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-7zp1d)*