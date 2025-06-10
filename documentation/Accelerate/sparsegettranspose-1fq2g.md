# SparseGetTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Float`.

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
func SparseGetTranspose(_ Factor: SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float
```

#### Return Value

A matrix factorization of `A^T`, where the original was of `A`. As this is reference counted, it must be freed through a call to `SparseCleanup` once it is no longer required.

## Parameters

- `Factor`: The factorization to transpose.

## See Also

- [func SparseGetTranspose(SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparsegettranspose(_:)-2fuzo.md)
  Returns a transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Float`.
- [func SparseGetTranspose(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparsegettranspose(_:)-4nr8u.md)
  Returns a transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Double`.
- [func SparseGetTranspose(SparseMatrix_Complex_Float) -> SparseMatrix_Complex_Float](sparsegettranspose(_:)-7dx1i.md)
  Returns a transposed copy of the specified matrix of complex float values.
- [func SparseGetTranspose(SparseMatrix_Complex_Float) -> SparseMatrix_Complex_Float](sparsegettranspose(_:)-7dx1i.md)
  Returns a transposed copy of the specified matrix of complex float values.
- [func SparseGetTranspose(SparseMatrix_Complex_Double) -> SparseMatrix_Complex_Double](sparsegettranspose(_:)-9olfr.md)
  Returns a transposed copy of the specified matrix of complex double values.
- [func SparseGetTranspose(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsegettranspose(_:)-d0ny.md)
  Returns a transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Double`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-1fq2g)*