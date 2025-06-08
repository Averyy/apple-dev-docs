# SparseMultiplyAdd(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

Performs `y += Ax` for complex double values

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
func SparseMultiplyAdd(_ A: SparseMatrix_Complex_Double, _ x: DenseVector_Complex_Double, _ y: DenseVector_Complex_Double)
```

#### Discussion

- Parameter `A`: (input) sparse matrix.
- Parameter `x`: (input) dense vector.
- Parameter `y`: (output) dense vector.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:)-6qi0p)*