# SparseMatrixStructure

**Framework**: Accelerate  
**Kind**: struct

A description of the sparsity structure of a sparse matrix.

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
struct SparseMatrixStructure
```

## Mentions

- [Creating sparse matrices](creating-sparse-matrices.md)

#### Overview

The sparsity structure is in a  format. The matrix consists of [`rowCount`](sparsematrixstructure/rowcount.md) x [`columnCount`](sparsematrixstructure/columncount.md) blocks, each of which is a square matrix of some fixed size. The system stores this block size separately from the sparsity because the graph algorithms that operate on the structure don’t need it.

## Topics

### Creating a sparse matrix description
- [init(rowCount: Int32, columnCount: Int32, columnStarts: UnsafeMutablePointer<Int>, rowIndices: UnsafeMutablePointer<Int32>, attributes: SparseAttributes_t, blockSize: UInt8)](sparsematrixstructure/init(rowcount:columncount:columnstarts:rowindices:attributes:blocksize:).md)
  Creates a new structure that represents the sparsity structure of a sparse matrix.
### Inspecting the properties of a sparse matrix description
- [var attributes: SparseAttributes_t](sparsematrixstructure/attributes.md)
  The attributes of the matrix, such as whether it’s symmetrical or triangular.
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

## See Also

- [Creating sparse matrices](creating-sparse-matrices.md)
  Create sparse matrices for factorization and solving systems.
- [struct SparseAttributes_t](sparseattributes_t.md)
  A structure that represents the attributes of a matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrixstructure)*