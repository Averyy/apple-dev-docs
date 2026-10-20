# reportError

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The function for reporting parameter errors.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
var reportError: ((UnsafePointer<CChar>) -> Void)?
```

```c
void (*)(const char *) reportError;
```

## Mentions

- [Solving systems using direct methods](../solving-systems-using-direct-methods.md)

#### Discussion

If this value is `nil`, the system reports errors using [`os_log_error`](../../os/os_log_error.md) and then `__builtin_trap()`.

## See Also

### Inspecting Symbolic Factor Options
- [var control: SparseControl_t](./control.md)
  The flags that control the computation.
- [struct SparseControl_t](../sparsecontrol_t.md)
  Options that control the computation.
- [var orderMethod: SparseOrder_t](./ordermethod.md)
  The ordering algorithm.
- [var order: UnsafeMutablePointer<Int32>?](./order.md)
  The user-supplied array for ordering.
- [struct SparseOrder_t](../sparseorder_t.md)
  Options that define which ordering algorithm to use.
- [var ignoreRowsAndColumns: UnsafeMutablePointer<Int32>?](./ignorerowsandcolumns.md)
  An array that contains row and column indices to ignore.
- [var malloc: (Int) -> UnsafeMutableRawPointer?](./malloc.md)
  The function for allocating any necessary storage.
- [var free: (UnsafeMutableRawPointer?) -> Void](./free.md)
  The function for freeing allocated storage.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesymbolicfactoroptions/reporterror)*