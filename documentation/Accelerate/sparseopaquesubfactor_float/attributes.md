# attributes

**Framework**: Accelerate  
**Kind**: property

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
var attributes: SparseAttributes_t
```

#### Discussion

- **`transpose`**: If `true`, the matrix is implicitly transposed when used in any functions.
- **`triangle`**: If `kind` is `SparseOrdinary`, this field is ignored. Otherwise it indicates which triangle (upper or lower) represents the matrix.
- **`kind`**: Identifies the matrix as being full (`SparseOrdinary`), [unit-] triangular (`SparseTriangular`, `SparseUnitTriangular`), or symmetric (Hermitian) (`SparseSymmetric`, `SparseHermitian`).
- **`_reserved`**: for future expansion. Must be zero.
- **`_allocatedBySparse`**: an implementation detail. Should be zero for any matrix you allocate.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseopaquesubfactor_float/attributes)*