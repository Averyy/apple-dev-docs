# SparseRefactor(_:_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, using updated options and without any internal allocations.

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
func SparseRefactor(_ Matrix: SparseMatrix_Complex_Float, _ Factored: UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, _ nfoptions: SparseNumericFactorOptions, _ workspace: UnsafeMutableRawPointer)
```

#### Discussion

`Matrix` must have the same non-zero structure as that used for the original factorization.

This call provides very similar behavior to that which can be achieved by reusing explicit storage supplied to `SparseFactor` as the argument `factorStorage`. However, in addition to providing a simplified call sequence, this call can also reuse any additional storage allocated to accomodate delayed pivots.

Note that internal memory allocations may occur in the case of pivoted factorizations that result in delayed pivots. If you require closer control over memory allocations, supply an `sfoptions.malloc` function that implements the required behaviour, or use an alternative non-pivoted factorization returns. Note that if `sfoptions.malloc` returns NULL the factorization will abort immediately.

Note that if the reference count of the underlying object is not exactly one (i.e. if there are any implict copies as a result of calls to `SparseGetTranspose` or `SparseCreateSubfactor()` that have not been destroyed through a call to `SparseCleanup`), then new storage will be allocated regardless.

## Parameters

- `Matrix`: The matrix to be factorized.
- `nfoptions`: Numeric factor options, for example pivoting parameters.
- `workspace`: A pointer to a workspace of size at least    bytes.   This memory must be 16-byte aligned (any allocation returned   by   has this property).   This workspace may be reused or destroyed by the user as soon as the   function returns.

## See Also

- [func SparseRefactor(SparseMatrix_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-9mqeq.md)
  Computes a factorization of the specified double-precision matrix using an existing factorization’s storage, without internal memory allocation.
- [func SparseRefactor(SparseMatrix_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-2dqt8.md)
  Computes a factorization of the specified single-precision matrix using an existing factorization’s storage, without internal memory allocation.
- [func SparseRefactor(SparseMatrix_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Double>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-59ehf.md)
  Computes a factorization of the specified double-precision matrix using an existing factorization’s storage and specified options, and without internal memory allocation.
- [func SparseRefactor(SparseMatrix_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Float>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-8i8vi.md)
  Computes a factorization of the specified single-precision matrix using an existing factorization’s storage and specified options, and without internal memory allocation.
- [func SparseRefactor(SparseMatrix_Complex_Float, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Float>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-4ofvz.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex float values, without any internal allocations.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, UnsafeMutableRawPointer)](sparserefactor(_:_:_:)-593yb.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, without any internal allocations.
- [func SparseRefactor(SparseMatrix_Complex_Double, UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, SparseNumericFactorOptions, UnsafeMutableRawPointer)](sparserefactor(_:_:_:_:)-20xqc.md)
  Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, using updated options and without any internal allocations.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparserefactor(_:_:_:_:)-201rh)*