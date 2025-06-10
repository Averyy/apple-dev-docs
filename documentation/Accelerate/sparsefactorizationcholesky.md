# SparseFactorizationCholesky

**Framework**: Accelerate  
**Kind**: var

A constant that represents Cholesky () factorization.

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
var SparseFactorizationCholesky: SparseFactorization_t { get }
```

#### Discussion

[`SparseFactorizationCholesky`](sparsefactorizationcholesky.md) provides a sparse counterpart to the dense Cholesky routines `spotrf()` and `dpotrf()` from LAPACK.

## See Also

- [var SparseFactorizationLDLT: SparseFactorization_t](sparsefactorizationldlt.md)
  A constant that represents the default  factorization.
- [var SparseFactorizationLDLTUnpivoted: SparseFactorization_t](sparsefactorizationldltunpivoted.md)
  A constant that represents Cholesky-like  factorization with only one-by-one pivots and no pivoting.
- [var SparseFactorizationLDLTSBK: SparseFactorization_t](sparsefactorizationldltsbk.md)
  A constant that represents  factorization with Supernode-Bunch-Kaufman and static pivoting.
- [var SparseFactorizationLDLTTPP: SparseFactorization_t](sparsefactorizationldlttpp.md)
  A constant that represents  factorization with full-threshold partial pivoting.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactorizationcholesky)*