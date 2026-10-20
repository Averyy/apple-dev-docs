# init(descriptor:momentumScale:usesNesterovMomentum:)

**Framework**: ML Compute  
**Kind**: init  
**Role**: Initializer

Create an SGD optimizer with the descriptor, momentum scale, and option to enable Nesterov momentum that you specify.

**Availability**:
- iOS 14.0+ - Deprecated in 17.4
- iPadOS 14.0+ - Deprecated in 17.4
- Mac Catalyst 14.0+ - Deprecated in 17.4
- macOS 11.0+ - Deprecated in 14.3
- tvOS 14.0+ - Deprecated in 17.4

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor, momentumScale: Float, usesNesterovMomentum: Bool)
```

```objc
+ (instancetype) optimizerWithDescriptor:(MLCOptimizerDescriptor *) optimizerDescriptor momentumScale:(float) momentumScale usesNesterovMomentum:(BOOL) usesNesterovMomentum;
```

## Parameters

- `optimizerDescriptor`: An object you use to configure the optimizer.
- `momentumScale`: The momentum scale.
- `usesNesterovMomentum`: A Boolean that indicates whether you enable Nesterov momentum.

## See Also

### Creating an SGD Optimizer
- [convenience init(descriptor: MLCOptimizerDescriptor)](./init%28descriptor%29.md)
  Creates an SGD optimizer with the descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsgdoptimizer/init(descriptor:momentumscale:usesnesterovmomentum:))*