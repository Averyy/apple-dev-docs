# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init

Creates an RMSProp optimizer with the descriptor you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.2+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor)
```

#### Return Value

An RMSProp optimizer.

#### Discussion

Sets [`momentumScale`](mlcsgdoptimizer/momentumscale.md) to `0.0`, [`alpha`](mlcrmspropoptimizer/alpha.md) to `0.99`, [`epsilon`](mlcrmspropoptimizer/epsilon.md) to `1e-8` , and [`isCentered`](mlcrmspropoptimizer/iscentered.md) to `false` by default.

## Parameters

- `optimizerDescriptor`: An object you use to configure the optimizer.

## See Also

- [convenience init(descriptor: MLCOptimizerDescriptor, momentumScale: Float, alpha: Float, epsilon: Float, isCentered: Bool)](mlcrmspropoptimizer/init(descriptor:momentumscale:alpha:epsilon:iscentered:).md)
  Creates an RMSProp optimizer with the descriptor, momentum scale, smoothing, epsilon, and option to compute the centered RMSProp that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcrmspropoptimizer/init(descriptor:))*