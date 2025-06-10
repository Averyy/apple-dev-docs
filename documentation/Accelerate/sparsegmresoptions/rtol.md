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

If [`rtol`](sparsegmresoptions/rtol.md) `= 0`, the operation uses the default value of `sqrt(epsilon)`.

If it’s negative, the system treats [`rtol`](sparsegmresoptions/rtol.md) as `0.0` (it doesn’t use the default).

## See Also

- [var atol: Double](sparsegmresoptions/atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](sparsegmresoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var nvec: Int32](sparsegmresoptions/nvec.md)
  The number of orthogonal vectors the operation maintains.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsegmresoptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparsegmresoptions/reportstatus.md)
  The function to report status.
- [var variant: SparseGMRESVariant_t](sparsegmresoptions/variant.md)
  The exact variant of GMRES to implement.
- [struct SparseGMRESVariant_t](sparsegmresvariant_t.md)
  Defines the exact variant of GMRES to implement


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/rtol)*