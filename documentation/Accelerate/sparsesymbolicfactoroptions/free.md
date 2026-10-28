# free

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The function for freeing allocated storage.

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
var free: (UnsafeMutableRawPointer?) -> Void
```

```c
void (*)(void *) free;
```

## Discussion

If this function pointer is `nil`, the system uses `free``()`.

## Parameters

- `pointer`: A pointer to memory to free.

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
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  The function for reporting parameter errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesymbolicfactoroptions/free)*