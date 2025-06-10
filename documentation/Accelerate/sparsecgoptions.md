# SparseCGOptions

**Framework**: Accelerate  
**Kind**: struct

Options for creating a conjugate gradient (CG) method.

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
struct SparseCGOptions
```

#### Overview

Use CG to solve  when  is symmetric positive-definite. The method may break down or fail to converge if  isn’t positive-definite.

For square, full-rank, unsymmetric or indefinite equations, use [`SparseGMRES(_:)`](sparsegmres(_:).md). For rectangular or singular systems, use [`SparseLSMR(_:)`](sparselsmr(_:).md).

## Topics

### Initializers
- [init()](sparsecgoptions/init.md)
  Returns a new CG options structure.
- [init(reportError: ((UnsafePointer<CChar>) -> Void)?, maxIterations: Int32, atol: Double, rtol: Double, reportStatus: ((UnsafePointer<CChar>) -> Void)?)](sparsecgoptions/init(reporterror:maxiterations:atol:rtol:reportstatus:).md)
  Returns a new CG options structure using the specified parameters.
### Inspecting CG Options
- [var atol: Double](sparsecgoptions/atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](sparsecgoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsecgoptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparsecgoptions/reportstatus.md)
  The function to report status.
- [var rtol: Double](sparsecgoptions/rtol.md)
  The relative convergence tolerance.

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [func SparseConjugateGradient() -> SparseIterativeMethod](sparseconjugategradient().md)
  Returns a conjugate gradient (CG) method.
- [func SparseConjugateGradient(SparseCGOptions) -> SparseIterativeMethod](sparseconjugategradient(_:).md)
  Returns a conjugate gradient (CG) method with specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions)*