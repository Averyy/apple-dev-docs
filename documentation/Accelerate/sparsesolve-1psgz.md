# SparseSolve(_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Complex_Double, _ xb: DenseVector_Complex_Double)
```

#### Discussion

If the factorization is A=QR and the system is underdetermined, the solution of minimum norm `|| x ||_2` is returned. If the factorization is `A=QR` and the system is overdetermined, the least squares solution `arg min_x || Ax - b ||_2` is returned. In the case of a `factorization of type=SparseCholeskyAtA`, the factorization is in fact of `A^T A`, so the solution returned is for the system `A^TAx=b`.

## Parameters

- `Factored`: A factorization of  .
- `xb`: On entry, the right-hand side  . On return, the solution vector   . If A has dimension  , then   must have length  , where   .

## See Also

- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-4fydu.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-4fydu.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:)-5apxy.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-3482l.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:_:)-3hev5.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-3qkkl.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex float values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsesolve(_:_:_:)-76ge0.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:_:)-7day5.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-7ltk8.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsesolve(_:_:_:)-85y2u.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](sparsesolve(_:_:_:)-90ojf.md)
  Solve the equation `Subfactor * x = b` for the vector `x` of complex double values, in place.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-1psgz)*