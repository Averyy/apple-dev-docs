# convergenceTest

**Framework**: Accelerate  
**Kind**: property

The convergence test to use for iterative solve methods.

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
var convergenceTest: SparseLSMRConvergenceTest_t
```

#### Discussion

For [`SparseLSMRCTDefault`](sparselsmrctdefault.md), iterations stop when:

- *‖ Aᵀ(b-Ax) ‖₂ < [`rtol`](sparselsmroptions/rtol.md) * ‖ Aᵀ(b-Ax_₀) ‖₂ + [`atol`](sparselsmroptions/atol.md)*

For [`SparseLSMRCTFongSaunders`](sparselsmrctfongsaunders.md), iterations stop when any of the following occur:

- *‖ b-Ax ‖₂ < [`btol`](sparselsmroptions/btol.md) * ‖ b ‖₂ + [`atol`](sparselsmroptions/atol.md) * ‖ A ‖₂ ‖ x ‖₂*    (*‖A‖₂* is an estimate)
- *‖ Aᵀ (b-Ax) ‖₂ < [`atol`](sparselsmroptions/atol.md) * ‖ A ‖₂ * ‖ A-bx ‖₂*             (*‖A‖₂* is an estimate)
- Estimated condition of *matrix >= [`conditionLimit`](sparselsmroptions/conditionlimit.md)*

## See Also

- [var atol: Double](sparselsmroptions/atol.md)
  The absolute tolerance (default test) or *A* tolerance (Fong-Saunders test).
- [var btol: Double](sparselsmroptions/btol.md)
  The *B* tolerance (Fong-Saunders test only).
- [var conditionLimit: Double](sparselsmroptions/conditionlimit.md)
  The condition number limit (Fong-Saunders test only).
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/convergencetest)*