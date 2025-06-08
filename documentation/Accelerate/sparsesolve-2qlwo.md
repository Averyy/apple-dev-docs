# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solve the equation `Subfactor * X` = B for the matrix `X` of complex float values in place.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Float, _ XB: DenseMatrix_Complex_Float, _ workspace: UnsafeMutableRawPointer)
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by   .
- `XB`: (Input/Output) On input, the matrix  . On return it is overwritten   with the matrix  . If Subfactor is  , then   must have dimension   , where   and   is the number of right-hand   sides. If  , then only the first   entries are used for   input or output as approriate.
- `workspace`: (Scratch) A workspace of size   .   This memory must be 16-byte aligned (any allocation returned   by   has this property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-2qlwo)*