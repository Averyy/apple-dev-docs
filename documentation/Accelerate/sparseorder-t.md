# SparseOrder_t

**Framework**: Accelerate  
**Kind**: struct

Options that define which ordering algorithm to use.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct SparseOrder_t
```

#### Overview

The column and row ordering you use when eliminating variables in a sparse factorization has a significant influence on the size of the resulting factors and the amount of work necessary to calculate them. Minimizing the size or the amount of work is an NP-complete problem, so the system only implements heuristics in this library.

Approximate minimum degree (AMD)-based orderings tend to be fast and provide good quality for small matrices. Conversely, nested dissection-based orderings, such as METIS, are usually considerably slower to compute, but provide better quality orderings for larger problems, and expose more parallelism during the factorization. Use AMD unless the problem is very large (millions of rows and columns) to avoid performing many repeated factorizations. If you’re uncertain, try both and see which gives better performance for your usage.

AMD and METIS provide good orderings for symmetric matrices. You can use them for QR factorizations, but that involves forming  explicitly, which is expensive. Alternatively, column AMD (COLAMD) finds an ordering for  while only working with . For this reason, you can’t use COLAMD for symmetric factorizations.

## Topics

### Constants
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
- [var SparseOrderCOLAMD: SparseOrder_t](sparseordercolamd.md)
  The column AMD ordering for .
### Raw Values
- [init(UInt8)](sparseorder_t/init(_:).md)
- [init(rawValue: UInt8)](sparseorder_t/init(rawvalue:).md)
- [var rawValue: UInt8](sparseorder_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var control: SparseControl_t](sparsesymbolicfactoroptions/control.md)
  The flags that control the computation.
- [struct SparseControl_t](sparsecontrol_t.md)
  Options that control the computation.
- [var orderMethod: SparseOrder_t](sparsesymbolicfactoroptions/ordermethod.md)
  The ordering algorithm.
- [var order: UnsafeMutablePointer<Int32>?](sparsesymbolicfactoroptions/order.md)
  The user-supplied array for ordering.
- [var ignoreRowsAndColumns: UnsafeMutablePointer<Int32>?](sparsesymbolicfactoroptions/ignorerowsandcolumns.md)
  An array that contains row and column indices to ignore.
- [var malloc: (Int) -> UnsafeMutableRawPointer?](sparsesymbolicfactoroptions/malloc.md)
  The function for allocating any necessary storage.
- [var free: (UnsafeMutableRawPointer?) -> Void](sparsesymbolicfactoroptions/free.md)
  The function for freeing allocated storage.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsesymbolicfactoroptions/reporterror.md)
  The function for reporting parameter errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseorder_t)*