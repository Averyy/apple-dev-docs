# alpha

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The constant for smoothing.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 14.0+

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
var alpha: Float { get }
```

```objc
@property (nonatomic, readonly) float alpha;
```

#### Discussion

The default value is `0.99`.

## See Also

### Inspecting an RMSProp Optimizer
- [var momentumScale: Float](./momentumscale.md)
  A hyper-parameter that specifies the momentum factor.
- [var epsilon: Float](./epsilon.md)
  The epsilon value you use to improve numerical stability.
- [var isCentered: Bool](./iscentered.md)
  A Boolean that indicates whether you compute the centered RMSProp.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer/alpha)*