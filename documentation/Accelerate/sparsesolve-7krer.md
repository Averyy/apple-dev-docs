# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values, in place.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Float, _ B: DenseMatrix_Complex_Float, _ X: DenseMatrix_Complex_Float)
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by  .
- `B`: (Input) The right-hand sides  . If   is  , then   must   have dimension  , where   is the number of right-hand   sides.
- `X`: (Output) The solutions  . If   is  , and   is  ,   then   must have dimension  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-7krer)*