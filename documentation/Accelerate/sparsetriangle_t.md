# SparseTriangle_t

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

A structure that defines which triangle a symmetric matrix stores, or whether a triangular matrix is upper or lower.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct SparseTriangle_t
```

```c
typedef enum { ... } SparseTriangle_t;
```

## Topics

### Constants
- [var SparseLowerTriangle: SparseTriangle_t](./sparselowertriangle.md)
  A constant that specifies the lower triangle.
- [var SparseUpperTriangle: SparseTriangle_t](./sparseuppertriangle.md)
  A constant that specifies the upper triangle.
### Raw Values
- [init(UInt8)](./sparsetriangle_t/init%28_%29.md)
- [init(rawValue: UInt8)](./sparsetriangle_t/init%28rawvalue%29.md)
- [var rawValue: UInt8](./sparsetriangle_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Instance Properties
- [var transpose: Bool](./sparseattributes_t/transpose.md)
  A Boolean value that specifies whether to implicitly transpose the matrix.
- [var triangle: SparseTriangle_t](./sparseattributes_t/triangle.md)
  An enumeration that specifies which triangle unit-triangular, triangular, and symmetric matrices need to use.
- [var kind: SparseKind_t](./sparseattributes_t/kind.md)
  An eumeration that specifies whether the matrix is ordinary, unit-triangular, triangular, or symmetric.
- [struct SparseKind_t](./sparsekind_t.md)
  A structure that defines whether the matrix is ordinary, symmetric, or triangular.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsetriangle_t)*