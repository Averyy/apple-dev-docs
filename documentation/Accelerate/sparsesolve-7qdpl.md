# SparseSolve(_:_:_:)

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
func SparseSolve(_ Subfactor: SparseOpaqueSubfactor_Complex_Double, _ B: DenseMatrix_Complex_Double, _ X: DenseMatrix_Complex_Double)
```

## Parameters

- `Subfactor`: (Input) The subfactor to solve a system involving, as returned by  .
- `B`: (Input) The right-hand sides  . If   is  , then   must   have dimension  , where   is the number of right-hand   sides.
- `X`: (Output) The solutions  . If   is  , and   is  ,   then   must have dimension  .

## See Also

- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:)-31yj7.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:)-3x0vj.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:)-4j17a.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-2qlwo.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex float values in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsesolve(_:_:_:)-2rk1c.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of A`,` in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-34okt.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:_:)-48njk.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of A`,` in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-6pudz.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex double values in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsesolve(_:_:_:)-7krer.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-8ikjb.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-5xn6p.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6demt.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-6od6k.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:_:)-7mtyx.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, and without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-7qdpl)*