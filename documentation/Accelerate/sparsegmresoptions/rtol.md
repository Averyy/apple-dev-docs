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

## Discussion

*‖ b-Ax ‖₂ < [`rtol`](./rtol.md) \* ‖ b-Ax₀ ‖₂ + [`atol`](./atol.md)* indicates convergence.

If [`rtol`](./rtol.md) `= 0`, the operation uses the default value of `sqrt(epsilon)`.

If it’s negative, the system treats [`rtol`](./rtol.md) as `0.0` (it doesn’t use the default).

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
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](./reportstatus.md)
  The function to report status.
- [var variant: SparseGMRESVariant_t](./variant.md)
  The exact variant of GMRES to implement.
- [struct SparseGMRESVariant_t](../sparsegmresvariant_t.md)
  Defines the exact variant of GMRES to implement


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresoptions/rtol)*