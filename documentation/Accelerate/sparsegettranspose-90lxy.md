# SparseGetTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a transposed copy of the specified double-precision factorization.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseGetTranspose(_ Factor: SparseOpaqueFactorization_Double) -> SparseOpaqueFactorization_Double
```

#### Return Value

A matrix factorization of , where the original was of . Because this is a reference-counted factorization, you must free it through a call to [`SparseCleanup(_:)`](sparsecleanup(_:)-3cnxt.md) when you no longer need it.

## Parameters

- `Factor`: The factorization to transpose.

## See Also

- [func SparseGetTranspose(SparseOpaqueFactorization_Float) -> SparseOpaqueFactorization_Float](sparsegettranspose(_:)-48t76.md)
  Returns a transposed copy of the specified single-precision factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-90lxy)*