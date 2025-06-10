# SparseRefactor(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, using different options.

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
func SparseRefactor(_ Matrix: SparseMatrix_Complex_Float, _ Factorization: UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, _ nfoptions: SparseNumericFactorOptions)
```

#### Discussion

`Matrix` must have the same non-zero structure as that used for the original factorization.

This call provides very similar behavior to that which can be achieved by reusing explicit storage supplied to `SparseFactor` as the argument `factorStorage`. However, in addition to providing a simplified call sequence, this call can also reuse any additional storage allocated to accomodate delayed pivots.

Note that if the reference count of the underlying object is not exactly one (i.e. if there are any implict copies as a result of calls to `SparseGetTranspose` or `SparseCreateSubfactor()` that have not been destroyed through a call to `SparseCleanup`), then new storage will be allocated regardless.

## Parameters

- `Matrix`: The matrix to be factorized.
- `Factorization`: The factorization to be updated.
- `nfoptions`: Numeric factor options, for example pivoting parameters.

## See Also

- [func SparseRefactor(SparseMatrix_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Double>)](sparserefactor(_:_:)-8vrf5.md)
  Computes a factorization of the specified double-precision matrix using an existing factorization’s storage.
- [func SparseRefactor(SparseMatrix_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Float>)](sparserefactor(_:_:)-21q4x.md)
  Computes a factorization of the specified single-precision matrix using an existing factorization’s storage.
- [func SparseRefactor(SparseMatrix_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-6ttkd.md)
  Computes a factorization of the specified double-precision matrix using an existing factorization’s storage and specified options.
- [func SparseRefactor(SparseMatrix_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-2ovxs.md)
  Computes a factorization of the specified single-precision matrix using an existing factorization’s storage and specified options.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>)](sparserefactor(_:_:)-mgni.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>)](sparserefactor(_:_:)-zegz.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, SparseNumericFactorOptions)](sparserefactor(_:_:_:)-q0va.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, using different options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparserefactor(_:_:_:)-4chx2)*