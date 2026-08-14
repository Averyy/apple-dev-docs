# SparseAttributesComplex_t

**Framework**: Accelerate  
**Kind**: struct

A type representing the attributes of a matrix.

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
struct SparseAttributesComplex_t
```

#### Overview

- **`transpose`**: If `true`, the matrix is implicitly transposed when used in any functions.
- **`triangle`**: If `kind` is `SparseOrdinary`, this field is ignored. Otherwise it indicates which triangle (upper or lower) represents the matrix.
- **`kind`**: Identifies the matrix as being full (`SparseOrdinary`), [unit-] triangular (`SparseTriangular`, `SparseUnitTriangular`), or symmetric (Hermitian) (`SparseSymmetric`, `SparseHermitian`).
- **`conjugate_transpose`**: If `true`, the matrix is implicitly conjugate transposed, otherwise it is simply transposed. This field has no meaning if `transpose` field is `false`.
- **`_reserved`**: for future expansion. Must be zero.
- **`_allocatedBySparse`**: an implementation detail. Should be zero for any matrix you allocate.

## Topics

### Initializers
- [init()](sparseattributescomplex_t/init.md)
### Instance Properties
- [var conjugate_transpose: Bool](sparseattributescomplex_t/conjugate_transpose.md)
- [var kind: SparseKind_t](sparseattributescomplex_t/kind.md)
  A flag to describe the type of matrix represented.
- [var transpose: Bool](sparseattributescomplex_t/transpose.md)
- [var triangle: SparseTriangle_t](sparseattributescomplex_t/triangle.md)
  A flag to indicate which triangle of a matrix is used.

## Relationships

### Conforms To
- [Sendable](../swift/sendable.md)

## See Also

- [struct SparseMatrix_Complex_Double](sparsematrix_complex_double.md)
  A type representing a sparse complex matrix.
- [struct SparseMatrix_Complex_Float](sparsematrix_complex_float.md)
  A type representing a sparse complex matrix.
- [struct SparseMatrixStructureComplex](sparsematrixstructurecomplex.md)
  A type representing the sparsity structure of a sparse complex matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseattributescomplex_t)*