# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init

Creates an Adam optimizer with the descriptor you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor)
```

#### Return Value

An Adam optimizer.

#### Discussion

Sets [`beta1`](mlcadamoptimizer/beta1.md) to `0.9`, [`beta2`](mlcadamoptimizer/beta2.md) to `0.999`, [`epsilon`](mlcadamoptimizer/epsilon.md) to `1e-8`, [`usesAMSGrad`](mlcadamoptimizer/usesamsgrad.md) to `false`, and [`timeStep`](mlcadamoptimizer/timestep.md) to `1` by default.

## Parameters

- `optimizerDescriptor`: An object for configuring the optimizer.

## See Also

- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, timeStep: Int)](mlcadamoptimizer/init(descriptor:beta1:beta2:epsilon:timestep:).md)
  Creates an Adam optimizer with the values you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)](mlcadamoptimizer/init(descriptor:beta1:beta2:epsilon:usesamsgrad:timestep:).md)
  Creates an Adam optimizer with the values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamoptimizer/init(descriptor:))*