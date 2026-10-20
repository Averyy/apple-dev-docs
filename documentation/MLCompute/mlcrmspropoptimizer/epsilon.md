# epsilon

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The epsilon value you use to improve numerical stability.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 14.0+

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
var epsilon: Float { get }
```

```objc
@property (nonatomic, readonly) float epsilon;
```

#### Discussion

The default value is `1e-8`.

## See Also

### Inspecting an RMSProp Optimizer
- [var momentumScale: Float](./momentumscale.md)
  A hyper-parameter that specifies the momentum factor.
- [var alpha: Float](./alpha.md)
  The constant for smoothing.
- [var isCentered: Bool](./iscentered.md)
  A Boolean that indicates whether you compute the centered RMSProp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer/epsilon)*