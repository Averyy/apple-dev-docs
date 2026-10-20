# convergenceTest

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The convergence test to use for iterative solve methods.

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
var convergenceTest: SparseLSMRConvergenceTest_t
```

```c
SparseLSMRConvergenceTest_t convergenceTest;
```

#### Discussion

For [`SparseLSMRCTDefault`](../sparselsmrctdefault.md), iterations stop when:

- *‖ Aᵀ(b-Ax) ‖₂ < [`rtol`](./rtol.md) * ‖ Aᵀ(b-Ax_₀) ‖₂ + [`atol`](./atol.md)*

For [`SparseLSMRCTFongSaunders`](../sparselsmrctfongsaunders.md), iterations stop when any of the following occur:

- *‖ b-Ax ‖₂ < [`btol`](./btol.md) * ‖ b ‖₂ + [`atol`](./atol.md) * ‖ A ‖₂ ‖ x ‖₂*    (*‖A‖₂* is an estimate)
- *‖ Aᵀ (b-Ax) ‖₂ < [`atol`](./atol.md) * ‖ A ‖₂ * ‖ A-bx ‖₂*             (*‖A‖₂* is an estimate)
- Estimated condition of *matrix >= [`conditionLimit`](./conditionlimit.md)*

## See Also

### Inspecting LSMR Options
- [var atol: Double](./atol.md)
  The absolute tolerance (default test) or *A* tolerance (Fong-Saunders test).
- [var btol: Double](./btol.md)
  The *B* tolerance (Fong-Saunders test only).
- [var conditionLimit: Double](./conditionlimit.md)
  The condition number limit (Fong-Saunders test only).
- [struct SparseLSMRConvergenceTest_t](../sparselsmrconvergencetest_t.md)
  Constants that specify the type of convergence test.
- [var lambda: Double](./lambda.md)
  The damping parameter lambda for regularized least squares.
- [var maxIterations: Int32](./maxiterations.md)
  The maximum number of iterations.
- [var nvec: Int32](./nvec.md)
  The number of vectors to use for local reorthogonalization.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](./reportstatus.md)
  An optional status-reporting routine.
- [var rtol: Double](./rtol.md)
  The relative convergence tolerance (default test only).


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/convergencetest)*