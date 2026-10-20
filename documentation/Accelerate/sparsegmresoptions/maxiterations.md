# maxIterations

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The maximum number of iterations to perform.

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
var maxIterations: Int32
```

```c
int maxIterations;
```

#### Discussion

If `0`, the operation uses the default value of `100`.

## See Also

### Inspecting GMRES Options
- [var atol: Double](./atol.md)
  The absolute convergence tolerance.
- [var nvec: Int32](./nvec.md)
  The number of orthogonal vectors the operation maintains.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](./reportstatus.md)
  The function to report status.
- [var rtol: Double](./rtol.md)
  The relative convergence tolerance.
- [var variant: SparseGMRESVariant_t](./variant.md)
  The exact variant of GMRES to implement.
- [struct SparseGMRESVariant_t](../sparsegmresvariant_t.md)
  Defines the exact variant of GMRES to implement


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/maxiterations)*