# SparseConjugateGradient()

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a conjugate gradient (CG) method.

**Availability**:
- iOS 11.0+
- iPadOS 11.0+
- Mac Catalyst 13.1+
- macOS 10.13+
- tvOS 11.0+
- visionOS 1.0+
- watchOS 4.0+

## Declaration

```swift
func SparseConjugateGradient() -> SparseIterativeMethod
```

```c
static SparseIterativeMethod SparseConjugateGradient();
```

## Return Value

A [`SparseIterativeMethod`](./sparseiterativemethod.md) structure that represents a default conjugate gradient method.

## Discussion

Use CG to solve *Ax = b* when *A* is symmetric positive-definite. The method may break down or fail to converge if *A* isn’t positive-definite.

For square, full-rank, unsymmetric or indefinite equations, use [`SparseGMRES(_:)`](./sparsegmres%28_%29.md). For rectangular or singular systems, use [`SparseLSMR(_:)`](./sparselsmr%28_%29.md).

## See Also

### Sparse Iterative Methods for Symmetric Positive-Definite Coefficient Matrices
- [func SparseConjugateGradient(SparseCGOptions) -> SparseIterativeMethod](./sparseconjugategradient%28_%29.md)
  Returns a conjugate gradient (CG) method with specified options.
- [struct SparseCGOptions](./sparsecgoptions.md)
  Options for creating a conjugate gradient (CG) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparseconjugategradient())*