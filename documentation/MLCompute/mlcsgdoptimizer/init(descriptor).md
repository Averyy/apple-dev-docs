# init(descriptor:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Creates an SGD optimizer with the descriptor you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor)
```

```objc
+ (instancetype) optimizerWithDescriptor:(MLCOptimizerDescriptor *) optimizerDescriptor;
```

## Return Value

An SGD optimizer.

## Discussion

Sets [`momentumScale`](./momentumscale.md) to `0.0` and [`usesNesterovMomentum`](./usesnesterovmomentum.md) to `false` by default.

## Parameters

- `optimizerDescriptor`: An object you use to configure the optimizer.

## See Also

### Creating an SGD Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor, momentumScale: Float, usesNesterovMomentum: Bool)](./init%28descriptor,momentumscale,usesnesterovmomentum%29.md)
  Create an SGD optimizer with the descriptor, momentum scale, and option to enable Nesterov momentum that you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsgdoptimizer/init(descriptor:))*