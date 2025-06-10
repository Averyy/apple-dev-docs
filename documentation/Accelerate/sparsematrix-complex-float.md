# SparseMatrix_Complex_Float

**Framework**: Accelerate  
**Kind**: struct

A type representing a sparse complex matrix.

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
struct SparseMatrix_Complex_Float
```

#### Overview

`data` is the array of values in the non-zero blocks of the matrix stored contiguously, each block in column-major order. If there are `N` structural non-zero blocks in the matrix, `data` holds `blockSize * blockSize * N` doubles.

- term  `structure` The symbolic structure of the matrix.
- term  `data` The numerical values of the matrix. If `structure.blockSize > 1`, blocks are stored contiguously in column-major format.

## Topics

### Initializers
- [init(structure: SparseMatrixStructureComplex, data: OpaquePointer)](sparsematrix_complex_float/init(structure:data:).md)
### Instance Properties
- [var data: OpaquePointer](sparsematrix_complex_float/data.md)
- [var structure: SparseMatrixStructureComplex](sparsematrix_complex_float/structure.md)
  A type representing the sparsity structure of a sparse complex matrix.

## See Also

- [struct SparseMatrix_Complex_Double](sparsematrix_complex_double.md)
  A type representing a sparse complex matrix.
- [struct SparseAttributesComplex_t](sparseattributescomplex_t.md)
  A type representing the attributes of a matrix.
- [struct SparseMatrixStructureComplex](sparsematrixstructurecomplex.md)
  A type representing the sparsity structure of a sparse complex matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsematrix_complex_float)*