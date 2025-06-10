# SparseFactor(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization, using the specified options.

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
func SparseFactor(_ SymbolicFactor: SparseOpaqueSymbolicFactorization, _ Matrix: SparseMatrix_Complex_Double, _ nfoptions: SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Double
```

#### Return Value

Factorization of Matrix.

## Parameters

- `SymbolicFactor`: A symbolic factorization, as returned by a call of the   form  .
- `Matrix`: The matrix to factorize.
- `nfoptions`: Numeric factor options, for example pivoting parameters.

## See Also

- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:)-7a3l4.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization.
- [func SparseFactor(SparseFactorization_t, SparseMatrixStructureComplex, SparseSymbolicFactorOptions) -> SparseOpaqueSymbolicFactorization](sparsefactor(_:_:_:)-6s9g.md)
  Returns a symbolic factorization of the requested type for a complex matrix with the given structure, with the supplied options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:)-7kqvi.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:_:)-6hqfp.md)
  Returns the specified factorization of a sparse matrix of complex double values, using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:_:)-9ykfp.md)
  Returns the specified factorization of a sparse matrix of complex float values, using the specified options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:_:_:)-2dqfv.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:_:_:)-7j0dm.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:_:)-9ypz5)*