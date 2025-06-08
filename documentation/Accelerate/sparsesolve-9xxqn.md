# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ B: DenseMatrix_Complex_Double, _ X: DenseMatrix_Complex_Double, _ workspace: UnsafeMutableRawPointer)
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by   .
- `B`: (Input) The right-hand sides  . If   is  , then   must   have dimension  , where   is the number of right-hand   sides.
- `X`: (Output) The solutions  . If   is  , and   is  ,   then   must have dimension  .
- `workspace`: (Scratch) A workspace of size   .   This memory must be 16-byte aligned (any allocation returned   by   has this property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-9xxqn)*