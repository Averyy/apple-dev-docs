# SparseGetTranspose(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a transposed copy of the specified matrix of complex float values.

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
func SparseGetTranspose(_ Matrix: SparseMatrix_Complex_Float) -> SparseMatrix_Complex_Float
```

#### Return Value

A copy of matrix with `matrix.structure.attributes.transpose` bit flipped and `matrix.structure.attributes.conjugate_transpose` bit cleared.

#### Discussion

Note that the underlying storage is  reference counted, so users must ensure the original matrix (or at least its underlying storage) is not destroyed before they are finished with the matrix returned by this routine.

## Parameters

- `Matrix`: The matrix to transpose.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-7dx1i)*