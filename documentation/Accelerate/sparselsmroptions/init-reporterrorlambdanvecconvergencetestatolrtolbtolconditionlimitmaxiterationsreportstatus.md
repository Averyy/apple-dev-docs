# init(reportError:lambda:nvec:convergenceTest:atol:rtol:btol:conditionLimit:maxIterations:reportStatus:)

**Framework**: Accelerate  
**Kind**: init

Returns a new LSMR options structure using the specified parameters.

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
init(reportError: ((UnsafePointer<CChar>) -> Void)?, lambda: Double, nvec: Int32, convergenceTest: SparseLSMRConvergenceTest_t, atol: Double, rtol: Double, btol: Double, conditionLimit: Double, maxIterations: Int32, reportStatus: ((UnsafePointer<CChar>) -> Void)?)
```

## Parameters

- `reportError`: An optional status-reporting routine.
- `lambda`: The damping parameter lambda for regularized least squares.
- `nvec`: The number of vectors to use for local reorthogonalization.
- `convergenceTest`: The convergence test to use for iterative solve methods.
- `atol`: The absolute tolerance (default test) or   tolerance (Fong-Saunders test).
- `rtol`: The relative convergence tolerance (default test only).
- `btol`: The   tolerance (Fong-Saunders test only).
- `conditionLimit`: The condition number limit (Fong-Saunders test only).
- `maxIterations`: The maximum number of iterations.
- `reportStatus`: An optional error-reporting routine.

## See Also

- [init()](sparselsmroptions/init.md)
  Returns a new LSMR options structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparselsmroptions/init(reporterror:lambda:nvec:convergencetest:atol:rtol:btol:conditionlimit:maxiterations:reportstatus:))*