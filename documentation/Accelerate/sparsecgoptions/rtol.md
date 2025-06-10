# rtol

**Framework**: Accelerate  
**Kind**: property

The relative convergence tolerance.

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
var rtol: Double
```

#### Discussion

 indicates convergence.

If [`rtol`](sparsecgoptions/rtol.md) is equal to `0`, the operation uses the default value of `sqrt(epsilon)`.

If it’s negative, the operation treats [`rtol`](sparsecgoptions/rtol.md) as `0.0` (it doesn’t use the default).

## See Also

- [var atol: Double](sparsecgoptions/atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](sparsecgoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsecgoptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparsecgoptions/reportstatus.md)
  The function to report status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/rtol)*