# SparseScalingDefault

**Framework**: Accelerate  
**Kind**: var

Default scaling.

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
var SparseScalingDefault: SparseScaling_t { get }
```

#### Discussion

The default scaling is [`SparseScalingEquilibriationInf`](sparsescalingequilibriationinf.md) if , or no scaling if Cholesky.

## See Also

- [var SparseScalingUser: SparseScaling_t](sparsescalinguser.md)
  User scaling.
- [var SparseScalingEquilibriationInf: SparseScaling_t](sparsescalingequilibriationinf.md)
  The norm equilibration scaling using infinity norm.
- [var SparseOrderMTMetis: SparseOrder_t](sparseordermtmetis.md)
  Specifies type of fill-reducing ordering.
- [var SparseScalingHungarianScalingOnly: SparseScaling_t](sparsescalinghungarianscalingonly.md)
  Specifies type of scaling to be performed.
- [var SparseScalingHungarianScalingAndOrdering: SparseScaling_t](sparsescalinghungarianscalingandordering.md)
  Specifies type of scaling to be performed.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsescalingdefault)*