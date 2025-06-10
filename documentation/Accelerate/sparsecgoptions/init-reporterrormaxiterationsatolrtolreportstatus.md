# init(reportError:maxIterations:atol:rtol:reportStatus:)

**Framework**: Accelerate  
**Kind**: init

Returns a new CG options structure using the specified parameters.

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
init(reportError: ((UnsafePointer<CChar>) -> Void)?, maxIterations: Int32, atol: Double, rtol: Double, reportStatus: ((UnsafePointer<CChar>) -> Void)?)
```

#### Return Value

A new CG options structure.

## Parameters

- `reportError`: An optional error-reporting routine.
- `maxIterations`: The maximum number of iterations.
- `atol`: The absolute convergence tolerance.
- `rtol`: The relative convergence tolerance.
- `reportStatus`: The function to report status.

## See Also

- [init()](sparsecgoptions/init.md)
  Returns a new CG options structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/init(reporterror:maxiterations:atol:rtol:reportstatus:))*