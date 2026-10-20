# SparseLSMR()

**Framework**: Accelerate  
**Kind**: func  
**Role**: Function

Returns a default least squares minimum residual (LSMR) method.

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
func SparseLSMR() -> SparseIterativeMethod
```

```c
static SparseIterativeMethod SparseLSMR();
```

#### Return Value

A [`SparseIterativeMethod`](./sparseiterativemethod.md) structure that represents a default LSMR method.

#### Discussion

LSMR is a minimal residual (MINRES) method for solving least squares. Use LSMR to solve equations of the form *Ax = b* where an exact solution doesn’t exist. The returned solution minimizes ‖ *b-Ax* ‖₂.

Although LSMR is equivalent to applying MINRES to the normal equations *AᵀAx = Aᵀb* in exact arithmetic, it has superior numerical behavior and is the preferred method. Due to the implicit squaring of the condition of *A* in the normal equations, LSMR may struggle to converge in single precision. Use double-precision arithmetic where possible.

For symmetric positive-definite systems, use [`SparseConjugateGradient(_:)`](./sparseconjugategradient%28_%29.md). For square, full-rank unsymmetric or indefinite equations, use [`SparseGMRES(_:)`](./sparsegmres%28_%29.md).

## See Also

### Sparse Iterative Methods for Overdetermined and Underdetermined Systems
- [func SparseLSMR(SparseLSMROptions) -> SparseIterativeMethod](./sparselsmr%28_%29.md)
  Returns a least squares minimum residual method with specified options.
- [struct SparseLSMROptions](./sparselsmroptions.md)
  Options for creating a least squares minimum residual method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmr())*