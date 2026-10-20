# Quadrature.Integrator

**Framework**: Accelerate  
**Kind**: enum  
**Role**: Enumeration

Constants that define different integrators.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst 13.0+
- macOS 10.15+
- tvOS 13.0+
- visionOS
- watchOS 6.0+

## Declaration

```swift
enum Integrator
```

## Topics

### Integrators
- [Quadrature.Integrator.qng](./integrator/qng.md)
  Non-adaptive automatic integrator that uses Gauss-Kronrod-Patterson quadrature coefficients.
- [static let nonAdaptive: Quadrature.Integrator](./integrator/nonadaptive.md)
  Non-adaptive automatic integrator that uses Gauss-Kronrod-Patterson quadrature coefficients.
- [case qag(pointsPerInterval: Quadrature.QAGPointsPerInterval, maxIntervals: Int)](./integrator/qag%28pointsperinterval,maxintervals%29.md)
  Globally adaptive integrator.
- [static func adaptive(pointsPerInterval: Quadrature.QAGPointsPerInterval, maxIntervals: Int) -> Quadrature.Integrator](./integrator/adaptive%28pointsperinterval,maxintervals%29.md)
  Globally adaptive integrator.
- [Quadrature.Integrator.qags(maxIntervals:)](./integrator/qags%28maxintervals%29.md)
  Globally adaptive integrator that is based on 21-point or 15-point Gauss–Kronrod quadrature within each subinterval.
- [static func adaptiveWithSingularities(maxIntervals: Int) -> Quadrature.Integrator](./integrator/adaptivewithsingularities%28maxintervals%29.md)
  Globally adaptive integrator that is based on 21-point or 15-point Gauss–Kronrod quadrature within each subinterval.

## See Also

### Enumerations
- [Quadrature.Error](./error.md)
  Errors thrown by the Quadrature structure.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature/integrator)*