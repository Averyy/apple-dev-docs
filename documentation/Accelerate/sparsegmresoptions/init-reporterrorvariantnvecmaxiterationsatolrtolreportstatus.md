# init(reportError:variant:nvec:maxIterations:atol:rtol:reportStatus:)

**Framework**: Accelerate  
**Kind**: init

Returns a new GMRES options structure using the specified parameters.

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
init(reportError: ((UnsafePointer<CChar>) -> Void)?, variant: SparseGMRESVariant_t, nvec: Int32, maxIterations: Int32, atol: Double, rtol: Double, reportStatus: ((UnsafePointer<CChar>) -> Void)?)
```

## Parameters

- `reportError`: An optional error-reporting routine.
- `variant`: The exact variant of GMRES to implement.
- `nvec`: The number of orthogonal vectors the operation maintains.
- `maxIterations`: The maximum number of iterations to perform.
- `atol`: The absolute convergence tolerance.
- `rtol`: The relative convergence tolerance.
- `reportStatus`: The function to report status.

## See Also

- [init()](sparsegmresoptions/init.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/init(reporterror:variant:nvec:maxiterations:atol:rtol:reportstatus:))*