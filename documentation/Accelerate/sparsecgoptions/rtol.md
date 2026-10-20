# rtol

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The relative convergence tolerance.

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
var rtol: Double
```

```c
double rtol;
```

#### Discussion

*‖ b-Ax ‖₂ < * ‖ b-Ax₀ ‖₂ + `atol`* indicates convergence.

If [`rtol`](./rtol.md) is equal to `0`, the operation uses the default value of `sqrt(epsilon)`.

If it’s negative, the operation treats [`rtol`](./rtol.md) as `0.0` (it doesn’t use the default).

## See Also

### Inspecting CG Options
- [var atol: Double](./atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](./maxiterations.md)
  The maximum number of iterations to perform.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](./reportstatus.md)
  The function to report status.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsecgoptions/rtol)*