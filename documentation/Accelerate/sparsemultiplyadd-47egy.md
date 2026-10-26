# SparseMultiplyAdd

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs `y += alpha * Ax` for complex double values

**Availability**:
- iOS 18.5+
- iPadOS 18.5+
- Mac Catalyst 18.5+
- macOS 15.5+
- tvOS 18.5+
- visionOS 2.5+
- watchOS 11.5+

## Declaration

```c
static void SparseMultiplyAdd(__SPARSE_double_complex alpha, SparseMatrix_Complex_Double A, DenseVector_Complex_Double x, DenseVector_Complex_Double y);
```

## Parameters

- `alpha`: (Input) scale to apply to the product of `A` and `x`.
- `A`: (Input) sparse matrix.
- `x`: (Input) dense vector.
- `y`: (Output) dense vector.

## See Also

### Complex multiply-add functions
- [func SparseMultiplyAdd(SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](./sparsemultiplyadd%28_,_,_%29-6qi0p.md)
  Performs `y += Ax` for complex double values
- [func SparseMultiplyAdd(SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](./sparsemultiplyadd%28_,_,_%29-8dqy7.md)
  Performs `y += Ax` for complex float values
- [SparseMultiplyAdd](./sparsemultiplyadd-8ym23.md)
  Performs `y += alpha * Ax` for complex float values


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd-47egy)*