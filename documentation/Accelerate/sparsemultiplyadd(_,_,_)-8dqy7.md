# SparseMultiplyAdd(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs `y += Ax` for complex float values

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
func SparseMultiplyAdd(_ A: SparseMatrix_Complex_Float, _ x: DenseVector_Complex_Float, _ y: DenseVector_Complex_Float)
```

```c
static void SparseMultiplyAdd(SparseMatrix_Complex_Float A, DenseVector_Complex_Float x, DenseVector_Complex_Float y);
```

#### Discussion

- Parameter `A`: (input) sparse matrix.
- Parameter `x`: (input) dense vector.
- Parameter `y`: (output) dense vector.

## See Also

### Complex multiply-add functions
- [func SparseMultiplyAdd(SparseMatrix_Complex_Double, DenseVector_Complex_Double, DenseVector_Complex_Double)](./sparsemultiplyadd%28_,_,_%29-6qi0p.md)
  Performs `y += Ax` for complex double values
- [SparseMultiplyAdd](./sparsemultiplyadd-47egy.md)
  Performs `y += alpha * Ax` for complex double values
- [SparseMultiplyAdd](./sparsemultiplyadd-8ym23.md)
  Performs `y += alpha * Ax` for complex float values


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:)-8dqy7)*