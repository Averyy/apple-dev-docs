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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-1fq2g)*