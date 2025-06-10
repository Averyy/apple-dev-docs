# reportError

**Framework**: Accelerate  
**Kind**: property

The function for reporting parameter errors.

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
var reportError: ((UnsafePointer<CChar>) -> Void)?
```

## Mentions

- [Solving systems using direct methods](solving-systems-using-direct-methods.md)

#### Discussion

If this value is `nil`, the system reports errors using [`os_log_error`](https://developer.apple.com/documentation/os/os_log_error) and then `__builtin_trap()`.

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
- [var malloc: (Int) -> UnsafeMutableRawPointer?](sparsesymbolicfactoroptions/malloc.md)
  The function for allocating any necessary storage.
- [var free: (UnsafeMutableRawPointer?) -> Void](sparsesymbolicfactoroptions/free.md)
  The function for freeing allocated storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesymbolicfactoroptions/reporterror)*