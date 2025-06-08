# SparseGetConjugateTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a conjugate transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Double`.

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
func SparseGetConjugateTranspose(_ Subfactor: SparseOpaqueSubfactor_Complex_Double) -> SparseOpaqueSubfactor_Complex_Double
```

#### Return Value

A matrix factorization of `A^H`, where the original was of `A`. As this is reference counted, it must be freed through a call to `SparseCleanup` once it is no longer required.

## Parameters

- `Subfactor`: The object to conjugate transpose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegetconjugatetranspose(_:)-5hc5a)*