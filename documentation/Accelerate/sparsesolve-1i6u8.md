# SparseSolve(_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve `AX=B` using the specified iterative method for complex float values.

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
func SparseSolve(_ method: SparseIterativeMethod, _ ApplyOperator: @escaping (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float) -> Void, _ B: DenseMatrix_Complex_Float, _ X: DenseMatrix_Complex_Float, _ Preconditioner: SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t
```

## Parameters

- `method`: (Input) Iterative method specification, eg return value of   SparseConjugateGradient().
- `ApplyOperator`:    should perform the operation   if   is  ,   or   if   is  .
- `B`: The right-hand sides   to solve for. If   has dimension  , then    must have dimension  , where   is the number of   right-hand sides to find solutions for.
- `X`: On entry, initial guess for solution, on return the solution. If    has dimension   and   has dimension  , then   must have   dimension  . If no good initial estimate is available, user   should set the initial guess to be the zero vector.
- `Preconditioner`: (Input) The preconditioner to use.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:_:)-1i6u8)*