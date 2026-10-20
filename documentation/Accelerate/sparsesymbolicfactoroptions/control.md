# control

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The flags that control the computation.

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
var control: SparseControl_t
```

```c
SparseControl_t control;
```

## See Also

### Inspecting Symbolic Factor Options
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
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  The function for reporting parameter errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesymbolicfactoroptions/control)*