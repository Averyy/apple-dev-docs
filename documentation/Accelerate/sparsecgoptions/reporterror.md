# reportError

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

An optional error-reporting routine.

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
var reportError: ((UnsafePointer<CChar>) -> Void)?
```

```c
void (*)(const char *) reportError;
```

## See Also

### Inspecting CG Options
- [var atol: Double](./atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](./maxiterations.md)
  The maximum number of iterations to perform.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](./reportstatus.md)
  The function to report status.
- [var rtol: Double](./rtol.md)
  The relative convergence tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/reporterror)*