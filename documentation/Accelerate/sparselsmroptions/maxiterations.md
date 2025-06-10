# maxIterations

**Framework**: Accelerate  
**Kind**: property

The maximum number of iterations.

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
var maxIterations: Int32
```

#### Discussion

If [`maxIterations`](sparselsmroptions/maxiterations.md) is less than `0`, the operation uses a default value of `4n`. However, if a good preconditioner is available or the matrix is well-conditioned such that singular values cluster, a value of `n/2` may be more appropriate.

## See Also

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
- [var nvec: Int32](sparselsmroptions/nvec.md)
  The number of vectors to use for local reorthogonalization.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparselsmroptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparselsmroptions/reportstatus.md)
  An optional status-reporting routine.
- [var rtol: Double](sparselsmroptions/rtol.md)
  The relative convergence tolerance (default test only).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/maxiterations)*