# momentumScale

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A hyper-parameter specifying the momentum factor.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var momentumScale: Float { get }
```

```objc
@property (nonatomic, readonly) float momentumScale;
```

#### Discussion

The default value is `0.0`.

## See Also

### Inspecting an SGD Optimizer
- [var usesNesterovMomentum: Bool](./usesnesterovmomentum.md)
  A Boolean that indicates whether you enable Nesterov momentum.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsgdoptimizer/momentumscale)*