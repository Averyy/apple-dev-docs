# SparseSolve(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve `Ax=b` using the specified iterative method for complex double values.

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
func SparseSolve(_ method: SparseIterativeMethod, _ ApplyOperator: @escaping (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Double, DenseVector_Complex_Double) -> Void, _ b: DenseVector_Complex_Double, _ x: DenseVector_Complex_Double, _ Preconditioner: SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t
```

## Parameters

- `method`: (Input) Iterative method specification, eg return value of   .
- `ApplyOperator`:    should perform the operation   if   is  ,   or   if   is  .
- `b`: The right-hand side   to solve for. If   has dimension  , then    must have length  .
- `x`: On entry, initial guess for solution, on return the solution. If    has dimension  , then   must have length  . If no good initial   estimate is available, user should set the initial guess to be the   zero vector.
- `Preconditioner`: (Input) The preconditioner to use.

## See Also

- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Float, DenseVector_Complex_Float) -> Void, DenseVector_Complex_Float, DenseVector_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-2cenj.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Double, DenseVector_Complex_Double) -> Void, DenseVector_Complex_Double, DenseVector_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:)-35kl2.md)
  Solve `Ax=b` using the specified iterative method for complex double values.
- [func SparseSolve(SparseIterativeMethod, (Bool, CBLAS_TRANSPOSE, DenseVector_Complex_Float, DenseVector_Complex_Float) -> Void, DenseVector_Complex_Float, DenseVector_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-2bm9r.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-2ygeh.md)
  Solve `Ax=b` using the specified iterative method for complex float values.
- [func SparseSolve(SparseIterativeMethod, SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, SparseOpaquePreconditioner_Complex_Double) -> SparseIterativeStatus_t](sparsesolve(_:_:_:_:_:)-7yfqx.md)
  Solve `Ax=b` using the specified iterative method for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:_:)-1ogxn)*