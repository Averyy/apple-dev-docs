# SparseFactor(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
static SparseOpaqueSymbolicFactorization SparseFactor(SparseFactorization_t type, SparseMatrixStructureComplex Matrix);
```

## Return Value

The requested symbolic factorization of Matrix.

## Discussion

The resulting symbolic factorization may be used for multiple numerical factorizations with different numerical values but the same non-zero structure.

## Parameters

- `type`: The type of factorization to perform.
- `Matrix`: The structure of the sparse matrix to be factorized.

## See Also

### Complex matrix factorization functions
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](./sparsefactor%28_,_%29-1avkp.md)
  Returns the specified factorization of a sparse matrix of complex double values.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](./sparsefactor%28_,_%29-5zzpu.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](./sparsefactor%28_,_%29-73n38.md)
  Returns the specified factorization of a sparse matrix of complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:)-55tzk)*