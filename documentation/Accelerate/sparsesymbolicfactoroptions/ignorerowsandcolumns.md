# ignoreRowsAndColumns

**Framework**: Accelerate  
**Kind**: property

An array that contains row and column indices to ignore.

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
var ignoreRowsAndColumns: UnsafeMutablePointer<Int32>?
```

#### Discussion

If this array isn’t `nil`, [`ignoreRowsAndColumns`](sparsesymbolicfactoroptions/ignorerowsandcolumns.md) provides a list of rows and columns to ignore. Terminate [`ignoreRowsAndColumns`](sparsesymbolicfactoroptions/ignorerowsandcolumns.md) with a negative index.

The row and column indices are for the actual matrix, not its block structure, so `0` indicates the first row, not the first `blockSize` rows.

In the symmetric case (Cholesky, ), each entry indicates that the system needs to ignore the matching row and column.

In the unsymmetric case (QR, Cholesky ), consider the matrix, `A`, given the value `m`, with one of the following definitions:

- `m = A.structure.rowCount * A.blockSize` if `A` isn’t a transposed matrix
- `m = A.structure.columnCount * A.blockSize` if `A` is a transposed matrix

In this case, an index less than `m` indicates that the system needs to ignore row `m`. An index `i`, greater than `m`, indicates that the system needs to ignore columns `i - m`.

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
- [var malloc: (Int) -> UnsafeMutableRawPointer?](sparsesymbolicfactoroptions/malloc.md)
  The function for allocating any necessary storage.
- [var free: (UnsafeMutableRawPointer?) -> Void](sparsesymbolicfactoroptions/free.md)
  The function for freeing allocated storage.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsesymbolicfactoroptions/reporterror.md)
  The function for reporting parameter errors.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsesymbolicfactoroptions/ignorerowsandcolumns)*