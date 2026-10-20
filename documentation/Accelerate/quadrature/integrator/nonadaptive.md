# nonAdaptive

**Framework**: Accelerate  
**Kind**: property  
**Role**: Type Property

Non-adaptive automatic integrator that uses Gauss-Kronrod-Patterson quadrature coefficients.

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
static let nonAdaptive: Quadrature.Integrator
```

## See Also

### Integrators
- [Quadrature.Integrator.qng](./qng.md)
  Non-adaptive automatic integrator that uses Gauss-Kronrod-Patterson quadrature coefficients.
- [case qag(pointsPerInterval: Quadrature.QAGPointsPerInterval, maxIntervals: Int)](./qag%28pointsperinterval,maxintervals%29.md)
  Globally adaptive integrator.
- [static func adaptive(pointsPerInterval: Quadrature.QAGPointsPerInterval, maxIntervals: Int) -> Quadrature.Integrator](./adaptive%28pointsperinterval,maxintervals%29.md)
  Globally adaptive integrator.
- [Quadrature.Integrator.qags(maxIntervals:)](./qags%28maxintervals%29.md)
  Globally adaptive integrator that is based on 21-point or 15-point Gauss–Kronrod quadrature within each subinterval.
- [static func adaptiveWithSingularities(maxIntervals: Int) -> Quadrature.Integrator](./adaptivewithsingularities%28maxintervals%29.md)
  Globally adaptive integrator that is based on 21-point or 15-point Gauss–Kronrod quadrature within each subinterval.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature/integrator/nonadaptive)*