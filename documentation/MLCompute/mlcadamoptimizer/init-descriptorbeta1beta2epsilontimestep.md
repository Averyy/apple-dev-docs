# init(descriptor:beta1:beta2:epsilon:timeStep:)

**Framework**: ML Compute  
**Kind**: init

Creates an Adam optimizer with the values you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, timeStep: Int)
```

## Parameters

- `optimizerDescriptor`: An object for configuring the optimizer.
- `beta1`: The coefficent for computing running averages of gradient. The default value is  .
- `beta2`: The coefficent for computing running averages of square of gradient. The default value is  .
- `epsilon`: The epsilon value for improving numerical stability. The default value is  .
- `timeStep`: The initial timestep for the update. The default value is  .

## See Also

- [convenience init(descriptor: MLCOptimizerDescriptor)](mlcadamoptimizer/init(descriptor:).md)
  Creates an Adam optimizer with the descriptor you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)](mlcadamoptimizer/init(descriptor:beta1:beta2:epsilon:usesamsgrad:timestep:).md)
  Creates an Adam optimizer with the values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamoptimizer/init(descriptor:beta1:beta2:epsilon:timestep:))*