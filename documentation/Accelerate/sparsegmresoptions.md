# SparseGMRESOptions

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Options for creating a generalized minimal residual (GMRES) method.

**Availability**:
- iOS
- iPadOS
- Mac Catalyst
- macOS
- tvOS
- visionOS
- watchOS

## Declaration

```swift
struct SparseGMRESOptions
```

```c
typedef struct { ... } SparseGMRESOptions;
```

#### Overview

Use GMRES to solve *Ax = b* when *A* is symmetric indefinite or unsymmetric.

For symmetric positive-definite systems, use [`SparseConjugateGradient(_:)`](./sparseconjugategradient%28_%29.md). For rectangular or singular systems, use [`SparseLSMR(_:)`](./sparselsmr%28_%29.md).

## Topics

### Initializers
- [init()](./sparsegmresoptions/init%28%29.md)
- [init(reportError: ((UnsafePointer<CChar>) -> Void)?, variant: SparseGMRESVariant_t, nvec: Int32, maxIterations: Int32, atol: Double, rtol: Double, reportStatus: ((UnsafePointer<CChar>) -> Void)?)](./sparsegmresoptions/init%28reporterror,variant,nvec,maxiterations,atol,rtol,reportstatus%29.md)
  Returns a new GMRES options structure using the specified parameters.
### Inspecting GMRES Options
- [var atol: Double](./sparsegmresoptions/atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](./sparsegmresoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var nvec: Int32](./sparsegmresoptions/nvec.md)
  The number of orthogonal vectors the operation maintains.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./sparsegmresoptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](./sparsegmresoptions/reportstatus.md)
  The function to report status.
- [var rtol: Double](./sparsegmresoptions/rtol.md)
  The relative convergence tolerance.
- [var variant: SparseGMRESVariant_t](./sparsegmresoptions/variant.md)
  The exact variant of GMRES to implement.
- [struct SparseGMRESVariant_t](./sparsegmresvariant_t.md)
  Defines the exact variant of GMRES to implement

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Sparse Iterative Methods for Symmetric Indefinite and Unsymmetric Coefficient Matrices
- [func SparseGMRES() -> SparseIterativeMethod](./sparsegmres%28%29.md)
  Returns a generalized minimal residual (GMRES) method.
- [func SparseGMRES(SparseGMRESOptions) -> SparseIterativeMethod](./sparsegmres%28_%29.md)
  Returns a generalized minimal residual (GMRES) method with specified options.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions)*