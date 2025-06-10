# SparseGetConjugateTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Float`.

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
func SparseGetConjugateTranspose(_ Subfactor: SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float
```

#### Return Value

A matrix factorization of `A^H`, where the original was of `A`. As this is reference counted, it must be freed through a call to `SparseCleanup` once it is no longer required.

## Parameters

- `Subfactor`: The object to conjugate transpose.

## See Also

- [func SparseGetConjugateTranspose(SparseMatrix_Complex_Float) -> SparseMatrix_Complex_Float](sparsegetconjugatetranspose(_:)-1e0js.md)
  Returns a conjugate transposed copy of the specified matrix of complex float values.
- [func SparseGetConjugateTranspose(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsegetconjugatetranspose(_:)-675y1.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Double`.
- [func SparseGetConjugateTranspose(SparseMatrix_Complex_Double) -> SparseMatrix_Complex_Double](sparsegetconjugatetranspose(_:)-9o30w.md)
  Returns a conjugate transposed copy of the specified specified matrix of complex double values.
- [func SparseGetConjugateTranspose(SparseMatrix_Complex_Double) -> SparseMatrix_Complex_Double](sparsegetconjugatetranspose(_:)-9o30w.md)
  Returns a conjugate transposed copy of the specified specified matrix of complex double values.
- [func SparseGetConjugateTranspose(SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsegetconjugatetranspose(_:)-a56p.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Float`.
- [func SparseGetConjugateTranspose(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparsegetconjugatetranspose(_:)-5hc5a.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Double`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegetconjugatetranspose(_:)-4hysc)*