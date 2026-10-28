# atol

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The absolute tolerance (default test) or *A* tolerance (Fong-Saunders test).

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
var atol: Double
```

```c
double atol;
```

## Discussion

In the Fong and Saunders case, this value holds an estimate of the relative error in the data defining the matrix *A*. For example, if *A* is accurate to about six digits, set [`atol`](./atol.md) `= 1.0e-6`.

## See Also

### Inspecting LSMR Options
- [var btol: Double](./btol.md)
  The *B* tolerance (Fong-Saunders test only).
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/atol)*