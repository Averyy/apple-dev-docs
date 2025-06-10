# reportError

**Framework**: Accelerate  
**Kind**: property

An optional error-reporting routine.

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
var reportError: ((UnsafePointer<CChar>) -> Void)?
```

## See Also

- [var atol: Double](sparsecgoptions/atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](sparsecgoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparsecgoptions/reportstatus.md)
  The function to report status.
- [var rtol: Double](sparsecgoptions/rtol.md)
  The relative convergence tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/reporterror)*