# SparseSolve(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Solves the system `AX=B` for `X`, using the supplied `SparseOpaqueFactorization_Complex_Double` of `A`, and without any internal memory allocations.

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
func SparseSolve(_ Factored: SparseOpaqueFactorization_Complex_Double, _ B: DenseMatrix_Complex_Double, _ X: DenseMatrix_Complex_Double, _ workspace: UnsafeMutableRawPointer)
```

#### Discussion

If the factorization is `A=QR` and the system is underdetermined, the solution of minimum norm `|| x ||_2` is returned. If the factorization is `A=QR` and the system is overdetermined, the least squares solution `arg min_x || Ax - b ||_2` is returned. In the case of a factorization of `type=SparseCholeskyAtA`, the factorization is in fact of `A^T A`, so the solution returned is for the system `A^TAx=b`.

## Parameters

- `Factored`: A factorization of  .
- `B`: The right-hand sides   to solve for. If   has dimension  , then    must have dimension  , where nrhs is the number of   right-hand sides to find solutions for.
- `X`: Matrix in which to return solutions. If   has dimension  , and    has dimension  , then   must have dimension  .
- `workspace`: Scratch space of size   .   This memory must be 16-byte aligned (any allocation returned   by   has this property).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesolve(_:_:_:_:)-5xn6p)*