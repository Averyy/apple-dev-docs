# SparseMultiply

**Framework**: Accelerate  
**Kind**: func

Performs the multiplication `y = alpha * Ax` for complex float values.

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
static void SparseMultiply(__SPARSE_float_complex alpha, SparseMatrix_Complex_Float A, DenseVector_Complex_Float x, DenseVector_Complex_Float y);
```

## Parameters

- `alpha`: (Input) scale to apply to the result.
- `A`: (Input) sparse matrix.
- `x`: (Input) dense vector.
- `y`: (Output) dense vector.

## See Also

- [func SparseMultiply(SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsemultiply(_:_:_:)-6gzb3.md)
  Performs the multiplication `y = Ax` for complex float values
- [SparseMultiply](sparsemultiply-15ysy.md)
  Performs the multiplication `y = alpha * Ax` for complex double values.
- [func SparseMultiply(SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsemultiply(_:_:_:)-6xiv8.md)
  Performs the multiplication `y = Ax` for complex double values


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply-4xaml)*