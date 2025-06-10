# SparseMultiplyAdd

**Framework**: Accelerate  
**Kind**: func

Performs `Y += alpha * AX` for complex float values

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
static void SparseMultiplyAdd(__SPARSE_float_complex alpha, SparseMatrix_Complex_Float A, DenseMatrix_Complex_Float X, DenseMatrix_Complex_Float Y);
```

## Parameters

- `alpha`: (Input) scale to apply to the product of   and  .
- `A`: (Input) sparse matrix.
- `X`: (Input) dense matrix. Inner dimensions of   and   must match.
- `Y`: (Output) dense matrix. Dimensions must match the outer dimensions   of   and  . Overwritten with  .

## See Also

- [func SparseMultiplyAdd(SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](sparsemultiplyadd(_:_:_:)-658zk.md)
  Performs `Y += AX` for complex double values
- [func SparseMultiplyAdd(SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](sparsemultiplyadd(_:_:_:)-4dpyu.md)
  Performs `Y += AX` for complex float values
- [SparseMultiplyAdd](sparsemultiplyadd-7pu5c.md)
  Performs `Y += alpha * AX` for complex double values


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd-4gs2p)*