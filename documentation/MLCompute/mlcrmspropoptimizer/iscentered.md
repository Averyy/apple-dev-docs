# isCentered

**Framework**: ML Compute  
**Kind**: property

A Boolean that indicates whether you compute the centered RMSProp.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
var isCentered: Bool { get }
```

#### Discussion

If `true`, the optimizer normalizes the gradient by an estimation of its variance. The default value is `false`.

## See Also

- [var momentumScale: Float](mlcrmspropoptimizer/momentumscale.md)
  A hyper-parameter that specifies the momentum factor.
- [var alpha: Float](mlcrmspropoptimizer/alpha.md)
  The constant for smoothing.
- [var epsilon: Float](mlcrmspropoptimizer/epsilon.md)
  The epsilon value you use to improve numerical stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer/iscentered)*