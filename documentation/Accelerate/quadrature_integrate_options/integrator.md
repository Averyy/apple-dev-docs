# integrator

**Framework**: Accelerate  
**Kind**: property

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
var integrator: quadrature_integrator
```

#### Discussion

Integrators

Simple non-adaptive automatic integrator using Gauss-Kronrod-Patterson quadrature coefficients. Evaluates 21, or 43, or 87 points in the interval until the requested accuracy is reached. No workspace is necessary for this integrator.

Simple globally adaptive integrator. Allows selection of the number of Gauss-Kronrod points used in each subinterval, and the max number of subintervals.

Global adaptive quadrature based on 21-point or 15-point (if at least one bound is infinite) Gauss–Kronrod quadrature within each subinterval, with acceleration by Peter Wynn’s epsilon algorithm. If at least one of the interval bounds is infinite, this is equivalent to the QUADPACK QAGI routine. Otherwise, this is equivalent to the QUADPACK QAGS routine.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature_integrate_options/integrator)*