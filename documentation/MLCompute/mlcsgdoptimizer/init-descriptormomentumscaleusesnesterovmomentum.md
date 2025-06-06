# init(descriptor:momentumScale:usesNesterovMomentum:)

**Framework**: ML Compute  
**Kind**: init

Create an SGD optimizer with the descriptor, momentum scale, and option to enable Nesterov momentum that you specify.

**Availability**:
- iOS 14.0+
- iPadOS 14.0+
- Mac Catalyst 14.0+
- macOS 11.0+
- tvOS 14.0+

## Declaration

```swift
convenience init(descriptor optimizerDescriptor: MLCOptimizerDescriptor, momentumScale: Float, usesNesterovMomentum: Bool)
```

## Parameters

- `optimizerDescriptor`: An object you use to configure the optimizer.
- `momentumScale`: The momentum scale.
- `usesNesterovMomentum`: A Boolean that indicates whether you enable Nesterov momentum.

## See Also

- [convenience init(descriptor: MLCOptimizerDescriptor)](mlcsgdoptimizer/init(descriptor:).md)
  Creates an SGD optimizer with the descriptor you specify.


---

*[View on Apple Developer](https://developer.apple.com/documentation/mlcompute/mlcsgdoptimizer/init(descriptor:momentumscale:usesnesterovmomentum:))*