# reportStatus

**Framework**: Accelerate  
**Kind**: property

The function to report status.

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
var reportStatus: ((UnsafePointer<CChar>) -> Void)?
```

## See Also

- [var atol: Double](sparsecgoptions/atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](sparsecgoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsecgoptions/reporterror.md)
  An optional error-reporting routine.
- [var rtol: Double](sparsecgoptions/rtol.md)
  The relative convergence tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/reportstatus)*