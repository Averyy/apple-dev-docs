# Quadrature

**Framework**: Accelerate  
**Kind**: struct

A structure that approximates the definite integral of a function over a finite interval.

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
struct Quadrature
```

#### Overview

The following code illustrates using a Quadrature structure to calculate the area under a curve, defined by `y = sqrt(radius * radius - pow(x - radius, 2))`:

```swift
let quadrature = Quadrature(integrator: .qags(maxIntervals: 10),
                            absoluteTolerance: 1.0e-8,
                            relativeTolerance: 1.0e-2)

let result = quadrature.integrate(over: 0.0 ... 25.0) { x in
    let radius: Double = 12.5
    return sqrt(radius * radius - pow(x - radius, 2))
}

switch result {
case .success(let integralResult, let estimatedAbsoluteError):
    print("quadrature success:", integralResult,
          estimatedAbsoluteError)
case .failure(let error):
    print("quadrature error:", error.errorDescription)
}
```

Alternatively, you can integrate over a function that uses vectors for its source and destination. For example:

```swift
func vectorExp(x: UnsafeBufferPointer<Double>,
               y: UnsafeMutableBufferPointer<Double>) {
    let radius: Double = 12.5
    for i in 0 ..< x.count {
        y[i] = sqrt(radius * radius - pow(x[i] - radius, 2))
    }
}

let vRresult = quadrature.integrate(over: 0.0 ... diameter,
                                    integrand: vectorExp)
```

## Topics

### Initializers
- [init(integrator: Quadrature.Integrator, absoluteTolerance: Double, relativeTolerance: Double)](quadrature/init(integrator:absolutetolerance:relativetolerance:).md)
  Initializes and returns a quadrature instance.
### Instance Properties
- [var absoluteTolerance: Double](quadrature/absolutetolerance.md)
  The requested absolute tolerance on the result.
- [var relativeTolerance: Double](quadrature/relativetolerance.md)
  The requested relative tolerance on the result.
### Instance Methods
- [func integrate(over: ClosedRange<Double>, integrand: (Double) -> Double) -> Result<(integralResult: Double, estimatedAbsoluteError: Double), Quadrature.Error>](quadrature/integrate(over:integrand:)-2d2y2.md)
  Performs the integration over the supplied scalar function.
- [func integrate(over: ClosedRange<Double>, integrand: (UnsafeBufferPointer<Double>, UnsafeMutableBufferPointer<Double>) -> ()) -> Result<(integralResult: Double, estimatedAbsoluteError: Double), Quadrature.Error>](quadrature/integrate(over:integrand:)-56h8b.md)
  Performs the integration over the supplied vector function.
### Structures
- [Quadrature.QAGPointsPerInterval](quadrature/qagpointsperinterval.md)
  Constants that specify the number of points per interval for the globally adaptive integrator.
### Enumerations
- [Quadrature.Error](quadrature/error.md)
  Errors thrown by the Quadrature structure.
- [Quadrature.Integrator](quadrature/integrator.md)
  Constants that define different integrators.
### Type Aliases
- [typealias quadrature_function_array](quadrature_function_array.md)
- [struct quadrature_integrate_function](quadrature_integrate_function.md)
- [struct quadrature_integrate_options](quadrature_integrate_options.md)

## See Also

- [struct quadrature_integrator](quadrature_integrator.md)
  Constants that specify integration algorithms.
- [struct quadrature_status](quadrature_status.md)
  Constants that indicate the status of a quadrature operation.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature)*