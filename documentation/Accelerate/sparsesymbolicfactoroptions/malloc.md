# malloc

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The function for allocating any necessary storage.

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
var malloc: (Int) -> UnsafeMutableRawPointer?
```

```c
void *(*)(unsigned long) malloc;
```

#### Return Value

A pointer to newly allocated memory, or `nil` if allocation fails.

#### Discussion

The system frees memory through the [`free`](./free.md) callback. If this function pointer is `nil`, the system uses `malloc()`.

## Parameters

- `size`: The size of space to allocate in bytes.

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
- [var free: (UnsafeMutableRawPointer?) -> Void](./free.md)
  The function for freeing allocated storage.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  The function for reporting parameter errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesymbolicfactoroptions/malloc)*