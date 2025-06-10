# attributes

**Framework**: Accelerate  
**Kind**: property

The attributes of the matrix, such as whether it’s symmetrical or triangular.

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
var attributes: SparseAttributes_t
```

## Mentions

- [Creating sparse matrices](creating-sparse-matrices.md)

## See Also

- [var blockSize: UInt8](sparsematrixstructure/blocksize.md)
  The block size of the matrix.
- [var columnCount: Int32](sparsematrixstructure/columncount.md)
  The number of columns in the matrix.
- [var columnStarts: UnsafeMutablePointer<Int>](sparsematrixstructure/columnstarts.md)
  The starting index for each column in the row indices array.
- [var rowCount: Int32](sparsematrixstructure/rowcount.md)
  The number of rows in the matrix.
- [var rowIndices: UnsafeMutablePointer<Int32>](sparsematrixstructure/rowindices.md)
  The row indices of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrixstructure/attributes)*