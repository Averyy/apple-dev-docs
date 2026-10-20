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

### Inspecting GMRES Options
- [var atol: Double](./atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](./maxiterations.md)
  The maximum number of iterations to perform.
- [var nvec: Int32](./nvec.md)
  The number of orthogonal vectors the operation maintains.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  An optional error-reporting routine.
- [var rtol: Double](./rtol.md)
  The relative convergence tolerance.
- [var variant: SparseGMRESVariant_t](./variant.md)
  The exact variant of GMRES to implement.
- [struct SparseGMRESVariant_t](../sparsegmresvariant_t.md)
  Defines the exact variant of GMRES to implement


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/reportstatus)*