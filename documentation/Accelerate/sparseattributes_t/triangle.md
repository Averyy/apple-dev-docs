# triangle

**Framework**: Accelerate  
**Kind**: property

An enumeration that specifies which triangle unit-triangular, triangular, and symmetric matrices need to use.

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
var triangle: SparseTriangle_t { get set }
```

#### Discussion

If [`kind`](sparseattributes_t/kind.md) is [`SparseOrdinary`](sparseordinary.md), this operation ignores this propoerty. Otherwise, it indicates which triangle ([`SparseUpperTriangle`](sparseuppertriangle.md) or [`SparseLowerTriangle`](sparselowertriangle.md)) represents the matrix.

## See Also

- [var transpose: Bool](sparseattributes_t/transpose.md)
  A Boolean value that specifies whether to implicitly transpose the matrix.
- [struct SparseTriangle_t](sparsetriangle_t.md)
  A structure that defines which triangle a symmetric matrix stores, or whether a triangular matrix is upper or lower.
- [var kind: SparseKind_t](sparseattributes_t/kind.md)
  An eumeration that specifies whether the matrix is ordinary, unit-triangular, triangular, or symmetric.
- [struct SparseKind_t](sparsekind_t.md)
  A structure that defines whether the matrix is ordinary, symmetric, or triangular.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseattributes_t/triangle)*