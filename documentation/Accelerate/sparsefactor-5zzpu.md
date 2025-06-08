# SparseFactor(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization.

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
func SparseFactor(_ SymbolicFactor: SparseOpaqueSymbolicFactorization, _ Matrix: SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double
```

#### Return Value

Factorization of Matrix.

#### Discussion

- Parameter SymbolicFactor A symbolic factorization, as returned by a call of the form `SymbolicFactor = SparseFactor(Matrix.structure)`.
- Parameter Matrix The matrix to factorize.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:)-5zzpu)*