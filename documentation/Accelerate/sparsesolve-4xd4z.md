# SparseSolve(_:_:_:_:_:)

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
func SparseSolve(_ method: SparseIterativeMethod, _ A: SparseMatrix_Complex_Double, _ B: DenseMatrix_Complex_Double, _ X: DenseMatrix_Complex_Double, _ Preconditioner: SparsePreconditioner_t) -> SparseIterativeStatus_t
```

## Parameters

- `method`: (Input) Iterative method specification, eg return value of   .
- `A`: (Input) The matrix   to solve the system for. Only used for   multiplication by   or  .
- `B`: The right-hand sides   to solve for. If   has dimension  , then    must have dimension  , where   is the number of   right-hand sides to find solutions for.
- `X`: On entry, initial guess for solution, on return the solution. If    has dimension  , and   has dimension  , then   must have   dimension  . If no good initial estimate is available, user   should set the initial guess to be the zero vector.
- `Preconditioner`: Type of preconditioner to create and apply.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:_:)-4xd4z)*