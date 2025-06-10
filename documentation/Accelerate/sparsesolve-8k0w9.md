# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the equation  in place for the matrix of double-precision values , without any internal memory allocations.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Double, _ XB: DenseMatrix_Double, _ workspace: UnsafeMutableRawPointer)
```

## Parameters

- `Subfactor`: The   in     that   returns.
- `XB`: On input, the matrix  . On return, the matrix   overwrites it.
- `workspace`: A workspace of size       where   is the number of right-hand-side vectors.

## See Also

- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-9kp2g.md)
  Solves the equation  in place for the matrix of single-precision values , without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-90z8f.md)
  Solves the equation  for the matrix of double-precision values , without any internal memory allocations.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-1hhdi.md)
  Solves the equation  for the matrix of single-precision values , without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-8k0w9)*