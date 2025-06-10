# transpose

**Framework**: Accelerate  
**Kind**: property

A Boolean value that specifies whether to implicitly transpose the matrix.

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
var transpose: Bool { get set }
```

#### Discussion

If [`true`](https://developer.apple.com/documentation/swift/true), the system implicitly transposes the matrix when it uses it in any functions.

## See Also

- [var triangle: SparseTriangle_t](sparseattributes_t/triangle.md)
  An enumeration that specifies which triangle unit-triangular, triangular, and symmetric matrices need to use.
- [struct SparseTriangle_t](sparsetriangle_t.md)
  A structure that defines which triangle a symmetric matrix stores, or whether a triangular matrix is upper or lower.
- [var kind: SparseKind_t](sparseattributes_t/kind.md)
  An eumeration that specifies whether the matrix is ordinary, unit-triangular, triangular, or symmetric.
- [struct SparseKind_t](sparsekind_t.md)
  A structure that defines whether the matrix is ordinary, symmetric, or triangular.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseattributes_t/transpose)*