# malloc

**Framework**: Accelerate  
**Kind**: property

The function for allocating any necessary storage.

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
var malloc: (Int) -> UnsafeMutableRawPointer?
```

#### Return Value

A pointer to newly allocated memory, or `nil` if allocation fails.

#### Discussion

The system frees memory through the [`free`](sparsesymbolicfactoroptions/free.md) callback. If this function pointer is `nil`, the system uses `malloc()`.

## Parameters

- `size`: The size of space to allocate in bytes.

## See Also

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
- [var free: (UnsafeMutableRawPointer?) -> Void](sparsesymbolicfactoroptions/free.md)
  The function for freeing allocated storage.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsesymbolicfactoroptions/reporterror.md)
  The function for reporting parameter errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesymbolicfactoroptions/malloc)*