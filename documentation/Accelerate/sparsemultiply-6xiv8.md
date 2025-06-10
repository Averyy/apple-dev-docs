# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

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

## Parameters

- `A`: (Input) sparse matrix.
- `x`: (Input) dense vector.
- `y`: (Output) dense vector.

## See Also

- [func SparseMultiply(SparseMatrix_Complex_Float, DenseVector_Complex_Float, DenseVector_Complex_Float)](sparsemultiply(_:_:_:)-6gzb3.md)
  Performs the multiplication `y = Ax` for complex float values


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-6xiv8)*