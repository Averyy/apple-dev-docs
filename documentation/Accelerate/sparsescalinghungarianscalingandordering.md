# SparseScalingHungarianScalingAndOrdering

**Framework**: Accelerate  
**Kind**: var

Scaling and ordering using the Hungarian algorithm.

**Availability**:
- iOS 26.0+
- iPadOS 26.0+
- Mac Catalyst 26.0+
- macOS 26.0+
- tvOS 26.0+
- visionOS 26.0+
- watchOS 26.0+

## Declaration

```swift
var SparseScalingHungarianScalingAndOrdering: SparseScaling_t { get }
```

#### Discussion

The Sparse Solvers library uses the associated matching to place large entries on the diagonal. This option is only valid if you use a combined symbolic and numeric call to `SparseFactor`()`. The Sparse Solvers library only supports this option for LU factorizations.

This algorithm is similar to MC64.

## See Also

- [var SparseScalingDefault: SparseScaling_t](sparsescalingdefault.md)
  Default scaling.
- [var SparseScalingUser: SparseScaling_t](sparsescalinguser.md)
  User scaling.
- [var SparseScalingEquilibriationInf: SparseScaling_t](sparsescalingequilibriationinf.md)
  The norm equilibration scaling using infinity norm.
- [var SparseScalingHungarianScalingOnly: SparseScaling_t](sparsescalinghungarianscalingonly.md)
  Scaling using the Hungarian algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsescalinghungarianscalingandordering)*