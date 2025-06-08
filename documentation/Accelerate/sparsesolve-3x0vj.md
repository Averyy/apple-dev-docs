# SparseSolve(_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ XB: DenseMatrix_Complex_Double)
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by   .
- `XB`: (Input/Output) On input, the matrix  . On return it is overwritten   with the matrix  . If   is  , then   must have dimension   , where   and   is the number of right-hand   sides. If  , then only the first   entries are used for   input or output as approriate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-3x0vj)*