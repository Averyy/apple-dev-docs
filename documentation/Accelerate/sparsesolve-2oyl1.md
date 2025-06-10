# SparseSolve(_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the equation  in place for the matrix of double-precision values .

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Double, _ XB: DenseMatrix_Double)
```

## Parameters

- `Subfactor`: The   in     that   returns.
- `XB`: On input, the matrix  . On return, the matrix   overwrites it.

## See Also

- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float)](sparsesolve(_:_:)-2tyws.md)
  Solves the equation  in place for the matrix of single-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double, DenseMatrix_Double)](sparsesolve(_:_:_:)-1lads.md)
  Solves the equation  for the matrix of double-precision values .
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsesolve(_:_:_:)-76z89.md)
  Solves the equation  for the matrix of single-precision values .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-2oyl1)*