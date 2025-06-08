# SparseConvertFromOpaque(_:)

**Framework**: Accelerate  
**Kind**: func

Converts an opaque matrix of complex double values object to a transparent sparse matrix object. When you are done with this matrix, release the memory that has been allocated by calling `SparseCleanup` on it.

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
func SparseConvertFromOpaque(_ matrix: sparse_matrix_double_complex) -> SparseMatrix_Complex_Double
```

## Parameters

- `matrix`: The matrix to be converted.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseconvertfromopaque(_:)-9xju4)*