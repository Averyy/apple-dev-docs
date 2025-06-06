# epsilon

**Framework**: ML Compute  
**Kind**: property

The epsilon value you use to improve numerical stability.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var epsilon: Float { get }
```

#### Discussion

The default value is `1e-8`.

## See Also

- [var momentumScale: Float](mlcrmspropoptimizer/momentumscale.md)
  A hyper-parameter that specifies the momentum factor.
- [var alpha: Float](mlcrmspropoptimizer/alpha.md)
  The constant for smoothing.
- [var isCentered: Bool](mlcrmspropoptimizer/iscentered.md)
  A Boolean that indicates whether you compute the centered RMSProp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer/epsilon)*