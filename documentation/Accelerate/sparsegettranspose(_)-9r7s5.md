# SparseGetTranspose(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a transposed copy of the specified double-precision subfactor.

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
func SparseGetTranspose(_ Subfactor: SparseOpaqueSubfactor_Double) -> SparseOpaqueSubfactor_Double
```

```c
static SparseOpaqueSubfactor_Double SparseGetTranspose(SparseOpaqueSubfactor_Double Subfactor);
```

## Return Value

An object equivalent to the transpose of the one you provide. Because this is a reference-counted subfactor, the system must free it through a call to [`SparseCleanup(_:)`](./sparsecleanup%28_%29-15kpj.md) when it no longer needs it.

## Parameters

- `Subfactor`: The subfactor to transpose.

## See Also

### Subfactor transpose functions
- [func SparseGetTranspose(SparseOpaqueSubfactor_Float) -> SparseOpaqueSubfactor_Float](./sparsegettranspose%28_%29-827va.md)
  Returns a transposed copy of the specified single-precision subfactor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-9r7s5)*