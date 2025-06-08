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
func SparseSolve(_ method: SparseIterativeMethod, _ A: SparseMatrix_Complex_Float, _ b: DenseVector_Complex_Float, _ x: DenseVector_Complex_Float, _ Preconditioner: SparseOpaquePreconditioner_Complex_Float) -> SparseIterativeStatus_t
```

## Parameters

- `method`: (Input) Iterative method specification, eg return value of   .
- `A`: (Input) The matrix   to solve the system for. Only used for   multiplication by   or  .
- `b`: The right-hand side b to solve for. If   has dimension  , then    must have length  .
- `x`: On entry, initial guess for solution, on return the solution. If    has dimension  , then   must have length  . If no good initial   estimate is available, user should set the initial guess to be the   zero vector.
- `Preconditioner`: The preconditioner to apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:_:)-2ygeh)*