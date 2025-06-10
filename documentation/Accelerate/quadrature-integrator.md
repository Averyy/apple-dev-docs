# quadrature_integrator

**Framework**: Accelerate  
**Kind**: struct

Constants that specify integration algorithms.

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
struct quadrature_integrator
```

## Topics

### Constants
- [init(UInt32)](quadrature_integrator/init(_:).md)
- [init(rawValue: UInt32)](quadrature_integrator/init(rawvalue:).md)
- [var rawValue: UInt32](quadrature_integrator/rawvalue.md)
- [var QUADRATURE_INTEGRATE_QAG: quadrature_integrator](quadrature_integrate_qag.md)
  A constant that specifies a simple globally adaptive integrator.
- [var QUADRATURE_INTEGRATE_QAGS: quadrature_integrator](quadrature_integrate_qags.md)
  A constant that specifies global adaptive quadrature.
- [var QUADRATURE_INTEGRATE_QNG: quadrature_integrator](quadrature_integrate_qng.md)
  A constant that specifies a simple non-adaptive automatic integrator.
- [var QUADRATURE_INTEGRATE_QAGS_WORKSPACE_PER_INTERVAL: Int32](quadrature_integrate_qags_workspace_per_interval.md)
- [var QUADRATURE_INTEGRATE_QAG_WORKSPACE_PER_INTERVAL: Int32](quadrature_integrate_qag_workspace_per_interval.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Equatable](../Swift/Equatable.md)
- [Hashable](../Swift/Hashable.md)
- [RawRepresentable](../Swift/RawRepresentable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [struct Quadrature](quadrature.md)
  A structure that approximates the definite integral of a function over a finite interval.
- [struct quadrature_status](quadrature_status.md)
  Constants that indicate the status of a quadrature operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature_integrator)*