# quadrature_integrate_options

**Framework**: Accelerate  
**Kind**: struct

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
struct quadrature_integrate_options
```

#### Overview

Can be 0, 15, 21, 31, 41, 51, 61. 0 maps to the default 21. Used by the QAG integrator only. Other integrators ignore this value.

If a workspace is provided, this value is ignored, and the number of intervals is limited by workspace_size. The QNG integrator doesn’t require a workspace. The QAG integrator requires at least max_intervals * QUADRATURE_INTEGRATE_QAG_WORKSPACE_PER_INTERVAL bytes in workspace. The QAGS integrator requires at least max_intervals * QUADRATURE_INTEGRATE_QAGS_WORKSPACE_PER_INTERVAL bytes in workspace.

## Topics

### Initializers
- [init()](quadrature_integrate_options/init.md)
- [init(integrator: quadrature_integrator, abs_tolerance: Double, rel_tolerance: Double, qag_points_per_interval: Int, max_intervals: Int)](quadrature_integrate_options/init(integrator:abs_tolerance:rel_tolerance:qag_points_per_interval:max_intervals:).md)
### Instance Properties
- [var abs_tolerance: Double](quadrature_integrate_options/abs_tolerance.md)
- [var integrator: quadrature_integrator](quadrature_integrate_options/integrator.md)
- [var max_intervals: Int](quadrature_integrate_options/max_intervals.md)
- [var qag_points_per_interval: Int](quadrature_integrate_options/qag_points_per_interval.md)
- [var rel_tolerance: Double](quadrature_integrate_options/rel_tolerance.md)

## Relationships

### Conforms To
- [BitwiseCopyable](../Swift/BitwiseCopyable.md)
- [Sendable](../Swift/Sendable.md)

## See Also

- [typealias quadrature_function_array](quadrature_function_array.md)
- [struct quadrature_integrate_function](quadrature_integrate_function.md)


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature_integrate_options)*