# btol

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The *B* tolerance (Fong-Saunders test only).

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
var btol: Double
```

```c
double btol;
```

## Discussion

This value holds an estimate of the relative error in the data defining the right-hand-side, *b*. For example, if *b* is accurate to about six digits, set [`btol`](./btol.md) `= 1.0e-6`.

## See Also

### Inspecting LSMR Options
- [var atol: Double](./atol.md)
  The absolute tolerance (default test) or *A* tolerance (Fong-Saunders test).
- [var conditionLimit: Double](./conditionlimit.md)
  The condition number limit (Fong-Saunders test only).
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/btol)*