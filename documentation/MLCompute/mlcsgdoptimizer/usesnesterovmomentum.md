# usesNesterovMomentum

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

A Boolean that indicates whether you enable Nesterov momentum.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
var usesNesterovMomentum: Bool { get }
```

```objc
@property (nonatomic, readonly) BOOL usesNesterovMomentum;
```

#### Discussion

The default value is `false`.

## See Also

### Inspecting an SGD Optimizer
- [var momentumScale: Float](./momentumscale.md)
  A hyper-parameter specifying the momentum factor.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsgdoptimizer/usesnesterovmomentum)*