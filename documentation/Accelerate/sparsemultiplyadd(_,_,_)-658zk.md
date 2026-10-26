# SparseMultiplyAdd(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs `Y += AX` for complex double values

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
func SparseMultiplyAdd(_ A: SparseMatrix_Complex_Double, _ X: DenseMatrix_Complex_Double, _ Y: DenseMatrix_Complex_Double)
```

```c
static void SparseMultiplyAdd(SparseMatrix_Complex_Double A, DenseMatrix_Complex_Double X, DenseMatrix_Complex_Double Y);
```

#### Discussion

- Parameter `A`: (input) sparse matrix.
- Parameter `X`: (input) dense matrix. Inner dimensions of `A` and `X` must match.
- Parameter `Y`: (output) dense matrix. Dimensions must match the outer dimensions of `A` and `X`. Overwritten with their product.

## See Also

### Complex multiply-add functions
- [func SparseMultiplyAdd(SparseMatrix_Complex_Float, DenseMatrix_Complex_Float, DenseMatrix_Complex_Float)](./sparsemultiplyadd%28_,_,_%29-4dpyu.md)
  Performs `Y += AX` for complex float values
- [SparseMultiplyAdd](./sparsemultiplyadd-4gs2p.md)
  Performs `Y += alpha * AX` for complex float values
- [SparseMultiplyAdd](./sparsemultiplyadd-7pu5c.md)
  Performs `Y += alpha * AX` for complex double values


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:)-658zk)*