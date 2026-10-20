# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates a default optimizer with the descriptor you specify.

**Availability**:
- iOS 15.0+ - Deprecated in 17.4
- iPadOS 15.0+ - Deprecated in 17.4
- Mac Catalyst 15.0+ - Deprecated in 17.4
- macOS 12.0+ - Deprecated in 14.3
- tvOS 15.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor)
```

```objc
+ (instancetype) optimizerWithDescriptor:(MLCOptimizerDescriptor *) optimizerDescriptor;
```

#### Return Value

An AdamW optimizer.

#### Discussion

Sets [`beta1`](./beta1.md) to `0.9`, [`beta2`](./beta2.md) to `0.999`, [`epsilon`](./epsilon.md) to `1e-8`, [`usesAMSGrad`](./usesamsgrad.md) to `false`, and [`timeStep`](./timestep.md) to `1` by default.

## Parameters

- `optimizerDescriptor`: An object for configuring the optimizer.

## See Also

### Creating an AdamW Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor, beta1: Float, beta2: Float, epsilon: Float, usesAMSGrad: Bool, timeStep: Int)](./init%28descriptor,beta1,beta2,epsilon,usesamsgrad,timestep%29.md)
  Creates an AdamW optimizer with the values you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcadamwoptimizer/init(descriptor:))*