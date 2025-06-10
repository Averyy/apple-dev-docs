# SparseAttributes_t

**Framework**: Accelerate  
**Kind**: struct

A structure that represents the attributes of a matrix.

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
struct SparseAttributes_t
```

## Mentions

- [Creating sparse matrices](creating-sparse-matrices.md)

## Topics

### Creating a New Attributes Structure
- [init()](sparseattributes_t/init.md)
  Returns a new sparse attributes structure.
### Instance Properties
- [var transpose: Bool](sparseattributes_t/transpose.md)
  A Boolean value that specifies whether to implicitly transpose the matrix.
- [var triangle: SparseTriangle_t](sparseattributes_t/triangle.md)
  An enumeration that specifies which triangle unit-triangular, triangular, and symmetric matrices need to use.
- [struct SparseTriangle_t](sparsetriangle_t.md)
  A structure that defines which triangle a symmetric matrix stores, or whether a triangular matrix is upper or lower.
- [var kind: SparseKind_t](sparseattributes_t/kind.md)
  An eumeration that specifies whether the matrix is ordinary, unit-triangular, triangular, or symmetric.
- [struct SparseKind_t](sparsekind_t.md)
  A structure that defines whether the matrix is ordinary, symmetric, or triangular.

## Relationships

### Conforms To
- [Sendable](../Swift/Sendable.md)

## See Also

- [var rowCount: Int32](densematrix_double/rowcount.md)
  The number of rows in the matrix.
- [var columnCount: Int32](densematrix_double/columncount.md)
  The number of columns in the matrix.
- [var columnStride: Int32](densematrix_double/columnstride.md)
  The stride between matrix columns, in elements.
- [var attributes: SparseAttributes_t](densematrix_double/attributes.md)
  The attributes of the matrix, such as whether it’s symmetrical or triangular.
- [var data: UnsafeMutablePointer<Double>](densematrix_double/data.md)
  The array of double-precision, floating-point values in column-major order.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseattributes_t)*