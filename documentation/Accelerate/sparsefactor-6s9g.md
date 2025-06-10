# SparseFactor(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Returns a symbolic factorization of the requested type for a complex matrix with the given structure, with the supplied options.

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
func SparseFactor(_ type: SparseFactorization_t, _ MatrixComplex: SparseMatrixStructureComplex, _ options: SparseSymbolicFactorOptions) -> SparseOpaqueSymbolicFactorization
```

#### Return Value

The requested symbolic factorization of Matrix.

#### Discussion

The resulting symbolic factorization may be used for multiple numerical factorizations with different numerical values but the same non-zero structure.

## Parameters

- `type`: The type of factorization to perform.

## See Also

- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:)-7a3l4.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:)-7kqvi.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:)-9ypz5.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization, using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Double, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:_:)-6hqfp.md)
  Returns the specified factorization of a sparse matrix of complex double values, using the specified options.
- [func SparseFactor(SparseFactorization_t, SparseMatrix_Complex_Float, SparseSymbolicFactorOptions, SparseNumericFactorOptions) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:_:)-9ykfp.md)
  Returns the specified factorization of a sparse matrix of complex float values, using the specified options.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Float, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Float](sparsefactor(_:_:_:_:_:)-2dqfv.md)
  Returns the factorization of a sparse matrix of complex float values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.
- [func SparseFactor(SparseOpaqueSymbolicFactorization, SparseMatrix_Complex_Double, SparseNumericFactorOptions, UnsafeMutableRawPointer?, UnsafeMutableRawPointer?) -> SparseOpaqueFactorization_Complex_Double](sparsefactor(_:_:_:_:_:)-7j0dm.md)
  Returns the factorization of a sparse matrix of complex double values corresponding to the supplied symbolic factorization, using the specified options and without any internal memory allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsefactor(_:_:_:)-6s9g)*