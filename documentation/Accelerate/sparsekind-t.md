# SparseKind_t

**Framework**: Accelerate  
**Kind**: struct

A structure that defines whether the matrix is ordinary, symmetric, or triangular.

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
struct SparseKind_t
```

## Topics

### Constants
- [var SparseOrdinary: SparseKind_t](sparseordinary.md)
  An unsymmetric sparse matrix without special structure.
- [var SparseSymmetric: SparseKind_t](sparsesymmetric.md)
  A symmetric sparse matrix.
- [var SparseTriangular: SparseKind_t](sparsetriangular.md)
  A triangular sparse matrix with a nonunit diagonal.
- [var SparseUnitTriangular: SparseKind_t](sparseunittriangular.md)
  A triangular sparse matrix with a unit diagonal.
- [var SparseHermitian: SparseKind_t](sparsehermitian.md)
  A flag to describe the type of matrix represented.
### Raw Values
- [init(UInt32)](sparsekind_t/init(_:).md)
- [init(rawValue: UInt32)](sparsekind_t/init(rawvalue:).md)
- [var rawValue: UInt32](sparsekind_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [var transpose: Bool](sparseattributes_t/transpose.md)
  A Boolean value that specifies whether to implicitly transpose the matrix.
- [var triangle: SparseTriangle_t](sparseattributes_t/triangle.md)
  An enumeration that specifies which triangle unit-triangular, triangular, and symmetric matrices need to use.
- [struct SparseTriangle_t](sparsetriangle_t.md)
  A structure that defines which triangle a symmetric matrix stores, or whether a triangular matrix is upper or lower.
- [var kind: SparseKind_t](sparseattributes_t/kind.md)
  An eumeration that specifies whether the matrix is ordinary, unit-triangular, triangular, or symmetric.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsekind_t)*