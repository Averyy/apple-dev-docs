# SparseRefactor(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Reuses supplied factorization object’s storage to compute a new factorization of the supplied matrix of complex double values, using different options.

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
func SparseRefactor(_ Matrix: SparseMatrix_Complex_Double, _ Factorization: UnsafeMutablePointer<SparseOpaqueFactorization_Complex_Double>, _ nfoptions: SparseNumericFactorOptions)
```

#### Discussion

`Matrix` must have the same non-zero structure as that used for the original factorization.

This call provides very similar behavior to that which can be achieved by reusing explicit storage supplied to `SparseFactor` as the argument `factorStorage`. However, in addition to providing a simplified call sequence, this call can also reuse any additional storage allocated to accomodate delayed pivots.

Note that if the reference count of the underlying object is not exactly one (i.e. if there are any implict copies as a result of calls to `SparseGetTranspose` or `SparseCreateSubfactor()` that have not been destroyed through a call to `SparseCleanup`), then new storage will be allocated regardless.

## Parameters

- `Matrix`: The matrix to be factorized.
- `Factorization`: The factorization to be updated.
- `nfoptions`: Numeric factor options, for example pivoting parameters.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparserefactor(_:_:_:)-q0va)*