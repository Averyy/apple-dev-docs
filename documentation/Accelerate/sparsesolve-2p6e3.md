# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the equation *Subfactor * X = B* for the vector of single-precision values *X*, without any internal memory allocations.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Float, _ B: DenseVector_Float, _ X: DenseVector_Float, _ workspace: UnsafeMutableRawPointer)
```

## Parameters

- `Subfactor`: The *Subfactor* in *Subfactor* ** X = B* that [`SparseCreateSubfactor(_:_:)`](sparsecreatesubfactor(_:_:)-49d8w.md) returns.
- `B`: The vector *B*.
- `X`: The vector *X*.
- `workspace`: A workspace of size `workspaceRequiredStatic` `+` `workspaceRequiredPerRHS`.

## See Also

- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-7auge.md)
  Solves the equation *Subfactor * X = B* for the vector of double-precision values *X*, in place and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseVector_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-1xw9b.md)
  Solves the equation *Subfactor * X = B* for the vector of single-precision values *X*, in place and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseVector_Double, DenseVector_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-eaq9.md)
  Solves the equation *Subfactor * X = B* for the vector of double-precision values *X*, without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-2p6e3)*