# SparseOrderCOLAMD

**Framework**: Accelerate  
**Kind**: var

The column AMD ordering for .

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
var SparseOrderCOLAMD: SparseOrder_t { get }
```

#### Discussion

This ordering isn’t valid for symmetric factorizations (use [`SparseOrderAMD`](sparseorderamd.md) instead).

## See Also

- [var SparseOrderDefault: SparseOrder_t](sparseorderdefault.md)
  The default ordering.
- [var SparseOrderUser: SparseOrder_t](sparseorderuser.md)
  The user-supplied ordering, or identity if the order parameter is null.
- [var SparseOrderAMD: SparseOrder_t](sparseorderamd.md)
  Approximate minimum degree (AMD) ordering.
- [var SparseOrderMetis: SparseOrder_t](sparseordermetis.md)
  METIS nested dissection ordering.
- [var SparseOrderMTMetis: SparseOrder_t](sparseordermtmetis.md)
  Specifies type of fill-reducing ordering.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseordercolamd)*