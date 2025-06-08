# SparseGetTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a transposed, reference-counted copy of a `SparseOpaqueSubfactor_Complex_Float`.

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
func SparseGetTranspose(_ Subfactor: SparseOpaqueSubfactor_Complex_Float) -> SparseOpaqueSubfactor_Complex_Float
```

#### Return Value

A subfactor equivalent to the transpose of the one provided. As this is reference counted, it must be freed through a call to `SparseCleanup` once it is no longer required.

## Parameters

- `Subfactor`: The object to transpose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-2fuzo)*