# SparseGetTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a transposed copy of the specified single-precision subfactor.

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
func SparseGetTranspose(_ Subfactor: SparseOpaqueSubfactor_Float) -> SparseOpaqueSubfactor_Float
```

#### Return Value

An object equivalent to the transpose of the one you provide. Because this is a reference-counted subfactor, the system must free it through a call to [`SparseCleanup(_:)`](sparsecleanup(_:)-1mrmc.md) when it no longer needs it.

## Parameters

- `Subfactor`: The subfactor to transpose.

## See Also

- [func SparseGetTranspose(SparseOpaqueSubfactor_Double) -> SparseOpaqueSubfactor_Double](sparsegettranspose(_:)-9r7s5.md)
  Returns a transposed copy of the specified double-precision subfactor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-827va)*