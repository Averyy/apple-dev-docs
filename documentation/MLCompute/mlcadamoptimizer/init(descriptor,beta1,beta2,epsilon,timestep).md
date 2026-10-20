# init(descriptor:beta1:beta2:epsilon:timeStep:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an Adam optimizer with the values you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, timeStep: Int)
```

```objc
+ (instancetype) optimizerWithDescriptor:(MLCOptimizerDescriptor *) optimizerDescriptor beta1:(float) beta1 beta2:(float) beta2 epsilon:(float) epsilon timeStep:(NSUInteger) timeStep;
```

## Parameters

- `optimizerDescriptor`: An object for configuring the optimizer.
- `beta1`: The coefficent for computing running averages of gradient. The default value is `0.9`.
- `beta2`: The coefficent for computing running averages of square of gradient. The default value is `0.999`.
- `epsilon`: The epsilon value for improving numerical stability. The default value is `1e-8`.
- `timeStep`: The initial timestep for the update. The default value is `1`.

## See Also

### Creating an Adam Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](./init%28descriptor%29.md)
  Creates an Adam optimizer with the descriptor you specify.
- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)](./init%28descriptor,beta1,beta2,epsilon,usesamsgrad,timestep%29.md)
  Creates an Adam optimizer with the values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamoptimizer/init(descriptor:beta1:beta2:epsilon:timestep:))*