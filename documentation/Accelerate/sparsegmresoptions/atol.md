# atol

**Framework**: Accelerate  
**Kind**: property

The absolute convergence tolerance.

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
var atol: Double
```

#### Discussion

 indicates convergence.

## See Also

- [var maxIterations: Int32](sparsegmresoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var nvec: Int32](sparsegmresoptions/nvec.md)
  The number of orthogonal vectors the operation maintains.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](sparsegmresoptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparsegmresoptions/reportstatus.md)
  The function to report status.
- [var rtol: Double](sparsegmresoptions/rtol.md)
  The relative convergence tolerance.
- [var variant: SparseGMRESVariant_t](sparsegmresoptions/variant.md)
  The exact variant of GMRES to implement.
- [struct SparseGMRESVariant_t](sparsegmresvariant_t.md)
  Defines the exact variant of GMRES to implement


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/atol)*