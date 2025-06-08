# SparseFactor(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the specified factorization of a sparse matrix of complex double values.

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```swift
func SparseFactor(_ type: SparseFactorization_t, _ Matrix: SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double
```

## Parameters

- `type`: The type of factorization to perform.
- `Matrix`: The matrix to factorize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:)-1avkp)*