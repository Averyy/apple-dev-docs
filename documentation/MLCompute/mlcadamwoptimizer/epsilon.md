# epsilon

**Framework**: ML Compute  
**Kind**: property  
**Role**: Instance Property

The epsilon value for improving numerical stability.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
var epsilon: Float { get }
```

```objc
@property (nonatomic, readonly) float epsilon;
```

## See Also

### Inspecting an AdamW Optimizer
- [var beta1: Float](./beta1.md)
  The coefficent for computing running averages of gradient.
- [var beta2: Float](./beta2.md)
  The coefficent for computing running averages of square of gradient.
- [var timeStep: Int](./timestep.md)
  The initial timestep for the update.
- [var usesAMSGrad: Bool](./usesamsgrad.md)
  A Boolean value that indicates whether to use a variant of the algorithm.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamwoptimizer/epsilon)*