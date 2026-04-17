# Quadrature.Integrator.qng

**Framework**: Accelerate  
**Kind**: case

Non-adaptive automatic integrator that uses Gauss-Kronrod-Patterson quadrature coefficients.

**Availability**:
- iOS 13.0+
- iPadOS 13.0+
- Mac Catalyst ?+
- macOS 10.15+
- tvOS 13.0+
- visionOS ?+
- watchOS 6.0+

## Declaration

```swift
case qng
```

## See Also

- [static let nonAdaptive: Quadrature.Integrator](quadrature/integrator/nonadaptive.md)
  Non-adaptive automatic integrator that uses Gauss-Kronrod-Patterson quadrature coefficients.
- [case qag(pointsPerInterval: Quadrature.QAGPointsPerInterval, maxIntervals: Int)](quadrature/integrator/qag(pointsperinterval:maxintervals:).md)
  Globally adaptive integrator.
- [static func adaptive(pointsPerInterval: Quadrature.QAGPointsPerInterval, maxIntervals: Int) -> Quadrature.Integrator](quadrature/integrator/adaptive(pointsperinterval:maxintervals:).md)
  Globally adaptive integrator.
- [Quadrature.Integrator.qags(maxIntervals:)](quadrature/integrator/qags(maxintervals:).md)
  Globally adaptive integrator that is based on 21-point or 15-point Gauss–Kronrod quadrature within each subinterval.
- [static func adaptiveWithSingularities(maxIntervals: Int) -> Quadrature.Integrator](quadrature/integrator/adaptivewithsingularities(maxintervals:).md)
  Globally adaptive integrator that is based on 21-point or 15-point Gauss–Kronrod quadrature within each subinterval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature/integrator/qng)*