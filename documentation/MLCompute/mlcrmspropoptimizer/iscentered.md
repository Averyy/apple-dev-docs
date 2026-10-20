# isCentered

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether you compute the centered RMSProp.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+ - Deprecated in 27.2
- macOS 11.0+ - Deprecated in 27.2
- tvOS 14.0+

> **Deprecated**: Use Metal Performance Shaders Graph or BNNS instead.

## Declaration

```swift
var isCentered: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL isCentered;
```

#### Discussion

If `true`, the optimizer normalizes the gradient by an estimation of its variance. The default value is `false`.

## See Also

### Inspecting an RMSProp Optimizer
- [var momentumScale: Float](./momentumscale.md)
  A hyper-parameter that specifies the momentum factor.
- [var alpha: Float](./alpha.md)
  The constant for smoothing.
- [var epsilon: Float](./epsilon.md)
  The epsilon value you use to improve numerical stability.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer/iscentered)*