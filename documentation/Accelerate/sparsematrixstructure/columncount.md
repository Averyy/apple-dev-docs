# columnCount

**Framework**: Accelerate  
**Kind**: property

The number of columns in the matrix.

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
var columnCount: Int32
```

## See Also

- [var attributes: SparseAttributes_t](sparsematrixstructure/attributes.md)
  The attributes of the matrix, such as whether it’s symmetrical or triangular.
- [var blockSize: UInt8](sparsematrixstructure/blocksize.md)
  The block size of the matrix.
- [var columnStarts: UnsafeMutablePointer<Int>](sparsematrixstructure/columnstarts.md)
  The starting index for each column in the row indices array.
- [var rowCount: Int32](sparsematrixstructure/rowcount.md)
  The number of rows in the matrix.
- [var rowIndices: UnsafeMutablePointer<Int32>](sparsematrixstructure/rowindices.md)
  The row indices of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrixstructure/columncount)*