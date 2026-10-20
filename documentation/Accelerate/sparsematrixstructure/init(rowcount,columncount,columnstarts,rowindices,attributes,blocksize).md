# init(rowCount:columnCount:columnStarts:rowIndices:attributes:blockSize:)

**Framework**: Accelerate  
**Kind**: init

Creates a new structure that represents the sparsity structure of a sparse matrix.

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
init(rowCount: Int32, columnCount: Int32, columnStarts: UnsafeMutablePointer<Int>, rowIndices: UnsafeMutablePointer<Int32>, attributes: SparseAttributes_t, blockSize: UInt8)
```

## Parameters

- `rowCount`: The number of rows in the matrix.
- `columnCount`: The number of columns in the matrix.
- `columnStarts`: An array that specifies where each column starts in the row indices array. This array requires an additional, final entry that defines the final column’s length.
- `rowIndices`: The row indices of the matrix.
- `attributes`: The attributes of the matrix, such as whether it’s symmetrical or triangular.
- `blockSize`: The block size of the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrixstructure/init(rowcount:columncount:columnstarts:rowindices:attributes:blocksize:))*