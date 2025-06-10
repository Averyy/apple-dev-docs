# SparseSolve(_:_:)

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Float, _ XB: DenseMatrix_Complex_Float)
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by   .
- `XB`: (Input/Output) On input, the matrix  . On return it is overwritten   with the matrix  . If   is  , then   must have dimension   , where   and   is the number of right-hand   sides. If  , then only the first   entries are used for   input or output as approriate.

## See Also

- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:)-3x0vj.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-4fydu.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:)-78cl0.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-2qlwo.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex float values in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-5stp5.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6afcf.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-9ui81.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-9xxqn.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-879na)*