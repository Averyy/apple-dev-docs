# SparseSymbolicFactorOptions

**Framework**: Accelerate  
**Kind**: struct

A structure that contains options that affect the symbolic stage of a sparse factorization.

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
struct SparseSymbolicFactorOptions
```

## Mentions

- [Solving systems using direct methods](solving-systems-using-direct-methods.md)

#### Overview

[`SparseSymbolicFactorOptions`](sparsesymbolicfactoroptions.md) supports the following ordering algorithms:

| [`SparseOrderDefault`](sparseorderdefault.md) | The default ordering ([`SparseOrderAMD`](sparseorderamd.md) for symmetric and [`SparseOrderCOLAMD`](sparseordercolamd.md) for unsymmetric factorizations). |
| --- | --- |
| [`SparseOrderUser`](sparseorderuser.md) | The user-supplied ordering, or identity if [`order`](sparsesymbolicfactoroptions/order.md) is `null`. |
| [`SparseOrderAMD`](sparseorderamd.md) | Approximate minimum degree (AMD) ordering. There’s a large overhead cost if you use it for QR-based factorization due to explicit formation of . |
| [`SparseOrderMetis`](sparseordermetis.md) | METIS nested dissection ordering. There’s a large overhead cost if you use it for QR-based factorization due to explicit formation of . |
| [`SparseOrderCOLAMD`](sparseordercolamd.md) | The column AMD ordering for . This isn’t valid for symmetric factorizations (use [`SparseOrderAMD`](sparseorderamd.md) instead). |

## Topics

### Creating a Symbolic Factor Options Structure
- [init(control: SparseControl_t, orderMethod: SparseOrder_t, order: UnsafeMutablePointer<Int32>?, ignoreRowsAndColumns: UnsafeMutablePointer<Int32>?, malloc: (Int) -> UnsafeMutableRawPointer?, free: (UnsafeMutableRawPointer?) -> Void, reportError: ((UnsafePointer<CChar>) -> Void)?)](sparsesymbolicfactoroptions/init(control:ordermethod:order:ignorerowsandcolumns:malloc:free:reporterror:).md)
  Creates a new structure that contains options that affect the symbolic stage of a sparse factorization.
### Inspecting Symbolic Factor Options
- [var control: SparseControl_t](sparsesymbolicfactoroptions/control.md)
  The flags that control the computation.
- [struct SparseControl_t](sparsecontrol_t.md)
  Options that control the computation.
- [var orderMethod: SparseOrder_t](sparsesymbolicfactoroptions/ordermethod.md)
  The ordering algorithm.
- [var order: UnsafeMutablePointer<Int32>?](sparsesymbolicfactoroptions/order.md)
  The user-supplied array for ordering.
- [struct SparseOrder_t](sparseorder_t.md)
  Options that define which ordering algorithm to use.
- [var ignoreRowsAndColumns: UnsafeMutablePointer<Int32>?](sparsesymbolicfactoroptions/ignorerowsandcolumns.md)
  An array that contains row and column indices to ignore.
- [var malloc: (Int) -> UnsafeMutableRawPointer?](sparsesymbolicfactoroptions/malloc.md)
  The function for allocating any necessary storage.
- [var free: (UnsafeMutableRawPointer?) -> Void](sparsesymbolicfactoroptions/free.md)
  The function for freeing allocated storage.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsesymbolicfactoroptions/reporterror.md)
  The function for reporting parameter errors.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)

## See Also

- [struct SparseOrder_t](sparseorder_t.md)
  Options that define which ordering algorithm to use.
- [struct SparseFactorization_t](sparsefactorization_t.md)
  Constants that define the factorization type.
- [struct SparseNumericFactorOptions](sparsenumericfactoroptions.md)
  A structure that contains options that affect the numerical stage of a sparse factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesymbolicfactoroptions)*