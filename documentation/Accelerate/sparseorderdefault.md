# SparseOrderDefault

**Framework**: Accelerate  
**Kind**: var

The default ordering.

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
var SparseOrderDefault: SparseOrder_t { get }
```

#### Discussion

The default ordering is [`SparseOrderAMD`](sparseorderamd.md) for symmetric and [`SparseOrderCOLAMD`](sparseordercolamd.md) for unsymmetric factorizations.

## See Also

- [var SparseOrderUser: SparseOrder_t](sparseorderuser.md)
  The user-supplied ordering, or identity if the order parameter is null.
- [var SparseOrderAMD: SparseOrder_t](sparseorderamd.md)
  Approximate minimum degree (AMD) ordering.
- [var SparseOrderMetis: SparseOrder_t](sparseordermetis.md)
  METIS nested dissection ordering.
- [var SparseOrderCOLAMD: SparseOrder_t](sparseordercolamd.md)
  The column AMD ordering for .


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseorderdefault)*