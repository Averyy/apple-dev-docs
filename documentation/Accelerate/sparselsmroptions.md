# SparseLSMROptions

**Framework**: Accelerate  
**Kind**: struct

Options for creating a least squares minimum residual method.

**Availability**:
- iOS ?+
- iPadOS ?+
- Mac Catalyst ?+
- macOS ?+
- tvOS ?+
- visionOS ?+
- watchOS ?+

## Declaration

```swift
struct SparseLSMROptions
```

#### Overview

LSMR is a minimal residual (MINRES) method for solving least squares. Use LSMR to solve equations of the form  where an exact solution doesn’t exist. The returned solution minimizes ‖  ‖₂.

Although LSMR is equivalent to applying MINRES to the normal equations  in exact arithmetic, it has superior numerical behavior and is the preferred method. Due to the implicit squaring of the condition of  in the normal equations, LSMR may struggle to converge in single precision. Use double-precision arithmetic where possible.

For symmetric positive-definite systems, use [`SparseConjugateGradient(_:)`](sparseconjugategradient(_:).md). For square, full-rank unsymmetric or indefinite equations, use [`SparseGMRES(_:)`](sparsegmres(_:).md).

## Topics

### Initializers
- [init()](sparselsmroptions/init.md)
  Returns a new LSMR options structure.
- [init(reportError: ((UnsafePointer<CChar>) -> Void)?, lambda: Double, nvec: Int32, convergenceTest: SparseLSMRConvergenceTest_t, atol: Double, rtol: Double, btol: Double, conditionLimit: Double, maxIterations: Int32, reportStatus: ((UnsafePointer<CChar>) -> Void)?)](sparselsmroptions/init(reporterror:lambda:nvec:convergencetest:atol:rtol:btol:conditionlimit:maxiterations:reportstatus:).md)
  Returns a new LSMR options structure using the specified parameters.
### Inspecting LSMR Options
- [var atol: Double](sparselsmroptions/atol.md)
  The absolute tolerance (default test) or  tolerance (Fong-Saunders test).
- [var btol: Double](sparselsmroptions/btol.md)
  The  tolerance (Fong-Saunders test only).
- [var conditionLimit: Double](sparselsmroptions/conditionlimit.md)
  The condition number limit (Fong-Saunders test only).
- [var convergenceTest: SparseLSMRConvergenceTest_t](sparselsmroptions/convergencetest.md)
  The convergence test to use for iterative solve methods.
- [struct SparseLSMRConvergenceTest_t](sparselsmrconvergencetest_t.md)
  Constants that specify the type of convergence test.
- [var lambda: Double](sparselsmroptions/lambda.md)
  The damping parameter lambda for regularized least squares.
- [var maxIterations: Int32](sparselsmroptions/maxiterations.md)
  The maximum number of iterations.
- [var nvec: Int32](sparselsmroptions/nvec.md)
  The number of vectors to use for local reorthogonalization.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparselsmroptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparselsmroptions/reportstatus.md)
  An optional status-reporting routine.
- [var rtol: Double](sparselsmroptions/rtol.md)
  The relative convergence tolerance (default test only).

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func SparseLSMR() -> SparseIterativeMethod](sparselsmr().md)
  Returns a default least squares minimum residual (LSMR) method.
- [func SparseLSMR(SparseLSMROptions) -> SparseIterativeMethod](sparselsmr(_:).md)
  Returns a least squares minimum residual method with specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions)*