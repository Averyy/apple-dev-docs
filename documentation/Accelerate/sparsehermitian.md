# SparseHermitian

**Framework**: Accelerate  
**Kind**: var

A flag to describe the type of matrix represented.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
var SparseHermitian: SparseKind_t { get }
```

#### Discussion

A `SparseMatrixStructure` object can represent several types of matrices:

- **`SparseOrdinary`**: A “normal” sparse matrix without special structure.
- **`SparseTriangular`**: A triangular sparse matrix with non-unit diagonal. The `SparseTriangle_t:` field indicates which triangle (upper or lower) is used.
- **`SparseUnitTriangular`**: A triangular sparse matrix with unit diagonal. The `SparseTriangle_t`: field indicates which triangle (upper or lower) is used.
- **`SparseSymmetric`**: A symmetric  sparse matrix.  The `SparseTriangle_t` field indicates which triangle (upper or lower) is used to represent the matrix.
- **`SparseHermitian`**: A Hermitian  sparse matrix.  The `SparseTriangle_t` field indicates which triangle (upper or lower) is used to represent the matrix.

## See Also

- [var SparseOrdinary: SparseKind_t](sparseordinary.md)
  An unsymmetric sparse matrix without special structure.
- [var SparseSymmetric: SparseKind_t](sparsesymmetric.md)
  A symmetric sparse matrix.
- [var SparseTriangular: SparseKind_t](sparsetriangular.md)
  A triangular sparse matrix with a nonunit diagonal.
- [var SparseUnitTriangular: SparseKind_t](sparseunittriangular.md)
  A triangular sparse matrix with a unit diagonal.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsehermitian)*