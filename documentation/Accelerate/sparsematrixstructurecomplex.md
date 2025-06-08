# SparseMatrixStructureComplex

**Framework**: Accelerate  
**Kind**: struct

A type representing the sparsity structure of a sparse complex matrix.

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
struct SparseMatrixStructureComplex
```

#### Overview

The sparsity structure is represented in  (block CSC) format. The matrix is divided into a regular grid of `rowCount x columnCount` blocks each of size `blockSize x blockSize`, and only blocks containing a non-zero entry are stored. CSC format is used to store the locations of these blocks. For each block column, a list of block row indices for non-zero blocks are stored, and the lists for each column are stored contiguously one after the other. Hence the row indices for column j are given by rowIndices`[columnStarts[j]:columnStarts[j+1]]`, where `columnStarts[]` is storing the location of the first index in each column.

If the blockSize is `1`, then this format is exactly equivalent to standard CSC format.

CSR format data can be simulated by using a blockSize of `1` and setting the transpose attribute (strictly this is still a transposed CSC matrix, so `rowCount` and `columnCount` will be transposed compared to true CSR).

## Topics

### Initializers
- [init(rowCount: Int32, columnCount: Int32, columnStarts: UnsafeMutablePointer<Int>, rowIndices: UnsafeMutablePointer<Int32>, attributes: SparseAttributesComplex_t, blockSize: UInt8)](sparsematrixstructurecomplex/init(rowcount:columncount:columnstarts:rowindices:attributes:blocksize:).md)
### Instance Properties
- [var attributes: SparseAttributesComplex_t](sparsematrixstructurecomplex/attributes.md)
  A type representing the attributes of a matrix.
- [var blockSize: UInt8](sparsematrixstructurecomplex/blocksize.md)
- [var columnCount: Int32](sparsematrixstructurecomplex/columncount.md)
- [var columnStarts: UnsafeMutablePointer<Int>](sparsematrixstructurecomplex/columnstarts.md)
- [var rowCount: Int32](sparsematrixstructurecomplex/rowcount.md)
- [var rowIndices: UnsafeMutablePointer<Int32>](sparsematrixstructurecomplex/rowindices.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrixstructurecomplex)*