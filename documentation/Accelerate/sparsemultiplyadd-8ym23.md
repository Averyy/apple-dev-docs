# SparseMultiplyAdd

**Framework**: Accelerate  
**Kind**: func

Performs `y += alpha * Ax` for complex float values

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
static void SparseMultiplyAdd(__SPARSE_float_complex alpha, SparseMatrix_Complex_Float A, DenseVector_Complex_Float x, DenseVector_Complex_Float y);
```

## Parameters

- `alpha`: (Input) scale to apply to the product of   and  .
- `A`: (Input) sparse matrix.
- `x`: (Input) dense vector.
- `y`: (Output) dense vector.

## See Also

- [func SparseMultiplyAdd(SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](sparsemultiplyadd(_:_:_:)-6qi0p.md)
  Performs `y += Ax` for complex double values
- [func SparseMultiplyAdd(SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsemultiplyadd(_:_:_:)-8dqy7.md)
  Performs `y += Ax` for complex float values
- [SparseMultiplyAdd](sparsemultiplyadd-47egy.md)
  Performs `y += alpha * Ax` for complex double values


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd-8ym23)*