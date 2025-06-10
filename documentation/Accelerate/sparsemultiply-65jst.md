# SparseMultiply

**Framework**: Accelerate  
**Kind**: func

Performs the multiplication `Y = alpha * AX` for complex double values

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
static void SparseMultiply(__SPARSE_double_complex alpha, SparseMatrix_Complex_Double A, DenseMatrix_Complex_Double X, DenseMatrix_Complex_Double Y);
```

## Parameters

- `alpha`: (Input) scale to apply to the result.
- `A`: (Input) sparse matrix.
- `X`: (Input) dense matrix. Inner dimensions of   and   must match.
- `Y`: (Output) dense matrix. Dimensions must match the outer dimensions   of   and  . Overwritten with  .

## See Also

- [func SparseMultiply(SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsemultiply(_:_:_:)-1sjuk.md)
  Performs the multiplication `Y = AX` for complex double values.
- [func SparseMultiply(SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiply(_:_:_:)-85a24.md)
  Performs the multiplication `Y = AX` for complex float values.
- [SparseMultiply](sparsemultiply-5bf3v.md)
  Performs the multiplication `Y = alpha * AX` for complex float values


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply-65jst)*