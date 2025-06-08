# SparseMultiplyAdd(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

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

#### Discussion

- Parameter `A`: (input) sparse matrix.
- Parameter `X`: (input) dense matrix. Inner dimensions of `A` and `X` must match.
- Parameter `Y`: (output) dense matrix. Dimensions must match the outer dimensions of `A` and `X`. Overwritten with their product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiplyadd(_:_:_:)-658zk)*