# rtol

**Framework**: Accelerate  
**Kind**: property

The relative convergence tolerance (default test only).

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
var rtol: Double
```

#### Discussion

If this value is `0.0`, the operation uses the default value of `sqrt(epsilon)`. If it’s negative, the operation treats [`rtol`](sparselsmroptions/rtol.md) as `0.0` (it doesn’t use the default)

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
- [var maxIterations: Int32](sparselsmroptions/maxiterations.md)
  The maximum number of iterations.
- [var nvec: Int32](sparselsmroptions/nvec.md)
  The number of vectors to use for local reorthogonalization.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparselsmroptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparselsmroptions/reportstatus.md)
  An optional status-reporting routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/rtol)*