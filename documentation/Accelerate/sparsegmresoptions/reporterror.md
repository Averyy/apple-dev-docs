# reportError

**Framework**: Accelerate  
**Kind**: property

An optional error-reporting routine.

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
var reportError: ((UnsafePointer<CChar>) -> Void)?
```

## See Also

- [var atol: Double](sparsegmresoptions/atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](sparsegmresoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var nvec: Int32](sparsegmresoptions/nvec.md)
  The number of orthogonal vectors the operation maintains.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](sparsegmresoptions/reportstatus.md)
  The function to report status.
- [var rtol: Double](sparsegmresoptions/rtol.md)
  The relative convergence tolerance.
- [var variant: SparseGMRESVariant_t](sparsegmresoptions/variant.md)
  The exact variant of GMRES to implement.
- [struct SparseGMRESVariant_t](sparsegmresvariant_t.md)
  Defines the exact variant of GMRES to implement


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/reporterror)*