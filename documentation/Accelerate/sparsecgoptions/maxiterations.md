# maxIterations

**Framework**: Accelerate  
**Kind**: property

The maximum number of iterations to perform.

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
var maxIterations: Int32
```

#### Discussion

If `0`, the operation uses the default value of `100`.

## See Also

- [var atol: Double](sparsecgoptions/atol.md)
  The absolute convergence tolerance.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsecgoptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparsecgoptions/reportstatus.md)
  The function to report status.
- [var rtol: Double](sparsecgoptions/rtol.md)
  The relative convergence tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/maxiterations)*