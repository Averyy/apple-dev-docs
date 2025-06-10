# SparseLSMR(_:)

**Framework**: Accelerate  
**Kind**: func

Returns a least squares minimum residual method with specified options.

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
func SparseLSMR(_ options: SparseLSMROptions) -> SparseIterativeMethod
```

#### Return Value

A [`SparseIterativeMethod`](sparseiterativemethod.md) structure that represents a default LSMR method.

#### Discussion

LSMR is a minimal residual (MINRES) method for solving least squares. Use LSMR to solve equations of the form  where an exact solution doesn’t exist. The returned solution minimizes ‖  ‖₂.

Although LSMR is equivalent to applying MINRES to the normal equations  in exact arithmetic, it has superior numerical behavior and is the preferred method. Due to the implicit squaring of the condition of  in the normal equations, LSMR may struggle to converge in single precision. Use double-precision arithmetic where possible.

For symmetric positive-definite systems, use [`SparseConjugateGradient(_:)`](sparseconjugategradient(_:).md). For square, full-rank unsymmetric or indefinite equations, use [`SparseGMRES(_:)`](sparsegmres(_:).md).

## Parameters

- `options`: The LSMR options to use when creating the LSMR method.

## See Also

- [func SparseLSMR() -> SparseIterativeMethod](sparselsmr().md)
  Returns a default least squares minimum residual (LSMR) method.
- [struct SparseLSMROptions](sparselsmroptions.md)
  Options for creating a least squares minimum residual method.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmr(_:))*