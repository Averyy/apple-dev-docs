# init(descriptor:beta1:beta2:epsilon:usesAMSGrad:timeStep:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an AdamW optimizer with the values you specify.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)
```

```objc
+ (instancetype) optimizerWithDescriptor:(MLCOptimizerDescriptor *) optimizerDescriptor beta1:(float) beta1 beta2:(float) beta2 epsilon:(float) epsilon usesAMSGrad:(BOOL) usesAMSGrad timeStep:(NSUInteger) timeStep;
```

## Parameters

- `optimizerDescriptor`: An object for configuring the optimizer.
- `beta1`: The coefficent for computing running averages of gradient. The default value is `0.9`.
- `beta2`: The coefficent for computing running averages of square of gradient. The default value is `0.999`.
- `epsilon`: The epsilon value for improving numerical stability. The default value is `1e-8`.
- `usesAMSGrad`: A Boolean value that indicates whether to use a variant of the algorithm. The default value is `false`.
- `timeStep`: The initial timestep for the update. The default value is `1`.

## See Also

### Creating an AdamW Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](./init%28descriptor%29.md)
  Creates a default optimizer with the descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamwoptimizer/init(descriptor:beta1:beta2:epsilon:usesamsgrad:timestep:))*