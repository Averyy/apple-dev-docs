# SparseGetConjugateTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a conjugate transposed copy of the specified specified matrix of complex double values.

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
func SparseGetConjugateTranspose(_ Matrix: SparseMatrix_Complex_Double) -> SparseMatrix_Complex_Double
```

#### Return Value

A copy of matrix with `matrix.structure.attributes.transpose` bit flipped and `matrix.structure.attributes.conjugate_transpose` bit set.

#### Discussion

Note that the underlying storage is  reference counted, so users must ensure the original matrix (or at least its underlying storage) is not destroyed before they are finished with the matrix returned by this routine.

## Parameters

- `Matrix`: The matrix to conjugate transpose.

## See Also

- [func SparseGetConjugateTranspose(SparseMatrix_Complex_Float) -> SparseMatrix_Complex_Float](sparsegetconjugatetranspose(_:)-1e0js.md)
  Returns a conjugate transposed copy of the specified matrix of complex float values.
- [func SparseGetConjugateTranspose(SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float](sparsegetconjugatetranspose(_:)-4hysc.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Float`.
- [func SparseGetConjugateTranspose(SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double](sparsegetconjugatetranspose(_:)-675y1.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Double`.
- [func SparseGetConjugateTranspose(SparseOpaqueFactorization_Complex_Float) -> SparseOpaqueFactorization_Complex_Float](sparsegetconjugatetranspose(_:)-a56p.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Float`.
- [func SparseGetConjugateTranspose(SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double](sparsegetconjugatetranspose(_:)-5hc5a.md)
  Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Double`.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegetconjugatetranspose(_:)-9o30w)*