# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Performs the multiplication `y = Ax` for complex double values

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
func SparseMultiply(_ A: SparseMatrix_Complex_Double, _ x: DenseVector_Complex_Double, _ y: DenseVector_Complex_Double)
```

```c
static void SparseMultiply(SparseMatrix_Complex_Double A, DenseVector_Complex_Double x, DenseVector_Complex_Double y);
```

## Parameters

- `A`: (Input) sparse matrix.
- `x`: (Input) dense vector.
- `y`: (Output) dense vector.

## See Also

### Complex multiplication functions
- [func SparseMultiply(SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](./sparsemultiply%28_,_,_%29-6gzb3.md)
  Performs the multiplication `y = Ax` for complex float values
- [SparseMultiply](./sparsemultiply-15ysy.md)
  Performs the multiplication `y = alpha * Ax` for complex double values.
- [SparseMultiply](./sparsemultiply-4xaml.md)
  Performs the multiplication `y = alpha * Ax` for complex float values.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-6xiv8)*