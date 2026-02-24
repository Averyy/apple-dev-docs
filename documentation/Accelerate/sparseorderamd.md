# SparseOrderAMD

**Framework**: Accelerate  
**Kind**: var

Approximate minimum degree (AMD) ordering.

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
var SparseOrderAMD: SparseOrder_t { get }
```

#### Discussion

There’s a large overhead cost if you use this for QR-based factorization due to explicit formation of *AᵀA*.

## See Also

- [var SparseOrderDefault: SparseOrder_t](sparseorderdefault.md)
  The default ordering.
- [var SparseOrderUser: SparseOrder_t](sparseorderuser.md)
  The user-supplied ordering, or identity if the order parameter is null.
- [var SparseOrderMetis: SparseOrder_t](sparseordermetis.md)
  METIS nested dissection ordering.
- [var SparseOrderMTMetis: SparseOrder_t](sparseordermtmetis.md)
  Specifies type of fill-reducing ordering.
- [var SparseOrderCOLAMD: SparseOrder_t](sparseordercolamd.md)
  The column AMD ordering for *AᵀA*.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseorderamd)*