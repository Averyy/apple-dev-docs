# triangle

**Framework**: Accelerate  
**Kind**: property

A flag to indicate which triangle of a matrix is used.

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

- **`SparseUpperTriangle`**: For triangular and unit-triangular matrices, indicates that the upper triangle is to be used, and the lower triangle is implicitly zero. For symmetric (Hermitian) matrices, indicates that the upper triangle is to be used; the lower triangle is implicitly defined by reflection.
- **`SparseLowerTriangle`**: For triangular matrices, indicates that the lower triangle is to be used, and the upper triangle is implicitly zero. For symmetric (Hermitian) matrices, indicates that the lower triangle is to be used; the upper triangle is implicitly defined by reflection.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseattributescomplex_t/triangle)*