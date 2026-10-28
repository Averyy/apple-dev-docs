# SparseSolve(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Complex_Float, _ XB: DenseMatrix_Complex_Float)
```

```c
static void SparseSolve(SparseOpaqueFactorization_Complex_Float Factored, DenseMatrix_Complex_Float XB);
```

## Discussion

If the factorization is `A=QR` and the system is underdetermined, the solution of minimum norm `|| x ||_2` is returned. If the factorization is A=QR and the system is overdetermined, the least squares solution `arg min_x || Ax - b ||_2` is returned. In the case of a factorization of `type=SparseCholeskyAtA`, the factorization is in fact of `A^T A`, so the solution returned is for the system `A^TAx=b`.

## Parameters

- `Factored`: A factorization of `A`.
- `XB`: On entry, the right-hand sides `B`. On return, the solution vectors `X`. If `A` has dimension `m x n`, then `XB` must have dimension `k x nrhs`, where `k=max(m,n)` and nrhs is the number of right-hand sides to find solutions for.

## See Also

### Complex matrix solving functions
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double)](./sparsesolve%28_,_%29-31yj7.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double)](./sparsesolve%28_,_%29-3x0vj.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-2qlwo.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex float values in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](./sparsesolve%28_,_,_%29-2rk1c.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of A`,` in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-34okt.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsesolve%28_,_,_%29-48njk.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of A`,` in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-6pudz.md)
  Solve the equation `Subfactor * X` = B for the matrix `X` of complex double values in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsesolve%28_,_,_%29-7krer.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex float values, in place.
- [func SparseSolve(SparseOpaqueSubfactor_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](./sparsesolve%28_,_,_%29-7qdpl.md)
  Solve the equation `Subfactor * X = B` for the matrix `X` of complex double values, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_%29-8ikjb.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-5xn6p.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, and without any internal memory allocations.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-6demt.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-6od6k.md)
  Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, in place.
- [func SparseSolve(SparseOpaqueFactorization_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float, UnsafeMutableRawPointer)](./sparsesolve%28_,_,_,_%29-7mtyx.md)
  Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Float` of `A`, and without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:)-4j17a)*