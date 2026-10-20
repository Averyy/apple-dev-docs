# atol

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The absolute convergence tolerance.

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

#### Discussion

*‖ b-Ax ‖₂ < * ‖ b-Ax₀ ‖₂ + `atol`* indicates convergence.

## See Also

### Inspecting CG Options
- [var maxIterations: Int32](./maxiterations.md)
  The maximum number of iterations to perform.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](./reportstatus.md)
  The function to report status.
- [var rtol: Double](./rtol.md)
  The relative convergence tolerance.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/atol)*