# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs the multiplication `Y = AX` for complex float values.

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
func SparseMultiply(_ A: SparseMatrix_Complex_Float, _ X: DenseMatrix_Complex_Float, _ Y: DenseMatrix_Complex_Float)
```

```c
static void SparseMultiply(SparseMatrix_Complex_Float A, DenseMatrix_Complex_Float X, DenseMatrix_Complex_Float Y);
```

## Parameters

- `A`: (Input) sparse matrix.
- `X`: (Input) dense matrix. Inner dimensions of `A` and `X` must match.
- `Y`: (Output) dense matrix. Dimensions must match the outer dimensions of `A` and `X`. Overwritten with their product.

## See Also

### Complex multiplication functions
- [func SparseMultiply(SparseMatrix_Complex_Double, DenseMatrix_Complex_Double, DenseMatrix_Complex_Double)](./sparsemultiply%28_,_,_%29-1sjuk.md)
  Performs the multiplication `Y = AX` for complex double values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-85a24)*