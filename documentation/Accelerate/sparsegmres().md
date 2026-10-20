# SparseGMRES()

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a generalized minimal residual (GMRES) method.

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
func SparseGMRES() -> SparseIterativeMethod
```

```c
static SparseIterativeMethod SparseGMRES();
```

#### Return Value

A [`SparseIterativeMethod`](./sparseiterativemethod.md) structure that represents a generalized minimal residual (GMRES) method.

#### Discussion

Use GMRES to solve *Ax = b* when *A* is symmetric indefinite or unsymmetric.

For symmetric positive-definite systems, use [`SparseConjugateGradient(_:)`](./sparseconjugategradient%28_%29.md). For rectangular or singular systems, use [`SparseLSMR(_:)`](./sparselsmr%28_%29.md).

## See Also

### Sparse Iterative Methods for Symmetric Indefinite and Unsymmetric Coefficient Matrices
- [func SparseGMRES(SparseGMRESOptions) -> SparseIterativeMethod](./sparsegmres%28_%29.md)
  Returns a generalized minimal residual (GMRES) method with specified options.
- [struct SparseGMRESOptions](./sparsegmresoptions.md)
  Options for creating a generalized minimal residual (GMRES) method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmres())*