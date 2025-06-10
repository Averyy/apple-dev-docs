# SparseFactor(_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a symbolic factorization of the requested type for a complex matrix with the given structure.

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
func SparseFactor(_ type: SparseFactorization_t, _ Matrix: SparseMatrixStructureComplex) -> SparseOpaqueSymbolicFactorization
```

#### Return Value

The requested symbolic factorization of Matrix.

#### Discussion

The resulting symbolic factorization may be used for multiple numerical factorizations with different numerical values but the same non-zero structure.

## Parameters

- `type`: The type of factorization to perform.
- `Matrix`: The structure of the sparse matrix to be factorized.

## See Also

- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:)-1avkp.md)
  Returns the specified factorization of a sparse matrix of complex double values.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:)-5zzpu.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:)-73n38.md)
  Returns the specified factorization of a sparse matrix of complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:)-55tzk)*