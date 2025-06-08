# SparseIterate(_:_:_:_:_:_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Perform a single iteration of the specified iterative method for complex double values with preconditioner.

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
func SparseIterate(_ method: SparseIterativeMethod, _ iteration: Int32, _ converged: UnsafePointer<Bool>, _ state: UnsafeMutableRawPointer, _ ApplyOperator: @escaping (Bool, CBLAS_TRANSPOSE, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double) -> Void, _ B: DenseMatrix_Complex_Double, _ R: DenseMatrix_Complex_Double, _ X: DenseMatrix_Complex_Double, _ Preconditioner: SparseOpaquePreconditioner_Complex_Double)
```

## Parameters

- `method`: (Input) Iterative method specification, eg return value of   .
- `iteration`: (Input) The current iteration number, starting from 0. If   , then the current iterate is finalised, and the value of    is updated (note that this may force some methods to restart,   slowing convergence).
- `converged`: (Input) Convergence status of each solution vector.    indicates that the vector stored as column   of    has converged, and it should be ignored in this iteration.
- `state`: (Input/Output) A pointer to a state-space of size returned by   . This memory must be 16-byte aligned   (any allocation returned by   has this property). It must not   be altered by the user between iterations, but may be safely discarded   after the final call to  .
- `ApplyOperator`:    should perform the operation   if   is  ,   or   if   is  .
- `B`: (Input) The right-hand sides to solve for.
- `R`: (Output) Residual estimate. On entry with  , it must hold   the residuals   (equal to   if  ). On return from each call with   , the first entry(s) of each vector contain various   estimates of norms to be used in convergence testing.
- `X`: (Input/Output) The current estimate of the solution vectors X.   On entry with iteration=0, this should be an initial estimate for the   solution. If no good estimate is available, use X = 0.0.   Depending on the method used, X may not be updated at each iteration,   or may be used to store some other vector.   The user should make a call with iteration<0 once convergence has   been achieved to bring X up to date.
- `Preconditioner`: (Input) Preconditioner to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseiterate(_:_:_:_:_:_:_:_:_:)-1wv28)*