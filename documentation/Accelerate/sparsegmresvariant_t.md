# SparseGMRESVariant_t

**Framework**: Accelerate  
**Kind**: struct  
**Role**: Structure

Defines the exact variant of GMRES to implement

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
struct SparseGMRESVariant_t
```

```c
typedef enum { ... } SparseGMRESVariant_t;
```

## Topics

### Constants
- [var SparseVariantDQGMRES: SparseGMRESVariant_t](./sparsevariantdqgmres.md)
  A constant that specifies the DQGMRES variant.
- [var SparseVariantFGMRES: SparseGMRESVariant_t](./sparsevariantfgmres.md)
  A constant that specifies the flexible GMRES variant.
- [var SparseVariantGMRES: SparseGMRESVariant_t](./sparsevariantgmres.md)
  A constant that specifies the standard restarted GMRES variant.
### Raw Values
- [init(UInt8)](./sparsegmresvariant_t/init%28_%29.md)
- [init(rawValue: UInt8)](./sparsegmresvariant_t/init%28rawvalue%29.md)
- [var rawValue: UInt8](./sparsegmresvariant_t/rawvalue.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/bitwisecopyable.md)
- [Equatable](../Swift/equatable.md)
- [Hashable](../Swift/hashable.md)
- [RawRepresentable](../Swift/rawrepresentable.md)
- [Sendable](../Swift/sendable.md)

## See Also

### Inspecting GMRES Options
- [var atol: Double](./sparsegmresoptions/atol.md)
  The absolute convergence tolerance.
- [var maxIterations: Int32](./sparsegmresoptions/maxiterations.md)
  The maximum number of iterations to perform.
- [var nvec: Int32](./sparsegmresoptions/nvec.md)
  The number of orthogonal vectors the operation maintains.
- [var reportError: ((UnsafePointer<CChar>) -> Void)?](./sparsegmresoptions/reporterror.md)
  An optional error-reporting routine.
- [var reportStatus: ((UnsafePointer<CChar>) -> Void)?](./sparsegmresoptions/reportstatus.md)
  The function to report status.
- [var rtol: Double](./sparsegmresoptions/rtol.md)
  The relative convergence tolerance.
- [var variant: SparseGMRESVariant_t](./sparsegmresoptions/variant.md)
  The exact variant of GMRES to implement.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/sparsegmresvariant_t)*