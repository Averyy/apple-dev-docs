# SparseGetConjugateTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueFactorization_Complex_Double`.

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
func SparseGetConjugateTranspose(_ Factor: SparseOpaqueFactorization_Complex_Double) -> SparseOpaqueFactorization_Complex_Double
```

#### Return Value

A matrix factorization of `A^H`, where the original was of `A`. As this is reference counted, it must be freed through a call to `SparseCleanup` once it is no longer required.

## Parameters

- `Factor`: The factorization to conjugate transpose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegetconjugatetranspose(_:)-675y1)*