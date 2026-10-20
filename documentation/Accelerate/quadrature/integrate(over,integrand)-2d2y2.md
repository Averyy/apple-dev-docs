# integrate(over:integrand:)

**Framework**: Accelerate  
**Kind**: method  
**Role**: Instance Method

Performs the integration over the supplied scalar function.

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
func integrate(over interval: ClosedRange<Double>, integrand: (Double) -> Double) -> Result<(integralResult: Double, estimatedAbsoluteError: Double), Quadrature.Error>
```

## See Also

### Instance Methods
- [func integrate(over: ClosedRange<Double>, integrand: (UnsafeBufferPointer<Double>, UnsafeMutableBufferPointer<Double>) -> ()) -> Result<(integralResult: Double, estimatedAbsoluteError: Double), Quadrature.Error>](./integrate%28over,integrand%29-56h8b.md)
  Performs the integration over the supplied vector function.


---

*[View on Apple Developer](https://developer.apple.com/documentation/accelerate/quadrature/integrate(over:integrand:)-2d2y2)*