# SparseOrderMTMetis

**Framework**: Accelerate  
**Kind**: var

Specifies type of fill-reducing ordering.

**Availability**:
- iOS 26.0+ (Beta)
- iPadOS 26.0+ (Beta)
- Mac Catalyst 26.0+ (Beta)
- macOS 26.0+ (Beta)
- tvOS 26.0+ (Beta)
- visionOS 26.0+ (Beta)
- watchOS 26.0+ (Beta)

## Declaration

```swift
var SparseOrderMTMetis: SparseOrder_t { get }
```

#### Discussion

The order in which variables are eliminated (i.e. the column/row ordering) in a sparse factorization makes a big difference to the size of the resulting factors and amount of work required to calculate them (it is probably the biggest single factor). Minimizing the size or work required is an NP-complete problem, so only heuristics are implemented in this library.

We note that AMD-based orderings tend to be fast and provide good quality for small matrices, whilst nested dissection based orderings (such as metis) are normally considerably slower to compute, but provide better quality orderings for larger problems, and expose more parallelism during the factorization. We recommend AMD is used unless the problem is very large (millions of rows and columns) or you will perform many repeated factorizations. If you are uncertain, try both and see which gives better performance for your usage.

The AMD and MeTiS orderings provide good orderings for symmetric (Hermitian) matrices. They can be used for the QR factorizations, but this involves forming A^TA explicitly, which is expensive. COLAMD on the other hand finds an ordering for `A^T A` whilst only working with A. For this reason, COLAMD cannot be used for symmetric (Hermitian) factorizations.

## See Also

- [var SparseScalingDefault: SparseScaling_t](sparsescalingdefault.md)
  Default scaling.
- [var SparseScalingUser: SparseScaling_t](sparsescalinguser.md)
  User scaling.
- [var SparseScalingEquilibriationInf: SparseScaling_t](sparsescalingequilibriationinf.md)
  The norm equilibration scaling using infinity norm.
- [var SparseScalingHungarianScalingOnly: SparseScaling_t](sparsescalinghungarianscalingonly.md)
  Specifies type of scaling to be performed.
- [var SparseScalingHungarianScalingAndOrdering: SparseScaling_t](sparsescalinghungarianscalingandordering.md)
  Specifies type of scaling to be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseordermtmetis)*