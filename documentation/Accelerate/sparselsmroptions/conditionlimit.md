# conditionLimit

**Framework**: Accelerate  
**Kind**: property

The condition number limit (Fong-Saunders test only).

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
var conditionLimit: Double
```

#### Discussion

The operation terminates iterations if a computed estimate of `cond(Abar)` exceeds this value. This is to prevent certain small or zero singular values of  or  from coming into effect and causing unwanted growth in the computed solution.

You can use [`conditionLimit`](sparselsmroptions/conditionlimit.md) and [`lambda`](sparselsmroptions/lambda.md) separately or together to regularize ill-conditioned systems.

Normally, [`conditionLimit`](sparselsmroptions/conditionlimit.md) is in the range `1000` to `1/eps`.

Suggested value: [`conditionLimit`](sparselsmroptions/conditionlimit.md) `= 1/(100*eps)`  for compatible systems, [`conditionLimit`](sparselsmroptions/conditionlimit.md) `= 1/(10*sqrt(eps))` for least squares

## See Also

- [var atol: Double](sparselsmroptions/atol.md)
  The absolute tolerance (default test) or  tolerance (Fong-Saunders test).
- [var btol: Double](sparselsmroptions/btol.md)
  The  tolerance (Fong-Saunders test only).
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


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/conditionlimit)*