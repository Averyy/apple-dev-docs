# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the equation *Subfactor * X = B* for the matrix of double-precision values *X*.

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Double, _ B: DenseMatrix_Double, _ X: DenseMatrix_Double)
```

## Parameters

- `Subfactor`: The *Subfactor* in *Subfactor* ** X = B* that [`SparseCreateSubfactor(_:_:)`](sparsecreatesubfactor(_:_:)-49d8w.md) returns.
- `B`: The matrix *B*.
- `X`: The matrix *X*.

## See Also

- [func SparseSolve(SparseOpaqueSubfactor_Double, DenseMatrix_Double)](sparsesolve(_:_:)-2oyl1.md)
  Solves the equation *Subfactor * X = B* in place for the matrix of double-precision values *X*.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float)](sparsesolve(_:_:)-2tyws.md)
  Solves the equation *Subfactor * X = B* in place for the matrix of single-precision values *X*.
- [func SparseSolve(SparseOpaqueSubfactor_Float, DenseMatrix_Float, DenseMatrix_Float)](sparsesolve(_:_:_:)-76z89.md)
  Solves the equation *Subfactor * X = B* for the matrix of single-precision values *X*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-1lads)*