# conditionLimit

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The condition number limit (Fong-Saunders test only).

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
var conditionLimit: Double
```

```c
double conditionLimit;
```

#### Discussion

The operation terminates iterations if a computed estimate of `cond(Abar)` exceeds this value. This is to prevent certain small or zero singular values of *A* or *Abar* from coming into effect and causing unwanted growth in the computed solution.

You can use [`conditionLimit`](./conditionlimit.md) and [`lambda`](./lambda.md) separately or together to regularize ill-conditioned systems.

Normally, [`conditionLimit`](./conditionlimit.md) is in the range `1000` to `1/eps`.

Suggested value: [`conditionLimit`](./conditionlimit.md) `= 1/(100*eps)`  for compatible systems, [`conditionLimit`](./conditionlimit.md) `= 1/(10*sqrt(eps))` for least squares

## See Also

### Inspecting LSMR Options
- [var atol: Double](./atol.md)
  The absolute tolerance (default test) or *A* tolerance (Fong-Saunders test).
- [var btol: Double](./btol.md)
  The *B* tolerance (Fong-Saunders test only).
- [var convergenceTest: SparseLSMRConvergenceTest_t](./convergencetest.md)
  The convergence test to use for iterative solve methods.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/conditionlimit)*