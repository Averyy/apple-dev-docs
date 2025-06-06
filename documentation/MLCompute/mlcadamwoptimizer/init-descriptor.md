# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init

Creates a default optimizer with the descriptor you specify.

**Availability**:
- iOS 15.0+
- iPadOS 15.0+
- Mac Catalyst 15.0+
- macOS 12.0+
- tvOS 15.0+

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor)
```

#### Return Value

An AdamW optimizer.

#### Discussion

Sets [`beta1`](mlcadamwoptimizer/beta1.md) to `0.9`, [`beta2`](mlcadamwoptimizer/beta2.md) to `0.999`, [`epsilon`](mlcadamwoptimizer/epsilon.md) to `1e-8`, [`usesAMSGrad`](mlcadamwoptimizer/usesamsgrad.md) to `false`, and [`timeStep`](mlcadamwoptimizer/timestep.md) to `1` by default.

## Parameters

- `optimizerDescriptor`: An object for configuring the optimizer.

## See Also

- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)](mlcadamwoptimizer/init(descriptor:beta1:beta2:epsilon:usesamsgrad:timestep:).md)
  Creates an AdamW optimizer with the values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamwoptimizer/init(descriptor:))*