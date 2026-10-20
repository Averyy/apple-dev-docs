# reportStatus

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The function to report status.

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
var reportStatus: ((UnsafePointer<CChar>) -> Void)?
```

```c
void (*)(const char *) reportStatus;
```

## See Also

### Inspecting CG Options
- [var atol: Double](./atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](./maxiterations.md)
  The maximum number of iterations to perform.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  An optional error-reporting routine.
- [var rtol: Double](./rtol.md)
  The relative convergence tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/reportstatus)*