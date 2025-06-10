# maxIterations

**Framework**: Accelerate  
**Kind**: property

The maximum number of iterations to perform.

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
var maxIterations: Int32
```

#### Discussion

If `0`, the operation uses the default value of `100`.

## See Also

- [var atol: Double](sparsegmresoptions/atol.md)
  The absolute convergence tolerance.
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

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/maxiterations)*