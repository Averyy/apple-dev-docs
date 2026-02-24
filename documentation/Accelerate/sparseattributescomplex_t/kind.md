# kind

**Framework**: Accelerate  
**Kind**: property

A flag to describe the type of matrix represented.

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
var kind: SparseKind_t { get set }
```

#### Discussion

A `SparseMatrixStructure` object can represent several types of matrices:

- **`SparseOrdinary`**: A “normal” sparse matrix without special structure.
- **`SparseTriangular`**: A triangular sparse matrix with non-unit diagonal. The `SparseTriangle_t:` field indicates which triangle (upper or lower) is used.
- **`SparseUnitTriangular`**: A triangular sparse matrix with unit diagonal. The `SparseTriangle_t`: field indicates which triangle (upper or lower) is used.
- **`SparseSymmetric`**: A symmetric  sparse matrix.  The `SparseTriangle_t` field indicates which triangle (upper or lower) is used to represent the matrix.
- **`SparseHermitian`**: A Hermitian  sparse matrix.  The `SparseTriangle_t` field indicates which triangle (upper or lower) is used to represent the matrix.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseattributescomplex_t/kind)*