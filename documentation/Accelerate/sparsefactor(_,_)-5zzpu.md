# SparseFactor(_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

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

```c
static SparseOpaqueFactorization_Complex_Double SparseFactor(SparseOpaqueSymbolicFactorization SymbolicFactor, SparseMatrix_Complex_Double Matrix);
```

#### Return Value

Factorization of Matrix.

#### Discussion

- Parameter SymbolicFactor A symbolic factorization, as returned by a call of the form `SymbolicFactor = SparseFactor(Matrix.structure)`.
- Parameter Matrix The matrix to factorize.

## See Also

### Complex matrix factorization functions
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](./sparsefactor%28_,_%29-1avkp.md)
  Returns the specified factorization of a sparse matrix of complex double values.
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructureComplex) -> SparseOpaqueSymbolicFactorization](./sparsefactor%28_,_%29-55tzk.md)
  Returns a symbolic factorization of the requested type for a complex matrix with the given structure.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](./sparsefactor%28_,_%29-73n38.md)
  Returns the specified factorization of a sparse matrix of complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:)-5zzpu)*