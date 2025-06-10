# SparseTriangular

**Framework**: Accelerate  
**Kind**: var

A triangular sparse matrix with a nonunit diagonal.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
var SparseTriangular: SparseKind_t { get }
```

## Mentions

- [Creating a sparse matrix from coordinate format arrays](creating-a-sparse-matrix-from-coordinate-format-arrays.md)

#### Discussion

The [`SparseTriangle_t`](sparsetriangle_t.md) field indicates which triangle (upper or lower) represents the matrix.

## See Also

- [var SparseOrdinary: SparseKind_t](sparseordinary.md)
  An unsymmetric sparse matrix without special structure.
- [var SparseSymmetric: SparseKind_t](sparsesymmetric.md)
  A symmetric sparse matrix.
- [var SparseUnitTriangular: SparseKind_t](sparseunittriangular.md)
  A triangular sparse matrix with a unit diagonal.
- [var SparseHermitian: SparseKind_t](sparsehermitian.md)
  A flag to describe the type of matrix represented.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsetriangular)*