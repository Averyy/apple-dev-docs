# SparseGetTranspose(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a transposed copy of the specified single-precision factorization.

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
func SparseGetTranspose(_ Factor: SparseOpaqueFactorization_Float) -> SparseOpaqueFactorization_Float
```

```c
static SparseOpaqueFactorization_Float SparseGetTranspose(SparseOpaqueFactorization_Float Factor);
```

## Return Value

A matrix factorization of *A__ᵀ*, where the original was of *A*. Because this is a reference-counted factorization, you must free it through a call to [`SparseCleanup(_:)`](./sparsecleanup%28_%29-4kus5.md) when you no longer need it.

## Parameters

- `Factor`: The factorization to transpose.

## See Also

### Factorization transpose functions
- [func SparseGetTranspose(SparseOpaqueFactorization_Double) -> SparseOpaqueFactorization_Double](./sparsegettranspose%28_%29-90lxy.md)
  Returns a transposed copy of the specified double-precision factorization.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-48t76)*