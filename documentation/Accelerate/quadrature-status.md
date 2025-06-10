# quadrature_status

**Framework**: Accelerate  
**Kind**: struct

Constants that indicate the status of a quadrature operation.

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
struct quadrature_status
```

## Topics

### Constants
- [init(Int32)](quadrature_status/init(_:).md)
- [init(rawValue: Int32)](quadrature_status/init(rawvalue:).md)
- [var rawValue: Int32](quadrature_status/rawvalue.md)
- [var QUADRATURE_ALLOC_ERROR: quadrature_status](quadrature_alloc_error.md)
  A constant that indicates that memory allocation failed.
- [var QUADRATURE_ERROR: quadrature_status](quadrature_error.md)
  A constant that indicates that a generic error occurred.
- [var QUADRATURE_INTEGRATE_BAD_BEHAVIOUR_ERROR: quadrature_status](quadrature_integrate_bad_behaviour_error.md)
  A constant that indicates bad integrand behaviour, or that an excessive roundoff error occurred.
- [var QUADRATURE_INTEGRATE_MAX_EVAL_ERROR: quadrature_status](quadrature_integrate_max_eval_error.md)
  A constant that indicates that the requested accuracy limit could not be reached.
- [var QUADRATURE_INTERNAL_ERROR: quadrature_status](quadrature_internal_error.md)
  A constant that indicates that an internal error occurred.
- [var QUADRATURE_INVALID_ARG_ERROR: quadrature_status](quadrature_invalid_arg_error.md)
  A constant that indicates that an invalid argument was passed to the operation.
- [var QUADRATURE_SUCCESS: quadrature_status](quadrature_success.md)
  A constant that indicates that the Quadrature operation was successful.

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
- [struct quadrature_integrator](quadrature_integrator.md)
  Constants that specify integration algorithms.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature_status)*