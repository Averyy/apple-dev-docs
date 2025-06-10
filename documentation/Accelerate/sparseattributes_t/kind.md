# kind

**Framework**: Accelerate  
**Kind**: property

An eumeration that specifies whether the matrix is ordinary, unit-triangular, triangular, or symmetric.

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

## Mentions

- [Creating a sparse matrix from coordinate format arrays](creating-a-sparse-matrix-from-coordinate-format-arrays.md)

## See Also

- [var transpose: Bool](sparseattributes_t/transpose.md)
  A Boolean value that specifies whether to implicitly transpose the matrix.
- [var triangle: SparseTriangle_t](sparseattributes_t/triangle.md)
  An enumeration that specifies which triangle unit-triangular, triangular, and symmetric matrices need to use.
- [struct SparseTriangle_t](sparsetriangle_t.md)
  A structure that defines which triangle a symmetric matrix stores, or whether a triangular matrix is upper or lower.
- [struct SparseKind_t](sparsekind_t.md)
  A structure that defines whether the matrix is ordinary, symmetric, or triangular.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseattributes_t/kind)*