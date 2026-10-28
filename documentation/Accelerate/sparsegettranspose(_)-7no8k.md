# SparseGetTranspose(_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a transposed copy of the specified matrix of single-precision, floating-point values.

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
func SparseGetTranspose(_ Matrix: SparseMatrix_Float) -> SparseMatrix_Float
```

```c
static SparseMatrix_Float SparseGetTranspose(SparseMatrix_Float Matrix);
```

## Return Value

A [`SparseMatrix_Float`](./sparsematrix_float.md) structure that represents the transposed matrix.

## Discussion

Use this function to return a new [`SparseMatrix_Double`](./sparsematrix_double.md) structure that shares underlying storage with the specified matrix, but with its [`transpose`](./sparseattributes_t/transpose.md) attribute as `true`. The system doesn’t reference-count the underlying storage, so you must ensure it doesn’t destroy the original matrix before you finish with the matrix that this routine returns.

## Parameters

- `Matrix`: The matrix to transpose.

## See Also

### Matrix transpose functions
- [func SparseGetTranspose(SparseMatrix_Double) -> SparseMatrix_Double](./sparsegettranspose%28_%29-227ei.md)
  Returns a transposed copy of the specified matrix of double-precision, floating-point values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegettranspose(_:)-7no8k)*