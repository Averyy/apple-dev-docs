# nvec

**Framework**: Accelerate  
**Kind**: property  
**Role**: Instance Property

The number of orthogonal vectors the operation maintains.

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
var nvec: Int32
```

```c
int nvec;
```

## Discussion

For GMRES and FGMRES variants, this is the number of iterations between restarts. For DQGMRES it’s the number of historical vectors the operation maintains in memory. If [`nvec`](./nvec.md) is less than or equal to `0`, the operation uses the default value of `16`.

## See Also

### Inspecting GMRES Options
- [var atol: Double](./atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](./maxiterations.md)
  The maximum number of iterations to perform.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/nvec)*