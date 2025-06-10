# structure

**Framework**: Accelerate  
**Kind**: property

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
var structure: SparseMatrixStructureComplex
```

#### Discussion

The sparsity structure is represented in  (block CSC) format. The matrix is divided into a regular grid of `rowCount x columnCount` blocks each of size `blockSize x blockSize`, and only blocks containing a non-zero entry are stored. CSC format is used to store the locations of these blocks. For each block column, a list of block row indices for non-zero blocks are stored, and the lists for each column are stored contiguously one after the other. Hence the row indices for column j are given by rowIndices`[columnStarts[j]:columnStarts[j+1]]`, where `columnStarts[]` is storing the location of the first index in each column.

If the blockSize is `1`, then this format is exactly equivalent to standard CSC format.

CSR format data can be simulated by using a blockSize of `1` and setting the transpose attribute (strictly this is still a transposed CSC matrix, so `rowCount` and `columnCount` will be transposed compared to true CSR).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrix_complex_float/structure)*