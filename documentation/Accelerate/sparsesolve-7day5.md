# SparseSolve(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the system `Ax=b` for `x`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Complex_Double, _ b: DenseVector_Complex_Double, _ x: DenseVector_Complex_Double)
```

#### Discussion

If the factorization is `A=QR` and the system is underdetermined, the solution of minimum norm `|| x ||_2` is returned. If the factorization is `A=QR` and the system is overdetermined, the least squares solution `arg min_x || Ax - b ||_2` is returned. In the case of a factorization of `type=SparseCholeskyAtA`, the factorization is in fact of `A^T A`, so the solution returned is for the system `A^TAx=b`.

## Parameters

- `Factored`: A factorization of  .
- `b`: The right-hand side   to solve for. If   has dimension  , then    must have length  .
- `x`: Vector in which to return solution. If   has dimension  , then    must have length  .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:)-7day5)*