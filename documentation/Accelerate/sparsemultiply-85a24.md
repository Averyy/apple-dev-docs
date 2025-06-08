# SparseMultiply(_:_:_:)

**Framework**: Accelerate  
**Kind**: func

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

## Parameters

- `A`: (Input) sparse matrix.
- `X`: (Input) dense matrix. Inner dimensions of   and   must match.
- `Y`: (Output) dense matrix. Dimensions must match the outer dimensions   of   and  . Overwritten with their product.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsemultiply(_:_:_:)-85a24)*